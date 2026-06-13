<?php
class InstallmentModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findByFinancingId($financingId) {
        $stmt = $this->db->prepare("SELECT * FROM installments WHERE financing_id = ? ORDER BY due_date ASC");
        $stmt->execute([$financingId]);
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT i.*, f.amount as financing_amount, fp.name as product_name FROM installments i JOIN financings f ON i.financing_id = f.id JOIN financing_products fp ON f.product_id = fp.id WHERE i.member_id = ? ORDER BY i.due_date ASC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function getSchedule($financingId) {
        return $this->findByFinancingId($financingId);
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO installments (financing_id, member_id, due_date, amount, paid_amount, status, created_at) VALUES (?, ?, ?, ?, 0, 'pending', NOW())");
        $stmt->execute([
            $data['financing_id'],
            $data['member_id'],
            $data['due_date'],
            $data['amount']
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE installments SET paid_amount = ?, paid_date = NOW(), status = ? WHERE id = ?");
        return $stmt->execute([
            $data['paid_amount'],
            $data['status'],
            $id
        ]);
    }
}
