import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

layouts = {
    r"app\views\layouts\public_header.php": """<!DOCTYPE html>
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
</head>
<body>
    <div id="spa-loader"></div>

    <nav class="navbar navbar-expand-lg fixed-top">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center" href="<?= BASE_URL ?>/">
                <i class="fa-solid fa-leaf text-primary me-2 fs-3"></i>
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
                <div class="d-flex">
                    <?php if(Auth::isLoggedIn()): ?>
                        <a href="<?= Auth::isAdmin() ? BASE_URL.'/admin-dashboard' : BASE_URL.'/member-dashboard' ?>" class="btn btn-outline-primary spa-link me-2">Dashboard</a>
                        <a href="<?= BASE_URL ?>/auth/logout" class="btn btn-primary">Logout</a>
                    <?php else: ?>
                        <a href="<?= BASE_URL ?>/auth/login" class="btn btn-primary spa-link"><i class="fa-solid fa-user me-2"></i>Login Anggota</a>
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
""",

    r"app\views\layouts\public_footer.php": """    </main>

    <footer class="footer">
        <div class="container">
            <div class="row gy-4">
                <div class="col-lg-4 col-md-6">
                    <h4 class="text-white mb-4 d-flex align-items-center">
                        <i class="fa-solid fa-leaf text-secondary me-2"></i> Kopma Mawar
                    </h4>
                    <p class="text-light opacity-75">Koperasi Syariah Mawar hadir untuk memberdayakan ekonomi umat dengan prinsip-prinsip syariah yang adil dan transparan.</p>
                    <div class="d-flex gap-3 mt-4">
                        <a href="#"><i class="fa-brands fa-facebook fs-4"></i></a>
                        <a href="#"><i class="fa-brands fa-instagram fs-4"></i></a>
                        <a href="#"><i class="fa-brands fa-youtube fs-4"></i></a>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6">
                    <h5 class="text-white mb-4">Link Cepat</h5>
                    <ul class="list-unstyled d-flex flex-column gap-2">
                        <li><a href="<?= BASE_URL ?>/profile"><i class="fa-solid fa-chevron-right me-2 text-secondary"></i>Tentang Kami</a></li>
                        <li><a href="<?= BASE_URL ?>/product/savings"><i class="fa-solid fa-chevron-right me-2 text-secondary"></i>Simpanan Syariah</a></li>
                        <li><a href="<?= BASE_URL ?>/product/financing"><i class="fa-solid fa-chevron-right me-2 text-secondary"></i>Pembiayaan Syariah</a></li>
                        <li><a href="<?= BASE_URL ?>/membership"><i class="fa-solid fa-chevron-right me-2 text-secondary"></i>Menjadi Anggota</a></li>
                        <li><a href="<?= BASE_URL ?>/faq"><i class="fa-solid fa-chevron-right me-2 text-secondary"></i>FAQ</a></li>
                    </ul>
                </div>
                <div class="col-lg-4 col-md-6">
                    <h5 class="text-white mb-4">Kontak Kami</h5>
                    <ul class="list-unstyled text-light opacity-75 d-flex flex-column gap-3">
                        <li class="d-flex"><i class="fa-solid fa-location-dot mt-1 me-3 text-secondary"></i> Jl. Mawar Raya No. 1, Jakarta Selatan</li>
                        <li class="d-flex"><i class="fa-solid fa-phone mt-1 me-3 text-secondary"></i> 021-1234567</li>
                        <li class="d-flex"><i class="fa-brands fa-whatsapp mt-1 me-3 text-secondary"></i> 0812-3456-7890</li>
                        <li class="d-flex"><i class="fa-solid fa-envelope mt-1 me-3 text-secondary"></i> info@kopma.ppmawar.or.id</li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom text-center">
                <p class="mb-0">&copy; <?= date('Y') ?> Koperasi Syariah Mawar. Hak Cipta Dilindungi.</p>
            </div>
        </div>
    </footer>

    <button id="back-to-top"><i class="fa-solid fa-arrow-up"></i></button>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.css"></script>
    <!-- App JS -->
    <script src="<?= BASE_URL ?>/assets/js/app.js"></script>
</body>
</html>
""",

    r"app\views\layouts\admin_header.php": """<!DOCTYPE html>
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
""",

    r"app\views\layouts\admin_sidebar.php": """<nav id="sidebar">
    <div class="sidebar-header">
        <h3 class="d-flex align-items-center justify-content-center gap-2">
            <i class="fa-solid fa-leaf text-warning"></i> Admin Panel
        </h3>
    </div>
    
    <ul class="sidebar-menu">
        <li>
            <a href="<?= BASE_URL ?>/admin-dashboard" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-dashboard') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-gauge"></i> Dashboard
            </a>
        </li>
        <li class="mt-3 mb-1 px-3 text-secondary small fw-bold text-uppercase">Website</li>
        <li>
            <a href="<?= BASE_URL ?>/admin-profile" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-profile') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-building"></i> Profil Koperasi
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-news" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-news') !== false ? 'active' : '' ?>">
                <i class="fa-regular fa-newspaper"></i> Berita & Artikel
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-gallery" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-gallery') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-images"></i> Galeri
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-faq" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-faq') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-circle-question"></i> FAQ
            </a>
        </li>
        
        <li class="mt-3 mb-1 px-3 text-secondary small fw-bold text-uppercase">Layanan</li>
        <li>
            <a href="<?= BASE_URL ?>/admin-saving-product" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-saving-product') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-wallet"></i> Produk Simpanan
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-financing-product" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-financing-product') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-hand-holding-dollar"></i> Produk Pembiayaan
            </a>
        </li>
        
        <li class="mt-3 mb-1 px-3 text-secondary small fw-bold text-uppercase">Operasional</li>
        <li>
            <a href="<?= BASE_URL ?>/admin-member" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-member') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-users"></i> Data Anggota
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-application" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-application') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-file-signature"></i> Pengajuan
            </a>
        </li>
        <li>
            <a href="<?= BASE_URL ?>/admin-contact" class="<?= strpos($_SERVER['REQUEST_URI'], 'admin-contact') !== false ? 'active' : '' ?>">
                <i class="fa-solid fa-envelope"></i> Pesan Masuk
            </a>
        </li>
        
        <li class="mt-4">
            <a href="<?= BASE_URL ?>/" target="_blank">
                <i class="fa-solid fa-external-link-alt"></i> Lihat Website
            </a>
        </li>
    </ul>
</nav>
""",

    r"app\views\layouts\admin_footer.php": """            </div> <!-- End main-content -->
        </div> <!-- End content -->
    </div> <!-- End wrapper -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="<?= BASE_URL ?>/assets/js/app.js"></script>
</body>
</html>
""",

    r"app\views\layouts\member_sidebar.php": """<div class="card shadow-sm mb-4">
    <div class="card-body text-center p-4">
        <div class="avatar-placeholder mb-3 mx-auto" style="width:80px;height:80px;background:#1B6B3A;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:2rem;">
            <?= substr($_SESSION['name'], 0, 1) ?>
        </div>
        <h5 class="fw-bold mb-1"><?= $_SESSION['name'] ?></h5>
        <p class="text-muted small mb-0">Anggota Koperasi</p>
    </div>
    <div class="list-group list-group-flush border-top">
        <a href="<?= BASE_URL ?>/member-dashboard" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'member-dashboard') !== false && !strpos($_SERVER['REQUEST_URI'], '/') ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-gauge me-2 w-20px"></i> Dashboard
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/profile" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'profile') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-user me-2 w-20px"></i> Profil Saya
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/savings" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'savings') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-wallet me-2 w-20px"></i> Simpanan Saya
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/financing" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'financing') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-hand-holding-dollar me-2 w-20px"></i> Pembiayaan
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/installments" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'installments') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-calendar-check me-2 w-20px"></i> Riwayat Angsuran
        </a>
        <a href="<?= BASE_URL ?>/auth/logout" class="list-group-item list-group-item-action text-danger">
            <i class="fa-solid fa-right-from-bracket me-2 w-20px"></i> Keluar
        </a>
    </div>
</div>
"""
}

for rel_path, content in layouts.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Layouts created successfully.")
