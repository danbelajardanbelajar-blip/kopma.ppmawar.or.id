<?php
class ContactModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function get() {
        $stmt = $this->db->query("SELECT * FROM contacts LIMIT 1");
        $contact = $stmt->fetch();
        if (!$contact) {
            $this->db->query("INSERT INTO contacts (koperasi_name, created_at) VALUES ('Koperasi Mawar', NOW())");
            $stmt = $this->db->query("SELECT * FROM contacts LIMIT 1");
            return $stmt->fetch();
        }
        return $contact;
    }

    public function update($data) {
        $stmt = $this->db->prepare("UPDATE contacts SET koperasi_name = ?, address = ?, phone = ?, email = ?, wa_number = ?, maps_embed = ?, office_hours = ? WHERE id = 1");
        return $stmt->execute([
            $data['koperasi_name'],
            $data['address'],
            $data['phone'],
            $data['email'],
            $data['wa_number'],
            $data['maps_embed'],
            $data['office_hours']
        ]);
    }
}
