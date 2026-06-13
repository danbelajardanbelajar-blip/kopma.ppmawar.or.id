<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= isset($title) ? $title . ' - Admin' : 'Admin Panel' ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="<?= BASE_URL ?>/assets/css/admin.css">
</head>
<body>
    <div id="admin-wrapper">
        <?php include APP_ROOT . '/app/views/layouts/admin_sidebar.php'; ?>
        
        <div id="content">
            <header class="topbar">
                <button class="topbar-btn" onclick="toggleSidebar()">
                    <i class="fa-solid fa-bars"></i>
                </button>
                <div class="d-flex align-items-center">
                    <span class="me-3 fw-medium">Hai, <?= $_SESSION['name'] ?? 'Admin' ?></span>
                    <a href="<?= BASE_URL ?>/auth/logout" class="btn btn-sm btn-danger"><i class="fa-solid fa-right-from-bracket me-1"></i>Keluar</a>
                </div>
            </header>
            
            <div class="main-content">
                <?php if($flash = Flash::get()): ?>
                <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> alert-dismissible fade show">
                    <?= $flash['message'] ?>
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                <?php endif; ?>
