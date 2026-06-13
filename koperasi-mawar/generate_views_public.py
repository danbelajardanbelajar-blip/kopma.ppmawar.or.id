import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

views = {
    r"app\views\public\home.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="hero d-flex align-items-center">
    <div class="container hero-content">
        <div class="row align-items-center gy-5">
            <div class="col-lg-6">
                <span class="badge bg-warning mb-3 py-2 px-3 text-dark fw-bold rounded-pill">Sesuai Syariah Islam</span>
                <h1 class="display-4 fw-bold mb-4 lh-sm">
                    Berkah Bersama<br>
                    <span class="text-secondary">Koperasi Syariah</span><br>
                    Mawar
                </h1>
                <p class="lead mb-4 opacity-75">
                    Solusi keuangan syariah terpercaya untuk pemberdayaan ekonomi umat. Aman, transparan, dan bebas riba.
                </p>
                <div class="d-flex flex-wrap gap-3 mt-4">
                    <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-lg px-4 rounded-pill">Daftar Anggota</a>
                    <a href="<?= BASE_URL ?>/simulation" class="btn btn-outline-light btn-lg px-4 rounded-pill">Simulasi Pembiayaan</a>
                </div>
            </div>
            <div class="col-lg-6 d-none d-lg-block text-center">
                <!-- SVG Illustration Placeholder -->
                <div class="bg-white rounded-circle d-inline-flex align-items-center justify-content-center p-5 shadow-lg" style="width: 400px; height: 400px;">
                    <i class="fa-solid fa-hand-holding-dollar text-primary" style="font-size: 150px;"></i>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Stats -->
<section class="py-5" style="margin-top: -50px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row g-4">
            <div class="col-md-3 col-6">
                <div class="stat-card">
                    <i class="fa-solid fa-users icon"></i>
                    <h3 class="counter" data-target="1500">0</h3>
                    <p class="mb-0 text-muted">Anggota Aktif</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="stat-card">
                    <i class="fa-solid fa-wallet icon"></i>
                    <h3 class="counter" data-target="50">0</h3>
                    <p class="mb-0 text-muted">Miliar Aset</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="stat-card">
                    <i class="fa-solid fa-handshake icon"></i>
                    <h3 class="counter" data-target="850">0</h3>
                    <p class="mb-0 text-muted">Pembiayaan Aktif</p>
                </div>
            </div>
            <div class="col-md-3 col-6">
                <div class="stat-card">
                    <i class="fa-solid fa-award icon"></i>
                    <h3 class="counter" data-target="15">0</h3>
                    <p class="mb-0 text-muted">Tahun Pengalaman</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- About -->
<section class="py-5 my-5 bg-pattern">
    <div class="container">
        <div class="row align-items-center gy-5">
            <div class="col-lg-6">
                <div class="position-relative">
                    <img src="https://images.unsplash.com/photo-1556761175-5973dc0f32d7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Tentang Koperasi" class="img-fluid rounded-4 shadow-lg">
                    <div class="position-absolute bottom-0 end-0 bg-secondary text-white p-4 rounded-4 m-n4 shadow d-none d-md-block">
                        <h4 class="fw-bold mb-0">100%</h4>
                        <p class="mb-0">Prinsip Syariah</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 ps-lg-5">
                <h2 class="section-title text-start">Tentang <?= $profile['koperasi_name'] ?? 'Koperasi Mawar' ?></h2>
                <p class="lead text-muted mb-4"><?= $profile['tagline'] ?? 'Membangun Ekonomi Ummat Berlandaskan Syariah' ?></p>
                <p class="mb-4 text-secondary-emphasis">
                    <?= Helper::truncate($profile['description'] ?? 'Koperasi Syariah Mawar adalah lembaga keuangan mikro syariah yang bertujuan mensejahterakan anggota.', 300) ?>
                </p>
                <ul class="list-unstyled mb-4 d-flex flex-column gap-3">
                    <li class="d-flex align-items-start">
                        <i class="fa-solid fa-check-circle text-primary fs-5 mt-1 me-3"></i>
                        <div>
                            <h5 class="fw-bold mb-1">Aman & Terpercaya</h5>
                            <p class="text-muted mb-0">Diawasi langsung oleh Dewan Pengawas Syariah (DPS) dan Kementerian Koperasi.</p>
                        </div>
                    </li>
                    <li class="d-flex align-items-start">
                        <i class="fa-solid fa-check-circle text-primary fs-5 mt-1 me-3"></i>
                        <div>
                            <h5 class="fw-bold mb-1">Bebas Riba</h5>
                            <p class="text-muted mb-0">Semua transaksi menggunakan akad syariah yang jelas dan transparan.</p>
                        </div>
                    </li>
                </ul>
                <a href="<?= BASE_URL ?>/profile" class="btn btn-outline-primary px-4 rounded-pill">Baca Selengkapnya</a>
            </div>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="py-5 bg-primary text-white text-center">
    <div class="container py-4">
        <h2 class="fw-bold mb-3">Mari Bergabung Menjadi Anggota</h2>
        <p class="lead opacity-75 mb-4 max-w-700 mx-auto">Nikmati berbagai fasilitas layanan keuangan syariah dan jadilah bagian dari kebangkitan ekonomi umat bersama kami.</p>
        <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-lg rounded-pill px-5">Daftar Sekarang</a>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\about.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Tentang Koperasi</h1>
        <p class="lead opacity-75">Mengenal lebih dekat Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow-sm border-0 rounded-4 p-md-5 p-4">
                    <div class="text-center mb-5">
                        <i class="fa-solid fa-building-columns text-primary mb-3" style="font-size: 4rem;"></i>
                        <h2 class="fw-bold"><?= $profile['koperasi_name'] ?? 'Koperasi Mawar' ?></h2>
                        <p class="text-secondary fs-5"><?= $profile['tagline'] ?? '' ?></p>
                    </div>
                    
                    <div class="content lh-lg fs-5 text-secondary-emphasis">
                        <p><?= nl2br($profile['description'] ?? 'Deskripsi belum tersedia.') ?></p>
                    </div>
                    
                    <hr class="my-5 text-muted">
                    
                    <h3 class="fw-bold mb-4 text-center">Informasi Umum</h3>
                    <div class="row g-4">
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-light rounded-3">
                                <i class="fa-solid fa-calendar-check text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0 text-muted">Tahun Berdiri</h6>
                                    <h5 class="mb-0 fw-bold"><?= $profile['founded_year'] ?? '-' ?></h5>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-light rounded-3">
                                <i class="fa-solid fa-location-dot text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0 text-muted">Lokasi</h6>
                                    <h5 class="mb-0 fw-bold">Jakarta Selatan</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\vision.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Visi dan Misi</h1>
        <p class="lead opacity-75">Arah dan tujuan Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-5 justify-content-center">
            <div class="col-lg-10">
                <div class="card shadow-sm border-0 rounded-4 overflow-hidden mb-5 card-hover-lift">
                    <div class="row g-0">
                        <div class="col-md-4 bg-primary text-white p-5 d-flex flex-column justify-content-center align-items-center text-center">
                            <i class="fa-solid fa-eye fs-1 mb-3 text-secondary"></i>
                            <h2 class="fw-bold m-0">VISI</h2>
                        </div>
                        <div class="col-md-8 p-5 d-flex align-items-center">
                            <p class="fs-4 lh-base text-secondary-emphasis fst-italic mb-0">
                                "<?= $profile['vision'] ?? 'Menjadi koperasi syariah terpercaya dan mandiri dalam membangun ekonomi umat yang berkeadilan dan sejahtera.' ?>"
                            </p>
                        </div>
                    </div>
                </div>

                <div class="card shadow-sm border-0 rounded-4 overflow-hidden card-hover-lift">
                    <div class="row g-0">
                        <div class="col-md-4 bg-secondary text-white p-5 d-flex flex-column justify-content-center align-items-center text-center order-md-2">
                            <i class="fa-solid fa-bullseye fs-1 mb-3 text-primary-dark"></i>
                            <h2 class="fw-bold m-0 text-primary-dark">MISI</h2>
                        </div>
                        <div class="col-md-8 p-5 order-md-1">
                            <div class="fs-5 lh-lg text-secondary-emphasis">
                                <?= nl2br($profile['mission'] ?? "1. Memberikan layanan keuangan syariah yang aman, cepat, dan transparan.\n2. Memberdayakan usaha mikro, kecil, dan menengah (UMKM) anggota.\n3. Meningkatkan literasi keuangan syariah di kalangan anggota dan masyarakat.\n4. Membangun sinergi dan kolaborasi ekonomi ummat.") ?>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\management.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Struktur Pengurus</h1>
        <p class="lead opacity-75">Tim di balik Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <h2 class="section-title text-center mb-5">Pengurus Inti</h2>
        <div class="row justify-content-center g-4">
            <!-- Ketua -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 rounded-4 text-center p-4 h-100 card-hover-lift">
                    <div class="mx-auto mb-4 bg-light rounded-circle d-flex align-items-center justify-content-center" style="width: 120px; height: 120px;">
                        <i class="fa-solid fa-user-tie text-primary" style="font-size: 3rem;"></i>
                    </div>
                    <h4 class="fw-bold mb-1">H. Ahmad Fauzi, S.E., M.E.</h4>
                    <p class="text-secondary fw-medium mb-3">Ketua Pengurus</p>
                    <p class="text-muted small">Berpengalaman lebih dari 15 tahun di bidang perbankan syariah dan koperasi.</p>
                </div>
            </div>
            <!-- Sekretaris -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 rounded-4 text-center p-4 h-100 card-hover-lift">
                    <div class="mx-auto mb-4 bg-light rounded-circle d-flex align-items-center justify-content-center" style="width: 120px; height: 120px;">
                        <i class="fa-solid fa-user text-primary" style="font-size: 3rem;"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Hj. Siti Aminah, S.Kom.</h4>
                    <p class="text-secondary fw-medium mb-3">Sekretaris</p>
                    <p class="text-muted small">Fokus pada digitalisasi koperasi dan pelayanan anggota.</p>
                </div>
            </div>
            <!-- Bendahara -->
            <div class="col-md-4">
                <div class="card shadow-sm border-0 rounded-4 text-center p-4 h-100 card-hover-lift">
                    <div class="mx-auto mb-4 bg-light rounded-circle d-flex align-items-center justify-content-center" style="width: 120px; height: 120px;">
                        <i class="fa-solid fa-user text-primary" style="font-size: 3rem;"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Budi Santoso, S.Ak.</h4>
                    <p class="text-secondary fw-medium mb-3">Bendahara</p>
                    <p class="text-muted small">Akuntan bersertifikat syariah yang menjaga transparansi dana.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\dps.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Dewan Pengawas Syariah</h1>
        <p class="lead opacity-75">Penjamin Kesesuaian Syariah Koperasi</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row align-items-center gy-5">
            <div class="col-lg-5 text-center">
                <i class="fa-solid fa-scale-balanced text-primary mb-4" style="font-size: 5rem;"></i>
                <h3 class="fw-bold">Peran DPS</h3>
                <p class="text-muted">Dewan Pengawas Syariah bertugas memastikan bahwa seluruh operasional, produk, dan transaksi Koperasi Mawar berjalan sesuai dengan fatwa DSN-MUI dan prinsip-prinsip syariah Islam.</p>
            </div>
            <div class="col-lg-7">
                <div class="row g-4">
                    <div class="col-sm-6">
                        <div class="card shadow-sm border-0 rounded-4 p-4 text-center h-100 card-hover-lift">
                            <div class="mx-auto mb-3 bg-light rounded-circle d-flex align-items-center justify-content-center" style="width: 100px; height: 100px;">
                                <i class="fa-solid fa-user-graduate text-primary" style="font-size: 2.5rem;"></i>
                            </div>
                            <h5 class="fw-bold mb-1">Dr. K.H. Abdul Rahman, Lc., M.A.</h5>
                            <p class="text-secondary fw-medium mb-0">Ketua DPS</p>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class="card shadow-sm border-0 rounded-4 p-4 text-center h-100 card-hover-lift">
                            <div class="mx-auto mb-3 bg-light rounded-circle d-flex align-items-center justify-content-center" style="width: 100px; height: 100px;">
                                <i class="fa-solid fa-user-graduate text-primary" style="font-size: 2.5rem;"></i>
                            </div>
                            <h5 class="fw-bold mb-1">Ust. M. Yusuf, Lc., M.Sy.</h5>
                            <p class="text-secondary fw-medium mb-0">Anggota DPS</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\legality.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Legalitas</h1>
        <p class="lead opacity-75">Dokumen Resmi dan Perizinan Koperasi</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow border-0 rounded-4 p-5">
                    <h3 class="fw-bold mb-4 text-center">Badan Hukum & Izin Usaha</h3>
                    <div class="table-responsive">
                        <table class="table table-borderless table-striped align-middle">
                            <tbody>
                                <tr>
                                    <th width="40%" class="py-3 text-muted">Badan Hukum</th>
                                    <td class="py-3 fw-medium">No. 1234/BH/M.KUKM.2/XI/2010</td>
                                </tr>
                                <tr>
                                    <th class="py-3 text-muted">Tanggal Pengesahan</th>
                                    <td class="py-3 fw-medium">10 November 2010</td>
                                </tr>
                                <tr>
                                    <th class="py-3 text-muted">Nomor Induk Berusaha (NIB)</th>
                                    <td class="py-3 fw-medium">1234567890123</td>
                                </tr>
                                <tr>
                                    <th class="py-3 text-muted">NPWP</th>
                                    <td class="py-3 fw-medium">01.234.567.8-091.000</td>
                                </tr>
                                <tr>
                                    <th class="py-3 text-muted">Izin Usaha Simpan Pinjam (KSPPS)</th>
                                    <td class="py-3 fw-medium">No. 567/SISP/DEP.1/2011</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="mt-4 pt-4 border-top text-center">
                        <i class="fa-solid fa-file-shield text-success fs-1 mb-3"></i>
                        <h5 class="fw-bold">Resmi dan Terdaftar</h5>
                        <p class="text-muted small mb-0">Koperasi Syariah Mawar telah terdaftar resmi dan diawasi oleh Kementerian Koperasi dan UKM Republik Indonesia.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\savings.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Simpanan Syariah</h1>
        <p class="lead opacity-75">Investasikan dana Anda dengan berkah dan aman sesuai syariat</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-4">
            <?php if(empty($products)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada produk simpanan yang tersedia.</h4>
                </div>
            <?php else: ?>
                <?php foreach($products as $product): ?>
                <div class="col-lg-4 col-md-6">
                    <div class="card shadow-sm border-0 rounded-4 h-100 card-hover-lift">
                        <div class="card-body p-4">
                            <div class="d-flex justify-content-between align-items-center mb-3">
                                <span class="badge <?= $product['type'] == 'Wajib' ? 'bg-danger' : 'bg-primary' ?>"><?= $product['type'] ?></span>
                                <i class="fa-solid fa-wallet text-secondary fs-3"></i>
                            </div>
                            <h4 class="card-title fw-bold text-primary-dark mb-3"><?= $product['name'] ?></h4>
                            <p class="card-text text-muted mb-4"><?= $product['description'] ?></p>
                            
                            <ul class="list-unstyled mb-4 border-top pt-3">
                                <li class="d-flex justify-content-between mb-2">
                                    <span class="text-muted">Min. Setoran:</span>
                                    <span class="fw-bold"><?= Helper::formatRupiah($product['min_amount']) ?></span>
                                </li>
                                <li class="d-flex justify-content-between mb-2">
                                    <span class="text-muted">Bagi Hasil/Nisbah:</span>
                                    <span class="fw-bold text-success"><?= $product['margin_rate'] > 0 ? $product['margin_rate'].'%' : 'Tidak Ada' ?></span>
                                </li>
                            </ul>
                        </div>
                        <div class="card-footer bg-transparent border-top p-4 text-center">
                            <a href="<?= BASE_URL ?>/membership/register" class="btn btn-outline-primary w-100 rounded-pill">Buka Rekening</a>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\financing.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Pembiayaan Syariah</h1>
        <p class="lead opacity-75">Solusi permodalan dan kebutuhan konsumtif tanpa riba</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-4">
            <?php if(empty($products)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada produk pembiayaan yang tersedia.</h4>
                </div>
            <?php else: ?>
                <?php foreach($products as $product): ?>
                <div class="col-lg-6">
                    <div class="card shadow-sm border-0 rounded-4 h-100 card-hover-lift">
                        <div class="row g-0 h-100">
                            <div class="col-md-4 bg-light d-flex flex-column justify-content-center align-items-center p-4 border-end">
                                <i class="fa-solid fa-hand-holding-dollar text-primary mb-3" style="font-size: 3rem;"></i>
                                <span class="badge bg-secondary mb-2"><?= $product['akad'] ?></span>
                                <span class="badge bg-dark"><?= $product['type'] ?></span>
                            </div>
                            <div class="col-md-8 p-4">
                                <h4 class="fw-bold text-primary-dark mb-2"><?= $product['name'] ?></h4>
                                <p class="text-muted mb-3"><?= $product['description'] ?></p>
                                
                                <div class="row g-3 mb-4">
                                    <div class="col-6">
                                        <small class="text-muted d-block">Plafon Maksimal</small>
                                        <strong class="fs-6"><?= Helper::formatRupiah($product['max_amount']) ?></strong>
                                    </div>
                                    <div class="col-6">
                                        <small class="text-muted d-block">Tenor Maksimal</small>
                                        <strong class="fs-6"><?= $product['max_tenor'] ?> Bulan</strong>
                                    </div>
                                    <div class="col-6">
                                        <small class="text-muted d-block">Margin/Bagi Hasil</small>
                                        <strong class="text-success"><?= $product['margin_rate'] ?>% / Tahun</strong>
                                    </div>
                                </div>
                                
                                <a href="<?= BASE_URL ?>/simulation" class="btn btn-outline-primary btn-sm rounded-pill px-3">Hitung Simulasi</a>
                            </div>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
        
        <div class="text-center mt-5 pt-4">
            <h4 class="fw-bold mb-3">Butuh Modal Usaha?</h4>
            <p class="text-muted mb-4">Ajukan pembiayaan syariah sekarang juga untuk mengembangkan usaha Anda.</p>
            <a href="<?= BASE_URL ?>/membership/register" class="btn btn-primary btn-lg rounded-pill px-5">Daftar Menjadi Anggota</a>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\membership.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Keanggotaan</h1>
        <p class="lead opacity-75">Syarat, Hak, dan Kewajiban Anggota Koperasi Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <ul class="nav nav-pills nav-fill mb-4 custom-pills" id="membershipTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active rounded-pill fw-bold" id="syarat-tab" data-bs-toggle="tab" data-bs-target="#syarat-tab-pane" type="button" role="tab" aria-controls="syarat-tab-pane" aria-selected="true">Syarat Keanggotaan</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link rounded-pill fw-bold" id="hak-tab" data-bs-toggle="tab" data-bs-target="#hak-tab-pane" type="button" role="tab" aria-controls="hak-tab-pane" aria-selected="false">Hak & Kewajiban</button>
                    </li>
                </ul>
                
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5">
                    <div class="tab-content" id="myTabContent">
                        <!-- Syarat -->
                        <div class="tab-pane fade show active" id="syarat-tab-pane" role="tabpanel" aria-labelledby="syarat-tab" tabindex="0">
                            <h4 class="fw-bold mb-4 text-primary"><i class="fa-solid fa-list-check me-2"></i>Syarat Menjadi Anggota</h4>
                            <ul class="list-group list-group-flush fs-5">
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Warga Negara Indonesia yang cakap hukum.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Memiliki KTP/Identitas yang sah.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Menyetujui Anggaran Dasar (AD) dan Anggaran Rumah Tangga (ART) Koperasi.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Membayar Simpanan Pokok sebesar Rp 500.000 (sekali bayar).</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Bersedia membayar Simpanan Wajib sebesar Rp 50.000 setiap bulan.</li>
                            </ul>
                            <div class="text-center mt-5">
                                <a href="<?= BASE_URL ?>/membership/register" class="btn btn-primary btn-lg rounded-pill px-5">Daftar Sekarang</a>
                            </div>
                        </div>
                        
                        <!-- Hak & Kewajiban -->
                        <div class="tab-pane fade" id="hak-tab-pane" role="tabpanel" aria-labelledby="hak-tab" tabindex="0">
                            <h4 class="fw-bold mb-4 text-primary"><i class="fa-solid fa-scale-balanced me-2"></i>Hak Anggota</h4>
                            <ul class="list-group list-group-flush mb-5">
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Menghadiri, menyatakan pendapat, dan memberikan suara dalam RAT.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Memilih dan/atau dipilih menjadi anggota Pengurus atau Pengawas.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Meminta diadakan RAT sesuai ketentuan AD/ART.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Mengemukakan pendapat atau saran kepada Pengurus.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Memanfaatkan pelayanan koperasi.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Mendapat bagian Sisa Hasil Usaha (SHU).</li>
                            </ul>
                            
                            <h4 class="fw-bold mb-4 text-danger"><i class="fa-solid fa-clipboard-list me-2"></i>Kewajiban Anggota</h4>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Mematuhi AD, ART, dan Keputusan RAT.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Berpartisipasi dalam kegiatan usaha koperasi.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Mengembangkan dan memelihara kebersamaan berdasar atas asas kekeluargaan.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
.custom-pills .nav-link {
    color: var(--dark);
    transition: all 0.3s;
}
.custom-pills .nav-link.active {
    background-color: var(--primary);
    box-shadow: 0 4px 10px rgba(27, 107, 58, 0.3);
}
</style>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\membership_form.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header pb-5">
    <div class="container">
        <h1 class="display-5 fw-bold">Daftar Anggota</h1>
        <p class="lead opacity-75">Bergabung dan jadilah bagian dari Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5" style="margin-top: -60px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow border-0 rounded-4 overflow-hidden">
                    <div class="card-body p-4 p-md-5">
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/membership/store" method="POST">
                            <h4 class="fw-bold mb-4 border-bottom pb-2">Informasi Pribadi</h4>
                            
                            <div class="row g-3 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nama Lengkap (Sesuai KTP)</label>
                                    <input type="text" name="name" class="form-control" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">NIK (16 Digit)</label>
                                    <input type="text" name="nik" class="form-control" pattern="[0-9]{16}" required>
                                </div>
                                <div class="col-12">
                                    <label class="form-label fw-medium">Alamat Lengkap</label>
                                    <textarea name="address" class="form-control" rows="3" required></textarea>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nomor WhatsApp/HP</label>
                                    <input type="text" name="phone" class="form-control" required>
                                </div>
                            </div>
                            
                            <h4 class="fw-bold mb-4 border-bottom pb-2 mt-5">Informasi Akun Login</h4>
                            
                            <div class="row g-3 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Alamat Email</label>
                                    <input type="email" name="email" class="form-control" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Password</label>
                                    <input type="password" name="password" class="form-control" minlength="6" required>
                                </div>
                            </div>
                            
                            <div class="form-check mt-4 mb-4">
                                <input class="form-check-input" type="checkbox" id="terms" required>
                                <label class="form-check-label text-muted" for="terms">
                                    Saya telah membaca, memahami, dan menyetujui <a href="<?= BASE_URL ?>/membership">Syarat dan Ketentuan Keanggotaan</a> serta Anggaran Dasar Koperasi Syariah Mawar.
                                </label>
                            </div>
                            
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg rounded-pill">Ajukan Pendaftaran</button>
                            </div>
                            
                            <div class="text-center mt-4">
                                <p class="text-muted">Sudah mendaftar dan disetujui? <a href="<?= BASE_URL ?>/auth/login" class="text-primary fw-bold text-decoration-none">Login di sini</a></p>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\login.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px); display: flex; align-items: center;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card shadow border-0 rounded-4 overflow-hidden">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <i class="fa-solid fa-leaf text-primary" style="font-size: 3rem;"></i>
                            <h3 class="fw-bold mt-3 text-primary-dark">Login Anggota</h3>
                            <p class="text-muted">Silakan masuk ke dashboard Anda</p>
                        </div>
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/auth/authenticate" method="POST">
                            <div class="mb-3">
                                <label class="form-label fw-medium">Email</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light"><i class="fa-solid fa-envelope text-muted"></i></span>
                                    <input type="email" name="email" class="form-control" required placeholder="Email terdaftar">
                                </div>
                            </div>
                            <div class="mb-4">
                                <label class="form-label fw-medium">Password</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light"><i class="fa-solid fa-lock text-muted"></i></span>
                                    <input type="password" name="password" class="form-control" required placeholder="********">
                                </div>
                            </div>
                            <div class="d-grid mb-4">
                                <button type="submit" class="btn btn-primary btn-lg rounded-pill">Masuk</button>
                            </div>
                            <div class="text-center">
                                <p class="text-muted mb-0">Belum menjadi anggota? <a href="<?= BASE_URL ?>/membership/register" class="text-secondary fw-bold text-decoration-none">Daftar sekarang</a></p>
                            </div>
                        </form>
                    </div>
                </div>
                
                <div class="text-center mt-4">
                    <a href="<?= BASE_URL ?>/auth/adminLogin" class="text-muted small text-decoration-none"><i class="fa-solid fa-shield-halved me-1"></i> Login sebagai Admin</a>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\simulation.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Simulasi Pembiayaan</h1>
        <p class="lead opacity-75">Hitung estimasi angsuran pembiayaan syariah Anda</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-5">
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5 bg-white">
                    <h4 class="fw-bold mb-4 border-bottom pb-3">Parameter Simulasi</h4>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Produk Pembiayaan</label>
                        <select class="form-select form-select-lg" id="sim_product" onchange="calculateSimulation()">
                            <option value="">Pilih Produk...</option>
                            <?php foreach($products as $p): ?>
                                <option value="<?= $p['id'] ?>" data-margin="<?= $p['margin_rate'] ?>"><?= $p['name'] ?> (<?= $p['akad'] ?> - Margin: <?= $p['margin_rate'] ?>%/thn)</option>
                            <?php endforeach; ?>
                        </select>
                    </div>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Jumlah Pembiayaan (Rp)</label>
                        <input type="text" class="form-control form-control-lg" id="sim_amount" placeholder="Contoh: 10.000.000" onkeyup="calculateSimulation()">
                    </div>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Tenor / Jangka Waktu (Bulan)</label>
                        <input type="number" class="form-control form-control-lg" id="sim_tenor" min="1" max="120" value="12" onkeyup="calculateSimulation()" onchange="calculateSimulation()">
                    </div>
                    
                    <button type="button" class="btn btn-primary w-100 btn-lg rounded-pill" onclick="calculateSimulation()">Hitung Sekarang</button>
                    <p class="text-muted small text-center mt-3">* Hasil simulasi ini adalah estimasi dan dapat berbeda dengan perhitungan riil.</p>
                </div>
            </div>
            
            <div class="col-lg-7">
                <div class="card shadow border-0 rounded-4 p-4 p-md-5 bg-primary text-white h-100" id="simulation_result" style="display:none; background-image: url('data:image/svg+xml,%3Csvg width=\'60\' height=\'60\' viewBox=\'0 0 60 60\' xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cg fill=\'none\' fill-rule=\'evenodd\'%3E%3Cg fill=\'%23ffffff\' fill-opacity=\'0.05\'%3E%3Cpath d=\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');">
                    <h3 class="fw-bold mb-4 text-secondary border-bottom border-light pb-3">Hasil Simulasi</h3>
                    
                    <div class="row g-4 mt-2">
                        <div class="col-sm-6">
                            <div class="p-3 bg-white bg-opacity-10 rounded-3">
                                <p class="mb-1 opacity-75">Pokok Pembiayaan</p>
                                <h4 class="fw-bold mb-0" id="res_amount">Rp 0</h4>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="p-3 bg-white bg-opacity-10 rounded-3">
                                <p class="mb-1 opacity-75">Estimasi Margin</p>
                                <h4 class="fw-bold mb-0" id="res_margin">Rp 0</h4>
                            </div>
                        </div>
                        <div class="col-12 mt-4">
                            <div class="p-4 bg-white rounded-4 text-dark text-center shadow-lg">
                                <p class="mb-1 text-muted fw-bold text-uppercase">Angsuran Per Bulan</p>
                                <h1 class="fw-bold text-primary mb-0 display-5" id="res_monthly">Rp 0</h1>
                            </div>
                        </div>
                        <div class="col-12 mt-4 text-center">
                            <p class="mb-1 opacity-75">Total Pengembalian (Pokok + Margin)</p>
                            <h4 class="fw-bold text-secondary mb-0" id="res_total">Rp 0</h4>
                        </div>
                    </div>
                    
                    <div class="text-center mt-5">
                        <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-lg rounded-pill px-5">Ajukan Pembiayaan</a>
                    </div>
                </div>
                
                <div class="card shadow-sm border-0 rounded-4 p-5 h-100 d-flex justify-content-center align-items-center text-center bg-light" id="simulation_empty" style="display:flex;">
                    <i class="fa-solid fa-calculator text-muted opacity-50 mb-4" style="font-size: 5rem;"></i>
                    <h4 class="text-muted">Masukkan parameter di samping untuk melihat hasil simulasi.</h4>
                </div>
            </div>
        </div>
    </div>
</section>

<script>
    // Hide empty state and show result when calculate is clicked
    const origCalculate = window.calculateSimulation;
    window.calculateSimulation = function() {
        if(origCalculate) origCalculate();
        if(document.getElementById('sim_product').value && document.getElementById('sim_amount').value) {
            document.getElementById('simulation_empty').style.display = 'none';
        }
    }
</script>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\public\news.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Berita & Informasi</h1>
        <p class="lead opacity-75">Kabar terbaru dari Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row mb-5">
            <div class="col-md-8 mx-auto text-center">
                <div class="btn-group shadow-sm" role="group">
                    <a href="<?= BASE_URL ?>/news" class="btn btn-outline-primary <?= empty($category) ? 'active' : '' ?>">Semua</a>
                    <a href="<?= BASE_URL ?>/news?category=Artikel" class="btn btn-outline-primary <?= $category == 'Artikel' ? 'active' : '' ?>">Artikel</a>
                    <a href="<?= BASE_URL ?>/news?category=Kegiatan" class="btn btn-outline-primary <?= $category == 'Kegiatan' ? 'active' : '' ?>">Kegiatan</a>
                    <a href="<?= BASE_URL ?>/news?category=Pengumuman" class="btn btn-outline-primary <?= $category == 'Pengumuman' ? 'active' : '' ?>">Pengumuman</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            <?php if(empty($news)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada berita yang diterbitkan.</h4>
                </div>
            <?php else: ?>
                <?php foreach($news as $item): ?>
                <div class="col-lg-4 col-md-6">
                    <div class="card shadow-sm border-0 rounded-4 h-100 card-hover-lift overflow-hidden">
                        <?php if($item['thumbnail']): ?>
                            <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $item['thumbnail'] ?>" class="card-img-top" alt="<?= $item['title'] ?>" style="height: 200px; object-fit: cover;">
                        <?php else: ?>
                            <div class="bg-light d-flex justify-content-center align-items-center" style="height: 200px;">
                                <i class="fa-regular fa-image text-muted fs-1 opacity-50"></i>
                            </div>
                        <?php endif; ?>
                        <div class="card-body p-4">
                            <div class="d-flex justify-content-between mb-3 align-items-center">
                                <span class="badge bg-secondary"><?= $item['category'] ?></span>
                                <small class="text-muted"><i class="fa-regular fa-calendar me-1"></i> <?= date('d M Y', strtotime($item['created_at'])) ?></small>
                            </div>
                            <h5 class="card-title fw-bold mb-3"><a href="<?= BASE_URL ?>/news/detail/<?= $item['slug'] ?>" class="text-dark text-decoration-none"><?= $item['title'] ?></a></h5>
                            <p class="card-text text-muted"><?= Helper::truncate(strip_tags($item['content']), 100) ?></p>
                        </div>
                        <div class="card-footer bg-transparent border-top-0 px-4 pb-4 pt-0">
                            <a href="<?= BASE_URL ?>/news/detail/<?= $item['slug'] ?>" class="text-primary fw-bold text-decoration-none">Baca Selengkapnya <i class="fa-solid fa-arrow-right ms-1 small"></i></a>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
        
        <?php if($total_pages > 1): ?>
        <nav class="mt-5">
            <ul class="pagination justify-content-center">
                <?php for($i=1; $i<=$total_pages; $i++): ?>
                    <li class="page-item <?= $i == $current_page ? 'active' : '' ?>">
                        <a class="page-link" href="<?= BASE_URL ?>/news?page=<?= $i ?><?= $category ? '&category='.$category : '' ?>"><?= $i ?></a>
                    </li>
                <?php endfor; ?>
            </ul>
        </nav>
        <?php endif; ?>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
"""
}

for rel_path, content in views.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Public Views created successfully.")
