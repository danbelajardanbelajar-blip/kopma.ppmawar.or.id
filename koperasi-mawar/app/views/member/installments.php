<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <h4 class="fw-bold mb-0">Riwayat Angsuran</h4>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-hover align-middle mb-0">
                                <thead class="table-light">
                                    <tr>
                                        <th class="ps-4">Tenggat Waktu</th>
                                        <th>Produk</th>
                                        <th>Tagihan</th>
                                        <th>Terbayar</th>
                                        <th>Tanggal Bayar</th>
                                        <th class="text-end pe-4">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($installments)): ?>
                                    <tr>
                                        <td colspan="6" class="text-center py-5 text-muted">Belum ada jadwal angsuran.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php foreach($installments as $i): ?>
                                        <tr>
                                            <td class="ps-4 fw-medium"><?= date('d M Y', strtotime($i['due_date'])) ?></td>
                                            <td><span class="text-muted small"><?= $i['product_name'] ?></span></td>
                                            <td class="fw-bold"><?= Helper::formatRupiah($i['amount']) ?></td>
                                            <td class="<?= $i['paid_amount'] > 0 ? 'text-success fw-bold' : 'text-muted' ?>">
                                                <?= Helper::formatRupiah($i['paid_amount']) ?>
                                            </td>
                                            <td class="text-muted small">
                                                <?= $i['paid_date'] ? date('d/m/Y', strtotime($i['paid_date'])) : '-' ?>
                                            </td>
                                            <td class="text-end pe-4">
                                                <?php if($i['status'] == 'paid'): ?>
                                                    <span class="badge bg-success rounded-pill px-3 py-2">Lunas</span>
                                                <?php elseif($i['status'] == 'late'): ?>
                                                    <span class="badge bg-danger rounded-pill px-3 py-2">Terlambat</span>
                                                <?php else: ?>
                                                    <span class="badge bg-warning text-dark rounded-pill px-3 py-2">Pending</span>
                                                <?php endif; ?>
                                            </td>
                                        </tr>
                                        <?php endforeach; ?>
                                    <?php endif; ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
