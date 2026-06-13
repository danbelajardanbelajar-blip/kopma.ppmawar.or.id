<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h4 class="fw-bold mb-0">Pembiayaan Saya</h4>
                    <a href="<?= BASE_URL ?>/member-dashboard/applyFinancing" class="btn btn-primary rounded-pill"><i class="fa-solid fa-plus me-2"></i>Ajukan Baru</a>
                </div>
                
                <?php if($flash = Flash::get()): ?>
                <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                    <?= $flash['message'] ?>
                </div>
                <?php endif; ?>

                <?php if(empty($financings)): ?>
                <div class="card shadow-sm border-0 rounded-4 p-5 text-center">
                    <i class="fa-solid fa-file-invoice-dollar text-muted opacity-50 mb-3" style="font-size: 4rem;"></i>
                    <h5 class="text-muted">Anda belum memiliki riwayat pembiayaan.</h5>
                </div>
                <?php else: ?>
                    <div class="row g-4">
                        <?php foreach($financings as $f): ?>
                        <div class="col-md-6">
                            <div class="card shadow-sm border-0 rounded-4 h-100">
                                <div class="card-header bg-white border-bottom p-3 d-flex justify-content-between align-items-center">
                                    <span class="badge bg-secondary"><?= $f['akad'] ?></span>
                                    <span class="badge <?= $f['status'] == 'active' ? 'bg-success' : 'bg-secondary' ?>"><?= ucfirst($f['status']) ?></span>
                                </div>
                                <div class="card-body p-4">
                                    <h5 class="fw-bold mb-1"><?= $f['product_name'] ?></h5>
                                    <p class="text-muted small mb-4">Mulai: <?= date('d/m/Y', strtotime($f['start_date'])) ?> &mdash; Selesai: <?= date('d/m/Y', strtotime($f['end_date'])) ?></p>
                                    
                                    <div class="d-flex justify-content-between mb-2 pb-2 border-bottom">
                                        <span class="text-muted">Pokok</span>
                                        <span class="fw-bold"><?= Helper::formatRupiah($f['amount']) ?></span>
                                    </div>
                                    <div class="d-flex justify-content-between mb-2 pb-2 border-bottom">
                                        <span class="text-muted">Tenor</span>
                                        <span class="fw-bold"><?= $f['tenor'] ?> Bulan</span>
                                    </div>
                                    <div class="d-flex justify-content-between mt-3">
                                        <span class="text-muted">Angsuran /bln</span>
                                        <h5 class="fw-bold text-danger mb-0"><?= Helper::formatRupiah($f['monthly_payment']) ?></h5>
                                    </div>
                                </div>
                                <div class="card-footer bg-white border-top p-3 text-center">
                                    <a href="<?= BASE_URL ?>/member-dashboard/installments" class="btn btn-outline-primary btn-sm w-100 rounded-pill">Lihat Jadwal Angsuran</a>
                                </div>
                            </div>
                        </div>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
