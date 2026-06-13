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
                        <h4 class="fw-bold mb-0">Riwayat Simpanan Saya</h4>
                    </div>
                    <div class="card-body p-4">
                        
                        <div class="table-responsive">
                            <table class="table table-hover align-middle border">
                                <thead class="table-light">
                                    <tr>
                                        <th class="ps-4">Tanggal Daftar</th>
                                        <th>Produk Simpanan</th>
                                        <th>Jenis</th>
                                        <th class="text-end pe-4">Saldo Saat Ini</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($savings)): ?>
                                    <tr>
                                        <td colspan="4" class="text-center py-5 text-muted">Belum ada data simpanan.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php 
                                        $total = 0;
                                        foreach($savings as $s): 
                                            $total += $s['balance'];
                                        ?>
                                        <tr>
                                            <td class="ps-4 text-muted"><?= date('d M Y', strtotime($s['created_at'])) ?></td>
                                            <td class="fw-medium"><?= $s['product_name'] ?></td>
                                            <td><span class="badge bg-secondary"><?= $s['type'] ?></span></td>
                                            <td class="text-end pe-4 fw-bold text-success"><?= Helper::formatRupiah($s['balance']) ?></td>
                                        </tr>
                                        <?php endforeach; ?>
                                        <tr class="table-light">
                                            <td colspan="3" class="text-end fw-bold">TOTAL SALDO SIMPANAN</td>
                                            <td class="text-end pe-4 fw-bold fs-5 text-primary"><?= Helper::formatRupiah($total) ?></td>
                                        </tr>
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
