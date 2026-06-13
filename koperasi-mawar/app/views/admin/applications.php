<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Pengajuan Pembiayaan</h3>
    <div class="btn-group">
        <a href="<?= BASE_URL ?>/admin-application" class="btn btn-sm btn-outline-primary <?= empty($_GET['status']) ? 'active' : '' ?>">Semua</a>
        <a href="<?= BASE_URL ?>/admin-application?status=pending" class="btn btn-sm btn-outline-warning <?= ($_GET['status']??'') == 'pending' ? 'active' : '' ?>">Pending</a>
        <a href="<?= BASE_URL ?>/admin-application?status=approved" class="btn btn-sm btn-outline-success <?= ($_GET['status']??'') == 'approved' ? 'active' : '' ?>">Disetujui</a>
        <a href="<?= BASE_URL ?>/admin-application?status=rejected" class="btn btn-sm btn-outline-danger <?= ($_GET['status']??'') == 'rejected' ? 'active' : '' ?>">Ditolak</a>
    </div>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Tanggal</th>
                        <th>Nama Anggota</th>
                        <th>Produk</th>
                        <th>Plafon & Tenor</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($applications)): ?>
                    <tr><td colspan="6" class="text-center py-4">Data tidak ditemukan</td></tr>
                    <?php else: ?>
                        <?php foreach($applications as $app): ?>
                        <tr>
                            <td class="ps-4"><?= date('d/m/Y H:i', strtotime($app['created_at'])) ?></td>
                            <td><?= $app['member_name'] ?><br><small class="text-muted"><?= $app['member_code'] ?></small></td>
                            <td class="fw-medium"><?= $app['product_name'] ?></td>
                            <td>
                                <?= Helper::formatRupiah($app['amount']) ?><br>
                                <small class="text-muted"><?= $app['tenor'] ?> Bulan</small>
                            </td>
                            <td>
                                <?php if($app['status'] == 'pending'): ?>
                                    <span class="badge bg-warning text-dark">Pending</span>
                                <?php elseif($app['status'] == 'approved'): ?>
                                    <span class="badge bg-success">Disetujui</span>
                                <?php elseif($app['status'] == 'rejected'): ?>
                                    <span class="badge bg-danger">Ditolak</span>
                                <?php else: ?>
                                    <span class="badge bg-secondary">Dibatalkan</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <?php if($app['status'] == 'pending'): ?>
                                    <form action="<?= BASE_URL ?>/admin-application/approve/<?= $app['id'] ?>" method="POST" class="d-inline">
                                        <button class="btn btn-sm btn-success" onclick="return confirm('Setujui pengajuan ini?')"><i class="fa-solid fa-check"></i></button>
                                    </form>
                                    <form action="<?= BASE_URL ?>/admin-application/reject/<?= $app['id'] ?>" method="POST" class="d-inline">
                                        <button class="btn btn-sm btn-danger" onclick="return confirm('Tolak pengajuan ini?')"><i class="fa-solid fa-xmark"></i></button>
                                    </form>
                                <?php endif; ?>
                                <a href="<?= BASE_URL ?>/admin-application/show/<?= $app['id'] ?>" class="btn btn-sm btn-info text-white"><i class="fa-solid fa-eye"></i></a>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
