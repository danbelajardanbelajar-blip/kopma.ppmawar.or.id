<?php
class FinancingModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT f.*, m.member_code, u.name as member_name, fp.name as product_name FROM financings f JOIN members m ON f.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON f.product_id = fp.id ORDER BY f.created_at DESC");
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT f.*, fp.name as product_name, fp.akad FROM financings f JOIN financing_products fp ON f.product_id = fp.id WHERE f.member_id = ? ORDER BY f.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function getActiveByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT f.*, fp.name as product_name FROM financings f JOIN financing_products fp ON f.product_id = fp.id WHERE f.member_id = ? AND f.status = 'active' ORDER BY f.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT f.*, m.member_code, u.name as member_name, fp.name as product_name, fp.akad FROM financings f JOIN members m ON f.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON f.product_id = fp.id WHERE f.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO financings (member_id, product_id, amount, margin_rate, tenor, monthly_payment, start_date, end_date, status, purpose, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['member_id'],
            $data['product_id'],
            $data['amount'],
            $data['margin_rate'],
            $data['tenor'],
            $data['monthly_payment'],
            $data['start_date'],
            $data['end_date'],
            $data['status'] ?? 'active',
            $data['purpose']
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE financings SET status = ? WHERE id = ?");
        return $stmt->execute([
            $data['status'],
            $id
        ]);
    }
}
