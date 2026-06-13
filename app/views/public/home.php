<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
