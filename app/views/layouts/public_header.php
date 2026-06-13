<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= isset($title) ? $title . ' - ' . APP_NAME : APP_NAME ?></title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="<?= BASE_URL ?>/assets/css/main.css">
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="<?= BASE_URL ?>/assets/img/favicon.png">
</head>
<body>
    <div id="spa-loader"></div>

    <nav class="navbar navbar-expand-lg fixed-top glass-nav">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="<?= BASE_URL ?>/">
                <img src="<?= BASE_URL ?>/assets/img/favicon.png" alt="Logo" class="me-2 rounded-circle" style="width: 32px; height: 32px; object-fit: cover;">
                <span class="fw-bold text-primary">Kopma <span class="text-secondary">Mawar</span></span>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav mx-auto">
                    <li class="nav-item">
                        <a class="nav-link spa-link" href="<?= BASE_URL ?>/">Beranda</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Profil</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/profile">Tentang Koperasi</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/profile/vision">Visi dan Misi</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/profile/management">Struktur Pengurus</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/profile/dps">Dewan Pengawas Syariah</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/profile/legality">Legalitas</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Layanan</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/product/savings">Simpanan Syariah</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/product/financing">Pembiayaan Syariah</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Keanggotaan</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/membership">Syarat & Ketentuan</a></li>
                            <li><a class="dropdown-item spa-link" href="<?= BASE_URL ?>/membership/register">Daftar Anggota</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link spa-link" href="<?= BASE_URL ?>/simulation">Simulasi</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link spa-link" href="<?= BASE_URL ?>/news">Berita</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link spa-link" href="<?= BASE_URL ?>/contact">Kontak</a>
                    </li>
                </ul>
                <div class="d-flex align-items-center gap-2">
                    <a href="<?= BASE_URL ?>/contact" class="btn btn-outline-primary d-none d-lg-inline-block rounded-pill fw-medium"><i class="fa-solid fa-headset me-2"></i>Hubungi Kami</a>
                    <?php if(Auth::isLoggedIn()): ?>
                        <a href="<?= Auth::isAdmin() ? BASE_URL.'/admin-dashboard' : BASE_URL.'/member-dashboard' ?>" class="btn btn-primary btn-modern spa-link"><i class="fa-solid fa-gauge me-2"></i>Dashboard</a>
                    <?php else: ?>
                        <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-modern d-none d-lg-inline-block">Daftar</a>
                        <a href="<?= BASE_URL ?>/auth/login" class="btn btn-primary btn-modern spa-link"><i class="fa-solid fa-user me-1"></i> Login</a>
                    <?php endif; ?>
                </div>
            </div>
        </div>
    </nav>
    <main style="min-height: 80vh;">
    
    <?php if($flash = Flash::get()): ?>
    <div class="container mt-5 pt-5">
        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> alert-dismissible fade show" role="alert">
            <?= $flash['message'] ?>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    </div>
    <?php endif; ?>
