<?php
// Database
define('DB_HOST', 'localhost');
define('DB_NAME', 'koperasi_mawar');
define('DB_USER', 'root');
define('DB_PASS', '');

// App
define('BASE_URL', 'http://localhost/kopma.ppmawar.or.id/public');
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
