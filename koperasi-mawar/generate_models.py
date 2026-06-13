import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

models = {
    r"app\models\UserModel.php": """<?php
class UserModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findByEmail($email) {
        $stmt = $this->db->prepare("SELECT * FROM users WHERE email = ?");
        $stmt->execute([$email]);
        return $stmt->fetch();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM users WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO users (name, email, password, role, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, NOW(), NOW())");
        $stmt->execute([
            $data['name'], 
            $data['email'], 
            $data['password'], 
            $data['role'] ?? 'member',
            $data['status'] ?? 'active'
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE users SET name = ?, email = ?, updated_at = NOW() WHERE id = ?");
        return $stmt->execute([$data['name'], $data['email'], $id]);
    }

    public function updatePassword($id, $password) {
        $stmt = $this->db->prepare("UPDATE users SET password = ?, updated_at = NOW() WHERE id = ?");
        return $stmt->execute([$password, $id]);
    }
}
""",

    r"app\models\MemberModel.php": """<?php
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
""",

    r"app\models\ProfileModel.php": """<?php
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
""",

    r"app\models\SavingProductModel.php": """<?php
class SavingProductModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT * FROM savings_products ORDER BY created_at DESC");
        return $stmt->fetchAll();
    }

    public function findActive() {
        $stmt = $this->db->query("SELECT * FROM savings_products WHERE is_active = 1 ORDER BY created_at DESC");
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT * FROM savings_products WHERE id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO savings_products (name, type, description, min_amount, margin_rate, terms, is_active, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['name'],
            $data['type'],
            $data['description'],
            $data['min_amount'],
            $data['margin_rate'],
            $data['terms'],
            $data['is_active'] ?? 1
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE savings_products SET name = ?, type = ?, description = ?, min_amount = ?, margin_rate = ?, terms = ?, is_active = ? WHERE id = ?");
        return $stmt->execute([
            $data['name'],
            $data['type'],
            $data['description'],
            $data['min_amount'],
            $data['margin_rate'],
            $data['terms'],
            $data['is_active'] ?? 1,
            $id
        ]);
    }

    public function delete($id) {
        $stmt = $this->db->prepare("DELETE FROM savings_products WHERE id = ?");
        return $stmt->execute([$id]);
    }
}
""",

    r"app\models\FinancingProductModel.php": """<?php
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
""",

    r"app\models\SavingModel.php": """<?php
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
""",

    r"app\models\FinancingModel.php": """<?php
class FinancingModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll() {
        $stmt = $this->db->query("SELECT f.*, m.member_code, u.name as member_name, fp.name as product_name FROM financings f JOIN members m ON f.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON f.product_id = fp.id ORDER BY f.created_at DESC");
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT f.*, fp.name as product_name, fp.akad FROM financings f JOIN financing_products fp ON f.product_id = fp.id WHERE f.member_id = ? ORDER BY f.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function getActiveByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT f.*, fp.name as product_name FROM financings f JOIN financing_products fp ON f.product_id = fp.id WHERE f.member_id = ? AND f.status = 'active' ORDER BY f.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT f.*, m.member_code, u.name as member_name, fp.name as product_name, fp.akad FROM financings f JOIN members m ON f.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON f.product_id = fp.id WHERE f.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO financings (member_id, product_id, amount, margin_rate, tenor, monthly_payment, start_date, end_date, status, purpose, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NOW())");
        $stmt->execute([
            $data['member_id'],
            $data['product_id'],
            $data['amount'],
            $data['margin_rate'],
            $data['tenor'],
            $data['monthly_payment'],
            $data['start_date'],
            $data['end_date'],
            $data['status'] ?? 'active',
            $data['purpose']
        ]);
        return $this->db->lastInsertId();
    }

    public function update($id, $data) {
        $stmt = $this->db->prepare("UPDATE financings SET status = ? WHERE id = ?");
        return $stmt->execute([
            $data['status'],
            $id
        ]);
    }
}
""",

    r"app\models\InstallmentModel.php": """<?php
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
""",

    r"app\models\FinancingApplicationModel.php": """<?php
class FinancingApplicationModel {
    private $db;

    public function __construct() {
        $this->db = Database::getInstance()->getConnection();
    }

    public function findAll($status = null) {
        $query = "SELECT fa.*, m.member_code, u.name as member_name, fp.name as product_name FROM financing_applications fa JOIN members m ON fa.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON fa.product_id = fp.id";
        $params = [];
        
        if ($status) {
            $query .= " WHERE fa.status = ?";
            $params[] = $status;
        }
        
        $query .= " ORDER BY fa.created_at DESC";
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchAll();
    }

    public function findByMemberId($memberId) {
        $stmt = $this->db->prepare("SELECT fa.*, fp.name as product_name FROM financing_applications fa JOIN financing_products fp ON fa.product_id = fp.id WHERE fa.member_id = ? ORDER BY fa.created_at DESC");
        $stmt->execute([$memberId]);
        return $stmt->fetchAll();
    }

    public function findById($id) {
        $stmt = $this->db->prepare("SELECT fa.*, m.member_code, u.name as member_name, fp.name as product_name FROM financing_applications fa JOIN members m ON fa.member_id = m.id JOIN users u ON m.user_id = u.id JOIN financing_products fp ON fa.product_id = fp.id WHERE fa.id = ?");
        $stmt->execute([$id]);
        return $stmt->fetch();
    }

    public function create($data) {
        $stmt = $this->db->prepare("INSERT INTO financing_applications (member_id, product_id, amount, tenor, purpose, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?, 'pending', NOW(), NOW())");
        $stmt->execute([
            $data['member_id'],
            $data['product_id'],
            $data['amount'],
            $data['tenor'],
            $data['purpose']
        ]);
        return $this->db->lastInsertId();
    }

    public function updateStatus($id, $status, $notes = '') {
        $stmt = $this->db->prepare("UPDATE financing_applications SET status = ?, admin_notes = ?, updated_at = NOW() WHERE id = ?");
        return $stmt->execute([$status, $notes, $id]);
    }

    public function count($status = null) {
        $query = "SELECT COUNT(*) FROM financing_applications";
        $params = [];
        
        if ($status) {
            $query .= " WHERE status = ?";
            $params[] = $status;
        }
        
        $stmt = $this->db->prepare($query);
        $stmt->execute($params);
        return $stmt->fetchColumn();
    }
}
""",

    r"app\models\NewsModel.php": """<?php
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
""",

    r"app\models\GalleryModel.php": """<?php
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
""",

    r"app\models\FaqModel.php": """<?php
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
""",

    r"app\models\ContactModel.php": """<?php
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
""",

    r"app\models\MessageModel.php": """<?php
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
"""
}

for rel_path, content in models.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Models created successfully.")
