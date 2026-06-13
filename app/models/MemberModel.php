<?php
class MemberModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($limit = 10, $offset = 0) {
        $stmt = $this->db->prepare("SELECT m.*, u.name, u.email, u.status as user_status FROM members m JOIN users u ON m.user_id = u.id ORDER BY m.created_at DESC LIMIT ? OFFSET ?");
        $stmt->bindValue(1, (int)$limit, PDO::PARAM_INT);
        $stmt->bindValue(2, (int)$offset, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT m.*, u.name, u.email, u.status as user_status FROM members m JOIN users u ON m.user_id = u.id WHERE m.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function findByUserId($userId) {
        $stmt = $this->db->prepare("SELECT m.*, u.name, u.email, u.status as user_status FROM members m JOIN users u ON m.user_id = u.id WHERE m.user_id = ?");
        $stmt->execute([$userId]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO members (user_id, member_code, nik, phone, address, join_date, status, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['user_id'],
            $data['member_code'],
            $data['nik'],
            $data['phone'],
            $data['address'],
            $data['join_date'] ?? date('Y-m-d'),
            $data['status'] ?? 'active'
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE members SET nik = ?, phone = ?, address = ?, status = ? WHERE id = ?");
        return $stmt->execute([
            $data['nik'],
            $data['phone'],
            $data['address'],
            $data['status'],
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM members WHERE id = ?");
        return $stmt->execute([$id]);
    }

    public function count() {
        $stmt = $this->db->query("SELECT COUNT(*) FROM members");
        return $stmt->fetchColumn();
    }

    public function search($keyword) {
        $keyword = "%{$keyword}%";
        $stmt = $this->db->prepare("SELECT m.*, u.name, u.email FROM members m JOIN users u ON m.user_id = u.id WHERE u.name LIKE ? OR m.member_code LIKE ? OR m.nik LIKE ?");
        $stmt->execute([$keyword, $keyword, $keyword]);
        return $stmt->fetchAll();
    }

    public function findByMemberCode($code) {
        $stmt = $this->db->prepare("SELECT m.*, u.name, u.email FROM members m JOIN users u ON m.user_id = u.id WHERE m.member_code = ?");
        $stmt->execute([$code]);
        return $stmt->fetch();
    }
}
