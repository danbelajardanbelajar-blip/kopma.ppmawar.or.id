<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
