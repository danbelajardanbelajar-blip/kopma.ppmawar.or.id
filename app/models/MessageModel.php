<?php
class MessageModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($limit = 10, $offset = 0) {
        $stmt = $this->db->prepare("SELECT * FROM messages ORDER BY created_at DESC LIMIT ? OFFSET ?");
        $stmt->bindValue(1, (int)$limit, PDO::PARAM_INT);
        $stmt->bindValue(2, (int)$offset, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM messages WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO messages (name, email, phone, subject, message, is_read, created_at) VALUES (?, ?, ?, ?, ?, 0, NOW())");
        $stmt->execute([
            $data['name'],
            $data['email'],
            $data['phone'],
            $data['subject'],
            $data['message']
        ]);
        return $this->db->lastInsertId();
    }

    public function markRead($id) {
        $stmt = $this->db->prepare("UPDATE messages SET is_read = 1 WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM messages WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function countUnread() {
        $stmt = $this->db->query("SELECT COUNT(*) FROM messages WHERE is_read = 0");
        return $stmt->fetchColumn();
    }
}
