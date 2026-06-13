<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
