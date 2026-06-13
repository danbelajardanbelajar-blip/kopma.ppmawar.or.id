<?php
$host = 'localhost';
$db   = 'koperasi_mawar';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
    
    // 1. Update Profile
    $vision = "Menjadi koperasi terbaik di Indonesia.";
    $mission = "1. Menciptakan kesejahteraan bagi para anggota yang berkesinambungan.\n2. Berdaya guna sebagai mitra strategis dan terpercaya bagi anggota.\n3. Berkontribusi dalam perkembangan perkoperasian di Indonesia.\n4. Mengelola Koperasi dan unit usaha secara profesional dengan menerapkan prinsip \"good corporate governance\".";
    
    $stmt = $pdo->prepare("UPDATE profiles SET vision = ?, mission = ? WHERE id = 1");
    $stmt->execute([$vision, $mission]);
    
    // 2. Update Savings Products (Min Amount = 10000)
    $stmt = $pdo->prepare("UPDATE savings_products SET min_amount = 10000");
    $stmt->execute();
    
    echo "Database updated successfully!\n";
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}
