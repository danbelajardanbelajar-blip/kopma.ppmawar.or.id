<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<!-- Hero Section -->
<section class="hero-modern d-flex align-items-center">
    <div class="container hero-content text-center fade-in-section">
        <span class="badge bg-warning mb-3 py-2 px-4 text-dark fw-bold rounded-pill shadow-sm" style="font-size: 0.9rem;"><i class="fa-solid fa-star me-2"></i>Koperasi Syariah Modern</span>
        <h1 class="display-4 fw-bold mb-4 lh-sm text-white text-shadow" style="text-shadow: 0 4px 15px rgba(0,0,0,0.5);">
            Koperasi Simpan Pinjam dan Pembiayaan Syariah<br>
            <span class="text-secondary">Matholi'ul Anwar</span>
        </h1>
        <p class="lead mb-5 opacity-100 fw-medium mx-auto text-shadow" style="max-width: 700px; text-shadow: 0 2px 10px rgba(0,0,0,0.5);">
            Membangun ekonomi umat yang adil, transparan, dan berkah berlandaskan prinsip-prinsip Syariah Islam tanpa riba.
        </p>
        <div class="d-flex justify-content-center flex-wrap gap-3 mt-2">
            <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-modern btn-lg px-5 shadow-lg">Daftar Anggota Sekarang</a>
            <a href="#produk" class="btn btn-outline-light btn-modern btn-lg px-5 shadow-lg">Lihat Produk</a>
        </div>
    </div>
</section>

<!-- Stats -->
<section class="py-0" style="margin-top: -60px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row g-4 justify-content-center fade-in-section">
            <div class="col-lg-3 col-md-6 col-6">
                <div class="card-modern p-4 text-center h-100">
                    <div class="text-secondary mb-3"><i class="fa-solid fa-users fs-1"></i></div>
                    <h2 class="counter fw-bold text-primary mb-1" data-target="1500">0</h2>
                    <p class="text-muted small fw-medium mb-0">Anggota Aktif</p>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-6">
                <div class="card-modern p-4 text-center h-100">
                    <div class="text-secondary mb-3"><i class="fa-solid fa-wallet fs-1"></i></div>
                    <h2 class="fw-bold text-primary mb-1"><span class="counter" data-target="27">0</span> M</h2>
                    <p class="text-muted small fw-medium mb-0">Total Aset</p>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-6">
                <div class="card-modern p-4 text-center h-100">
                    <div class="text-secondary mb-3"><i class="fa-solid fa-hand-holding-dollar fs-1"></i></div>
                    <h2 class="fw-bold text-primary mb-1"><span class="counter" data-target="10">0</span> M</h2>
                    <p class="text-muted small fw-medium mb-0">Pembiayaan Aktif</p>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-6">
                <div class="card-modern p-4 text-center h-100">
                    <div class="text-secondary mb-3"><i class="fa-solid fa-award fs-1"></i></div>
                    <h2 class="counter fw-bold text-primary mb-1" data-target="17">0</h2>
                    <p class="text-muted small fw-medium mb-0">Tahun Berdiri</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Keunggulan -->
<section class="py-5 mt-5">
    <div class="container py-5">
        <div class="text-center mb-5 fade-in-section">
            <h6 class="text-secondary fw-bold text-uppercase tracking-wider">Mengapa Memilih Kami</h6>
            <h2 class="fw-bold text-primary-dark">Keunggulan Koperasi Mawar</h2>
        </div>
        <div class="row g-4 fade-in-section">
            <div class="col-lg-4 col-md-6">
                <div class="card-modern p-5 h-100">
                    <div class="feature-icon-box shadow-sm">
                        <i class="fa-solid fa-scale-balanced"></i>
                    </div>
                    <h4 class="fw-bold mb-3">100% Syariah</h4>
                    <p class="text-muted mb-0">Sistem bagi hasil yang adil, transparan, dan dipastikan bebas dari unsur Riba, Gharar, serta Maysir.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="card-modern p-5 h-100">
                    <div class="feature-icon-box shadow-sm">
                        <i class="fa-solid fa-shield-halved"></i>
                    </div>
                    <h4 class="fw-bold mb-3">Aman & Terpercaya</h4>
                    <p class="text-muted mb-0">Diawasi langsung oleh Dewan Pengawas Syariah (DPS) dan terdaftar resmi di Kementerian Koperasi.</p>
                </div>
            </div>
            <div class="col-lg-4 col-md-6">
                <div class="card-modern p-5 h-100">
                    <div class="feature-icon-box shadow-sm">
                        <i class="fa-solid fa-mobile-screen-button"></i>
                    </div>
                    <h4 class="fw-bold mb-3">Layanan Digital</h4>
                    <p class="text-muted mb-0">Kemudahan mengakses informasi saldo, riwayat transaksi, hingga pengajuan secara online dari mana saja.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Produk & Layanan -->
