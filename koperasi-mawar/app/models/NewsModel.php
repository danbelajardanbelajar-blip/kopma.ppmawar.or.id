<?php
class NewsModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($limit = null, $offset = 0, $category = null) {
        $query = "SELECT * FROM news";
        $params = [];
        
        if ($category) {
            $query .= " WHERE category = ?";
            $params[] = $category;
        }
        
        $query .= " ORDER BY created_at DESC";
        
        if ($limit !== null) {
            $query .= " LIMIT ? OFFSET ?";
        }
        
        $stmt = $this->db->prepare($query);
        
        if ($category) {
            $stmt->bindValue(1, $category);
            if ($limit !== null) {
                $stmt->bindValue(2, (int)$limit, PDO::PARAM_INT);
                $stmt->bindValue(3, (int)$offset, PDO::PARAM_INT);
            }
        } else if ($limit !== null) {
            $stmt->bindValue(1, (int)$limit, PDO::PARAM_INT);
            $stmt->bindValue(2, (int)$offset, PDO::PARAM_INT);
        }
        
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function findLatest($limit = 5) {
        return $this->findAll($limit, 0);
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM news WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function findBySlug($slug) {
        $stmt = $this->db->prepare("SELECT * FROM news WHERE slug = ? AND is_published = 1");
        $stmt->execute([$slug]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO news (title, slug, content, category, thumbnail, author_id, is_published, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, NOW(), NOW())");
        $stmt->execute([
            $data['title'],
            $data['slug'],
            $data['content'],
            $data['category'],
            $data['thumbnail'] ?? null,
            $data['author_id'],
            $data['is_published'] ?? 1
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE news SET title = ?, slug = ?, content = ?, category = ?, thumbnail = ?, is_published = ?, updated_at = NOW() WHERE id = ?");
        return $stmt->execute([
            $data['title'],
            $data['slug'],
            $data['content'],
            $data['category'],
            $data['thumbnail'],
            $data['is_published'] ?? 1,
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM news WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function count($category = null) {
        $query = "SELECT COUNT(*) FROM news";
        $params = [];
        
        if ($category) {
            $query .= " WHERE category = ?";
            $params[] = $category;
        }
        
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchColumn();
    }
}
