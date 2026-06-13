import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

files = {
    r"config\config.php": """<?php
// Database
define('DB_HOST', 'localhost');
define('DB_NAME', 'koperasi_mawar');
define('DB_USER', 'root');
define('DB_PASS', '');

// App
define('BASE_URL', 'http://localhost/koperasi-mawar/public');
define('APP_NAME', 'Koperasi Mawar');
define('APP_VERSION', '1.0.0');

// Paths
define('APP_ROOT', dirname(__DIR__));
define('VIEW_PATH', APP_ROOT . '/app/views/');

// Pagination
define('PER_PAGE', 10);

// Upload
define('UPLOAD_PATH', APP_ROOT . '/public/assets/img/uploads/');
define('MAX_FILE_SIZE', 5 * 1024 * 1024); // 5MB
""",
    
    r"app\core\Database.php": """<?php
class Database {
    private static $instance = null;
    private $pdo;

    private function __construct() {
        try {
            $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
            $options = [
                PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES   => false,
            ];
            $this->pdo = new PDO($dsn, DB_USER, DB_PASS, $options);
        } catch (PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }

    public static function getInstance() {
        if (self::$instance == null) {
            self::$instance = new Database();
        }
        return self::$instance;
    }

    public function getConnection() {
        return $this->pdo;
    }
}
""",

    r"app\core\Router.php": """<?php
class Router {
    protected $controller = 'HomeController';
    protected $method = 'index';
    protected $params = [];

    public function parseUrl() {
        if (isset($_GET['url'])) {
            $url = rtrim($_GET['url'], '/');
            $url = filter_var($url, FILTER_SANITIZE_URL);
            $url = explode('/', $url);
            return $url;
        }
        return [];
    }
}
""",

    r"app\core\App.php": """<?php
class App {
    protected $controller = 'HomeController';
    protected $method = 'index';
    protected $params = [];

    public function __construct() {
        $url = $this->parseUrl();

        // Check controller
        $controllerName = isset($url[0]) ? str_replace('-', '', ucwords($url[0], '-')) . 'Controller' : $this->controller;
        if (file_exists(APP_ROOT . '/app/controllers/' . $controllerName . '.php')) {
            $this->controller = $controllerName;
            unset($url[0]);
        }

        require_once APP_ROOT . '/app/controllers/' . $this->controller . '.php';
        $this->controller = new $this->controller;

        // Check method
        if (isset($url[1])) {
            $methodName = lcfirst(str_replace('-', '', ucwords($url[1], '-')));
            if (method_exists($this->controller, $methodName)) {
                $this->method = $methodName;
                unset($url[1]);
            }
        }

        // Setup params
        $this->params = $url ? array_values($url) : [];

        // Call method
        call_user_func_array([$this->controller, $this->method], $this->params);
    }

    public function parseUrl() {
        if (isset($_GET['url'])) {
            $url = rtrim($_GET['url'], '/');
            $url = filter_var($url, FILTER_SANITIZE_URL);
            $url = explode('/', $url);
            return $url;
        }
        return [];
    }
}
""",

    r"app\core\Controller.php": """<?php
class Controller {
    public function view($view, $data = []) {
        if (file_exists(APP_ROOT . '/app/views/' . $view . '.php')) {
            extract($data);
            require_once APP_ROOT . '/app/views/' . $view . '.php';
        } else {
            die("View does not exist: " . $view);
        }
    }

    public function model($model) {
        if (file_exists(APP_ROOT . '/app/models/' . $model . '.php')) {
            require_once APP_ROOT . '/app/models/' . $model . '.php';
            return new $model();
        }
        die("Model does not exist: " . $model);
    }

    public function redirect($url) {
        header('Location: ' . BASE_URL . $url);
        exit;
    }

    public function json($data) {
        header('Content-Type: application/json');
        echo json_encode($data);
        exit;
    }
}
""",

    r"app\helpers\Auth.php": """<?php
class Auth {
    public static function isLoggedIn() {
        return isset($_SESSION['user_id']);
    }

    public static function isAdmin() {
        return self::isLoggedIn() && $_SESSION['role'] === 'admin';
    }

    public static function isMember() {
        return self::isLoggedIn() && $_SESSION['role'] === 'member';
    }

    public static function requireLogin() {
        if (!self::isLoggedIn()) {
            Flash::set('error', 'Anda harus login terlebih dahulu.');
            header('Location: ' . BASE_URL . '/auth/login');
            exit;
        }
    }

    public static function requireAdmin() {
        self::requireLogin();
        if (!self::isAdmin()) {
            Flash::set('error', 'Akses ditolak. Halaman khusus admin.');
            header('Location: ' . BASE_URL . '/');
            exit;
        }
    }

    public static function requireMember() {
        self::requireLogin();
        if (!self::isMember()) {
            Flash::set('error', 'Akses ditolak. Halaman khusus anggota.');
            header('Location: ' . BASE_URL . '/');
            exit;
        }
    }

    public static function getCurrentUser() {
        if (self::isLoggedIn()) {
            return [
                'id' => $_SESSION['user_id'],
                'name' => $_SESSION['name'],
                'role' => $_SESSION['role']
            ];
        }
        return null;
    }

    public static function login($user) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['name'] = $user['name'];
        $_SESSION['role'] = $user['role'];
    }

    public static function logout() {
        session_unset();
        session_destroy();
    }
}
""",

    r"app\helpers\Flash.php": """<?php
class Flash {
    public static function set($type, $message) {
        $_SESSION['flash'] = [
            'type' => $type,
            'message' => $message
        ];
    }

    public static function get() {
        if (isset($_SESSION['flash'])) {
            $flash = $_SESSION['flash'];
            unset($_SESSION['flash']);
            return $flash;
        }
        return null;
    }

    public static function has() {
        return isset($_SESSION['flash']);
    }
}
""",

    r"app\helpers\Helper.php": """<?php
class Helper {
    public static function formatRupiah($amount) {
        return "Rp " . number_format($amount, 0, ',', '.');
    }

    public static function sanitize($input) {
        if (is_array($input)) {
            foreach ($input as $k => $v) {
                $input[$k] = self::sanitize($v);
            }
            return $input;
        }
        return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
    }

    public static function generateMemberCode($lastId = 0) {
        $year = date('Y');
        $nextId = $lastId + 1;
        return "ANG-" . $year . "-" . str_pad($nextId, 4, '0', STR_PAD_LEFT);
    }

    public static function timeAgo($datetime) {
        $time = strtotime($datetime);
        $diff = time() - $time;
        
        if ($diff < 60) return "Baru saja";
        if ($diff < 3600) return floor($diff / 60) . " menit lalu";
        if ($diff < 86400) return floor($diff / 3600) . " jam lalu";
        if ($diff < 2592000) return floor($diff / 86400) . " hari lalu";
        if ($diff < 31536000) return floor($diff / 2592000) . " bulan lalu";
        return floor($diff / 31536000) . " tahun lalu";
    }

    public static function truncate($text, $length = 150) {
        if (strlen($text) <= $length) return $text;
        return substr($text, 0, strrpos(substr($text, 0, $length), ' ')) . '...';
    }

    public static function slugify($text) {
        $text = preg_replace('~[^\pL\d]+~u', '-', $text);
        $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
        $text = preg_replace('~[^-\w]+~', '', $text);
        $text = trim($text, '-');
        $text = preg_replace('~-+~', '-', $text);
        $text = strtolower($text);
        if (empty($text)) return 'n-a';
        return $text;
    }

    public static function uploadImage($file, $directory) {
        if ($file['error'] !== UPLOAD_ERR_OK) {
            return false;
        }

        if ($file['size'] > MAX_FILE_SIZE) {
            return false;
        }

        $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        $mimeType = finfo_file($finfo, $file['tmp_name']);
        finfo_close($finfo);

        if (!in_array($mimeType, $allowedTypes)) {
            return false;
        }

        $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
        $filename = uniqid() . '.' . $extension;
        $target = rtrim($directory, '/') . '/' . $filename;

        if (!is_dir(dirname($target))) {
            mkdir(dirname($target), 0777, true);
        }

        if (move_uploaded_file($file['tmp_name'], $target)) {
            return $filename;
        }

        return false;
    }
}
"""
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Foundation files created successfully.")
