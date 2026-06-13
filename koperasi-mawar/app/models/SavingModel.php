<?php
class SavingModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT s.*, m.member_code, u.name as member_name, sp.name as product_name FROM savings s JOIN members m ON s.member_id = m.id JOIN users u ON m.user_id = u.id JOIN savings_products sp ON s.product_id = sp.id ORDER BY s.created_at DESC");
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT s.*, sp.name as product_name, sp.type FROM savings s JOIN savings_products sp ON s.product_id = sp.id WHERE s.member_id = ? ORDER BY s.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT s.*, m.member_code, u.name as member_name, sp.name as product_name FROM savings s JOIN members m ON s.member_id = m.id JOIN users u ON m.user_id = u.id JOIN savings_products sp ON s.product_id = sp.id WHERE s.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO savings (member_id, product_id, amount, balance, last_transaction, status, created_at) VALUES (?, ?, ?, ?, NOW(), ?, NOW())");
        $stmt->execute([
            $data['member_id'],
            $data['product_id'],
            $data['amount'],
            $data['amount'], // Initial balance = amount
            $data['status'] ?? 'active'
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE savings SET balance = ?, last_transaction = NOW(), status = ? WHERE id = ?");
        return $stmt->execute([
            $data['balance'],
            $data['status'],
            $id
        ]);
    }

    public function getTotalByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT SUM(balance) as total FROM savings WHERE member_id = ? AND status = 'active'");
        $stmt->execute([$memberId]);
        return $stmt->fetchColumn() ?: 0;
    }
}
