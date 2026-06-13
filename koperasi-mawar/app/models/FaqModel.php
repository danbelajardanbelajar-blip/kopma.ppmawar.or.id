<?php
class FaqModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT * FROM faqs ORDER BY sort_order ASC, created_at DESC");
        return $stmt->fetchAll();
    }

    public function findActive() {
        $stmt = $this->db->query("SELECT * FROM faqs WHERE is_active = 1 ORDER BY sort_order ASC, created_at DESC");
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM faqs WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO faqs (question, answer, category, sort_order, is_active, created_at) VALUES (?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['question'],
            $data['answer'],
            $data['category'] ?? 'Umum',
            $data['sort_order'] ?? 0,
            $data['is_active'] ?? 1
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE faqs SET question = ?, answer = ?, category = ?, sort_order = ?, is_active = ? WHERE id = ?");
        return $stmt->execute([
            $data['question'],
            $data['answer'],
            $data['category'] ?? 'Umum',
            $data['sort_order'] ?? 0,
            $data['is_active'] ?? 1,
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM faqs WHERE id = ?");
        return $stmt->execute([$id]);
    }
}
