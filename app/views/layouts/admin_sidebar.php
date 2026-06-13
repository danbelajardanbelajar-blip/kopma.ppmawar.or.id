<nav id="sidebar">
    <div class="sidebar-header">
        <h3 class="d-flex align-items-center justify-content-center gap-2">
            <img src="<?= BASE_URL ?>/assets/img/favicon.png" alt="Logo" class="rounded-circle" style="width: 28px; height: 28px; object-fit: cover;"> Admin Panel
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