<section id="produk" class="py-5 bg-light bg-pattern">
    <div class="container py-5">
        <div class="text-center mb-5 fade-in-section">
            <h6 class="text-secondary fw-bold text-uppercase tracking-wider">Layanan Kami</h6>
            <h2 class="fw-bold text-primary-dark">Produk Unggulan</h2>
        </div>
        <div class="row g-4 align-items-center fade-in-section">
            <div class="col-lg-6">
                <div class="card-modern border-0 overflow-hidden shadow-sm h-100">
                    <div class="row g-0 h-100">
                        <div class="col-md-4 bg-primary text-white d-flex align-items-center justify-content-center p-4">
                            <i class="fa-solid fa-piggy-bank" style="font-size: 4rem; opacity: 0.8;"></i>
                        </div>
                        <div class="col-md-8 p-4">
                            <h4 class="fw-bold text-primary-dark">Simpanan Syariah</h4>
                            <p class="text-muted small mb-3">Investasi amanah dengan imbal hasil yang menarik dan kompetitif melalui akad Mudharabah dan Wadiah.</p>
                            <a href="<?= BASE_URL ?>/product/savings" class="btn btn-sm btn-outline-primary rounded-pill px-4 fw-medium">Pelajari Detail</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="card-modern border-0 overflow-hidden shadow-sm h-100">
                    <div class="row g-0 h-100">
                        <div class="col-md-4 bg-secondary text-white d-flex align-items-center justify-content-center p-4">
                            <i class="fa-solid fa-hand-holding-dollar" style="font-size: 4rem; opacity: 0.8;"></i>
                        </div>
                        <div class="col-md-8 p-4">
                            <h4 class="fw-bold text-primary-dark">Pembiayaan Syariah</h4>
                            <p class="text-muted small mb-3">Solusi permodalan usaha dan kebutuhan konsumtif dengan angsuran ringan melalui akad Murabahah & Ijarah.</p>
                            <a href="<?= BASE_URL ?>/product/financing" class="btn btn-sm btn-outline-secondary rounded-pill px-4 fw-medium">Pelajari Detail</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Alur Anggota & Simulasi -->
