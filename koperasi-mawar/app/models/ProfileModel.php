<?php
class ProfileModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function get() {
        $stmt = $this->db->query("SELECT * FROM profiles LIMIT 1");
        $profile = $stmt->fetch();
        // If empty, create default
        if (!$profile) {
            $this->db->query("INSERT INTO profiles (koperasi_name, created_at) VALUES ('Koperasi Mawar', NOW())");
            $stmt = $this->db->query("SELECT * FROM profiles LIMIT 1");
            return $stmt->fetch();
        }
        return $profile;
    }

    public function update($data) {
        $stmt = $this->db->prepare("UPDATE profiles SET koperasi_name = ?, tagline = ?, description = ?, address = ?, phone = ?, email = ?, wa_number = ?, maps_embed = ?, founded_year = ?, vision = ?, mission = ? WHERE id = 1");
        return $stmt->execute([
            $data['koperasi_name'],
            $data['tagline'],
            $data['description'],
            $data['address'],
            $data['phone'],
            $data['email'],
            $data['wa_number'],
            $data['maps_embed'],
            $data['founded_year'],
            $data['vision'],
            $data['mission']
        ]);
    }
}
