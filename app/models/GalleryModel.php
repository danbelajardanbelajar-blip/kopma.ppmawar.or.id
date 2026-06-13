<?php
class GalleryModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($category = null) {
        $query = "SELECT * FROM galleries";
        $params = [];
        
        if ($category) {
            $query .= " WHERE category = ?";
            $params[] = $category;
        }
        
        $query .= " ORDER BY created_at DESC";
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM galleries WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO galleries (title, description, image, category, created_at) VALUES (?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['title'],
            $data['description'],
            $data['image'],
            $data['category']
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE galleries SET title = ?, description = ?, image = ?, category = ? WHERE id = ?");
        return $stmt->execute([
            $data['title'],
            $data['description'],
            $data['image'],
            $data['category'],
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM galleries WHERE id = ?");
        return $stmt->execute([$id]);
    }
}
