<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card-modern p-4 p-md-5 mb-4 border-0">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <h3 class="fw-bold mb-0">Hai, <?= $member['name'] ?>!</h3>
                        <span class="badge-status <?= $member['status'] == 'active' ? 'approved' : 'pending' ?>"><?= ucfirst($member['status']) ?></span>
                    </div>
                    <p class="text-muted mb-0">No. Anggota: <strong class="text-dark"><?= $member['member_code'] ?></strong></p>
                </div>
                
                <div class="row g-4 mb-4">
                    <div class="col-md-6">
                        <div class="card-modern p-4 h-100 bg-primary text-white overflow-hidden position-relative">
                            <i class="fa-solid fa-wallet position-absolute" style="font-size: 8rem; right: -20px; bottom: -20px; opacity: 0.1;"></i>
                            <h5 class="opacity-75 mb-3">Total Saldo Simpanan</h5>
                            <h2 class="fw-bold mb-0 display-6"><?= Helper::formatRupiah($total_savings) ?></h2>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card-modern p-4 h-100 bg-secondary text-white overflow-hidden position-relative">
                            <i class="fa-solid fa-hand-holding-dollar position-absolute" style="font-size: 8rem; right: -20px; bottom: -20px; opacity: 0.1;"></i>
                            <h5 class="opacity-75 mb-3">Pembiayaan Aktif</h5>
                            <h2 class="fw-bold mb-0 display-6"><?= count($active_financings) ?> <span class="fs-5 fw-normal">Kontrak</span></h2>
                        </div>
                    </div>
                </div>
                
                <div class="card-modern mb-4">
                    <div class="card-header bg-white border-0 pt-4 pb-0 px-4">
                        <h5 class="fw-bold d-flex justify-content-between align-items-center">
                            Menu Cepat
                        </h5>
                    </div>
                    <div class="card-body p-4">
                        <div class="row g-3">
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/member-dashboard/applyFinancing" class="btn btn-outline-primary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-file-signature fs-3"></i>
                                    <span>Ajukan Pembiayaan</span>
                                </a>
                            </div>
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/member-dashboard/savings" class="btn btn-outline-primary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-money-bill-transfer fs-3"></i>
                                    <span>Riwayat Simpanan</span>
                                </a>
                            </div>
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/simulation" class="btn btn-outline-secondary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-calculator fs-3"></i>
                                    <span>Simulasi Angsuran</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="card-modern">
                    <div class="card-header bg-white border-bottom p-4">
                        <h5 class="fw-bold mb-0">Angsuran Mendatang</h5>
                    </div>
                    <div class="card-body p-4">
                        <div class="table-responsive">
                            <table class="table-modern">
                                <thead>
                                    <tr>
                                        <th class="ps-4">Tenggat Waktu</th>
                                        <th>Produk</th>
                                        <th>Jumlah Tagihan</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($upcoming_installments)): ?>
                                    <tr>
                                        <td colspan="4" class="text-center py-4 text-muted">Belum ada tagihan angsuran.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php 
                                        $count = 0;
                                        foreach($upcoming_installments as $inst): 
                                            if($inst['status'] == 'pending' && $count < 3):
                                                $count++;
                                        ?>
                                        <tr>
                                            <td class="ps-4 fw-medium text-danger"><?= date('d M Y', strtotime($inst['due_date'])) ?></td>
                                            <td><?= $inst['product_name'] ?></td>
                                            <td class="fw-bold"><?= Helper::formatRupiah($inst['amount']) ?></td>
                                            <td><span class="badge-status pending">Belum Dibayar</span></td>
                                        </tr>
                                        <?php endif; endforeach; ?>
                                        <?php if($count == 0): ?>
                                            <tr>
                                                <td colspan="4" class="text-center py-4 text-muted">Semua tagihan bulan ini sudah dilunasi.</td>
                                            </tr>
                                        <?php endif; ?>
                                    <?php endif; ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <?php if($count > 0): ?>
                    <div class="card-footer bg-white border-top p-3 text-center">
                        <a href="<?= BASE_URL ?>/member-dashboard/installments" class="text-decoration-none text-primary fw-medium">Lihat Semua Riwayat</a>
                    </div>
                    <?php endif; ?>
                </div>
                
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
