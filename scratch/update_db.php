<?php
require_once __DIR__ . '/../config/config.php';
require_once __DIR__ . '/../app/core/Database.php';

try {
    $db = Database::getInstance();

    // 1. Update Profile (Visi & Misi)
    $vision = "Menjadi koperasi terbaik di Indonesia.";
    $mission = "1. Menciptakan kesejahteraan bagi para anggota yang berkesinambungan.\n2. Berdaya guna sebagai mitra strategis dan terpercaya bagi anggota.\n3. Berkontribusi dalam perkembangan perkoperasian di Indonesia.\n4. Mengelola Koperasi dan unit usaha secara profesional dengan menerapkan prinsip \"good corporate governance\".";
    
    $db->query("UPDATE profiles SET vision = :vision, mission = :mission WHERE id = 1");
    $db->bind(':vision', $vision);
    $db->bind(':mission', $mission);
    $db->execute();

    // 2. Update Saving Products Minimum Amount
    // We update the active products to match the SOP
    $db->query("UPDATE savings_products SET min_amount = 10000 WHERE type = 'Wadiah'");
    $db->execute();

    echo "Data successfully updated!";
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
