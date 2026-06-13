<?php
class FinancingApplicationModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($status = null) {
        $query = "SELECT fa.*, m.member_code, u.name as member_name, fp.name as product_name FROM financing_applications fa JOIN members m ON fa.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON fa.product_id = fp.id";
        $params = [];
        
        if ($status) {
            $query .= " WHERE fa.status = ?";
            $params[] = $status;
        }
        
        $query .= " ORDER BY fa.created_at DESC";
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT fa.*, fp.name as product_name FROM financing_applications fa JOIN financing_products fp ON fa.product_id = fp.id WHERE fa.member_id = ? ORDER BY fa.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT fa.*, m.member_code, u.name as member_name, fp.name as product_name FROM financing_applications fa JOIN members m ON fa.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON fa.product_id = fp.id WHERE fa.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO financing_applications (member_id, product_id, amount, tenor, purpose, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, 'pending', NOW(), NOW())");
        $stmt->execute([
            $data['member_id'],
            $data['product_id'],
            $data['amount'],
            $data['tenor'],
            $data['purpose']
        ]);
        return $this->db->lastInsertId();
    }

    public function updateStatus($id, $status, $notes = '') {
        $stmt = $this->db->prepare("UPDATE financing_applications SET status = ?, admin_notes = ?, updated_at = NOW() WHERE id = ?");
        return $stmt->execute([$status, $notes, $id]);
    }

    public function count($status = null) {
        $query = "SELECT COUNT(*) FROM financing_applications";
        $params = [];
        
        if ($status) {
            $query .= " WHERE status = ?";
            $params[] = $status;
        }
        
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchColumn();
    }
}
