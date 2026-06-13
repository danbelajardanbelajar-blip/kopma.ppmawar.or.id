<?php
class FinancingProductModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT * FROM financing_products ORDER BY created_at DESC");
        return $stmt->fetchAll();
    }

    public function findActive() {
        $stmt = $this->db->query("SELECT * FROM financing_products WHERE is_active = 1 ORDER BY created_at DESC");
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM financing_products WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO financing_products (name, type, akad, description, min_amount, max_amount, margin_rate, max_tenor, terms, is_active, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['name'],
            $data['type'],
            $data['akad'],
            $data['description'],
            $data['min_amount'],
            $data['max_amount'],
            $data['margin_rate'],
            $data['max_tenor'],
            $data['terms'],
            $data['is_active'] ?? 1
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE financing_products SET name = ?, type = ?, akad = ?, description = ?, min_amount = ?, max_amount = ?, margin_rate = ?, max_tenor = ?, terms = ?, is_active = ? WHERE id = ?");
        return $stmt->execute([
            $data['name'],
            $data['type'],
            $data['akad'],
            $data['description'],
            $data['min_amount'],
            $data['max_amount'],
            $data['margin_rate'],
            $data['max_tenor'],
            $data['terms'],
            $data['is_active'] ?? 1,
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM financing_products WHERE id = ?");
        return $stmt->execute([$id]);
    }
}