<section class="py-5">
    <div class="container py-5">
        <div class="row gy-5 fade-in-section">
            <div class="col-lg-6 pe-lg-5">
                <h6 class="text-secondary fw-bold text-uppercase tracking-wider">Mudah & Cepat</h6>
                <h2 class="fw-bold text-primary-dark mb-4">Cara Menjadi Anggota</h2>
                <div class="d-flex mb-4 align-items-start">
                    <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center flex-shrink-0" style="width: 45px; height: 45px; font-weight: bold;">1</div>
                    <div class="ms-3">
                        <h5 class="fw-bold text-dark mb-1">Daftar Akun Online</h5>
                        <p class="text-muted small">Isi formulir pendaftaran melalui website dengan data diri yang valid (KTP & KK).</p>
                    </div>
                </div>
                <div class="d-flex mb-4 align-items-start">
                    <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center flex-shrink-0" style="width: 45px; height: 45px; font-weight: bold;">2</div>
                    <div class="ms-3">
                        <h5 class="fw-bold text-dark mb-1">Verifikasi Berkas</h5>
                        <p class="text-muted small">Tim kami akan memverifikasi berkas yang dikirim maksimal dalam 1x24 jam kerja.</p>
                    </div>
                </div>
                <div class="d-flex align-items-start">
                    <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center flex-shrink-0" style="width: 45px; height: 45px; font-weight: bold;">3</div>
                    <div class="ms-3">
                        <h5 class="fw-bold text-dark mb-1">Setor Simpanan Pokok</h5>
                        <p class="text-muted small">Lakukan pembayaran Simpanan Pokok dan Anda resmi menikmati fasilitas layanan koperasi.</p>
                    </div>
                </div>
                <a href="<?= BASE_URL ?>/membership/register" class="btn btn-primary btn-modern mt-4">Mulai Pendaftaran <i class="fa-solid fa-arrow-right ms-2"></i></a>
            </div>
            
            <div class="col-lg-6">
                <div class="card-modern p-5 bg-primary text-white position-relative overflow-hidden">
                    <div class="position-absolute top-0 end-0 bg-pattern w-100 h-100" style="opacity: 0.1; pointer-events: none;"></div>
                    <h3 class="fw-bold mb-3 position-relative"><i class="fa-solid fa-calculator me-2 text-secondary"></i> Simulasi Pembiayaan</h3>
                    <p class="opacity-75 small mb-4 position-relative">Ingin tahu estimasi angsuran Anda? Hitung perkiraannya sekarang sebelum mengajukan pembiayaan sungguhan.</p>
                    <form action="<?= BASE_URL ?>/simulation" method="GET" class="form-modern position-relative">
                        <div class="mb-3">
                            <label class="form-label small fw-medium text-white">Plafon (Rp)</label>
                            <input type="number" class="form-control" placeholder="Contoh: 10000000" name="amount" required>
                        </div>
                        <div class="mb-4">
                            <label class="form-label small fw-medium text-white">Tenor / Jangka Waktu</label>
                            <select class="form-select" name="tenor">
                                <option value="12">12 Bulan (1 Tahun)</option>
                                <option value="24">24 Bulan (2 Tahun)</option>
                                <option value="36">36 Bulan (3 Tahun)</option>
                            </select>
                        </div>
                        <button type="submit" class="btn btn-secondary btn-modern w-100">Hitung Simulasi</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Testimonial -->
<section class="py-5 bg-light bg-pattern">
    <div class="container py-5">
        <div class="text-center mb-5 fade-in-section">
            <h6 class="text-secondary fw-bold text-uppercase tracking-wider">Suara Anggota</h6>
            <h2 class="fw-bold text-primary-dark">Apa Kata Mereka?</h2>
        </div>
        <div class="row g-4 fade-in-section">
            <div class="col-md-4">
                <div class="testimonial-card h-100">
                    <p class="text-muted fst-italic mb-4">"Sangat membantu usaha kecil saya. Proses pembiayaan musyarakah-nya sangat transparan dan sesuai dengan syariat. Pengurus juga ramah!"</p>
                    <div class="d-flex align-items-center mt-auto">
                        <div class="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px; font-weight: bold; font-size: 1.2rem;">AF</div>
                        <div class="ms-3">
                            <h6 class="fw-bold mb-0">Ahmad Fauzi</h6>
                            <small class="text-muted">Pedagang Sembako</small>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="testimonial-card h-100">
                    <p class="text-muted fst-italic mb-4">"Alhamdulillah sejak menjadi anggota, tabungan pendidikan anak lebih terencana lewat Simpanan Berjangka. Bebas riba dan menenangkan."</p>
                    <div class="d-flex align-items-center mt-auto">
                        <div class="bg-secondary text-white rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px; font-weight: bold; font-size: 1.2rem;">SR</div>
                        <div class="ms-3">
                            <h6 class="fw-bold mb-0">Siti Rahmawati</h6>
                            <small class="text-muted">Ibu Rumah Tangga</small>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="testimonial-card h-100">
                    <p class="text-muted fst-italic mb-4">"Pelayanan ramah, aplikasi online-nya memudahkan cek saldo dari HP kapan saja. Sangat direkomendasikan bagi yang butuh solusi syariah!"</p>
                    <div class="d-flex align-items-center mt-auto">
                        <div class="bg-dark text-white rounded-circle d-flex align-items-center justify-content-center" style="width: 45px; height: 45px; font-weight: bold; font-size: 1.2rem;">BW</div>
                        <div class="ms-3">
                            <h6 class="fw-bold mb-0">Budi Waseso</h6>
                            <small class="text-muted">Karyawan Swasta</small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Berita Singkat -->
<section class="py-5">
    <div class="container py-5">
        <div class="d-flex justify-content-between align-items-end mb-4 fade-in-section">
            <div>
                <h6 class="text-secondary fw-bold text-uppercase tracking-wider">Kabar Terbaru</h6>
                <h2 class="fw-bold text-primary-dark mb-0">Berita Koperasi</h2>
            </div>
            <a href="<?= BASE_URL ?>/news" class="btn btn-outline-primary btn-modern d-none d-md-block rounded-pill">Lihat Semua Berita</a>
        </div>
        <div class="row g-4 fade-in-section">
            <?php 
            // Dummy array if no news provided via controller yet
            $home_news = [
                ['title' => 'RAT Tahun Buku 2024 Berlangsung Sukses', 'date' => '20 Feb 2025', 'desc' => 'Rapat Anggota Tahunan Koperasi Syariah Matholi\'ul Anwar menetapkan pembagian SHU yang transparan.'],
                ['title' => 'Peluncuran Layanan Digital Kopma Mawar', 'date' => '15 Jan 2025', 'desc' => 'Kini anggota dapat memantau simpanan dan pembiayaan melalui gawai cerdas masing-masing secara realtime.']
            ];
            foreach($home_news as $news):
            ?>
            <div class="col-md-6">
                <div class="card-modern border-0 d-flex flex-row h-100 overflow-hidden">
                    <div class="bg-light p-3 d-flex flex-column justify-content-center text-center" style="min-width: 110px; border-right: 1px solid #e9ecef;">
                        <span class="fs-2 fw-bold text-primary lh-1"><?= explode(' ', $news['date'])[0] ?></span>
                        <span class="text-muted small text-uppercase fw-bold"><?= explode(' ', $news['date'])[1] ?> <?= explode(' ', $news['date'])[2] ?></span>
                    </div>
                    <div class="p-4 d-flex flex-column justify-content-center">
                        <h5 class="fw-bold mb-2"><a href="<?= BASE_URL ?>/news" class="text-dark text-decoration-none" style="transition: color 0.3s;" onmouseover="this.style.color='var(--primary)'" onmouseout="this.style.color='var(--dark)'"><?= $news['title'] ?></a></h5>
                        <p class="text-muted small mb-0"><?= $news['desc'] ?></p>
                    </div>
                </div>
            </div>
            <?php endforeach; ?>
        </div>
        <div class="text-center mt-4 d-md-none">
             <a href="<?= BASE_URL ?>/news" class="btn btn-outline-primary btn-modern w-100">Lihat Semua Berita</a>
        </div>
    </div>
</section>

<!-- CTA -->
<section class="py-5 bg-primary text-white text-center position-relative overflow-hidden fade-in-section">
    <div class="position-absolute top-0 start-0 w-100 h-100 bg-pattern" style="opacity: 0.15;"></div>
    <div class="container py-5 position-relative" style="z-index: 1;">
        <h2 class="fw-bold mb-4 display-5">Siap Bergabung dengan Kami?</h2>
        <p class="lead opacity-75 mb-5 mx-auto" style="max-width: 700px;">Nikmati kemudahan layanan perbankan syariah yang aman, transparan, dan adil untuk kesejahteraan bersama.</p>
        <div class="d-flex justify-content-center flex-wrap gap-3">
            <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-modern btn-lg px-5 shadow-lg">Daftar Sekarang</a>
            <a href="<?= BASE_URL ?>/contact" class="btn btn-outline-light btn-modern btn-lg px-5 shadow-lg">Konsultasi Dulu</a>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
