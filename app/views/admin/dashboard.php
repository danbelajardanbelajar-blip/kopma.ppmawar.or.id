<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Dashboard Statistik</h3>
</div>

<div class="row g-4 mb-4">
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-primary-light">
                <i class="fa-solid fa-users"></i>
            </div>
            <div class="stat-details">
                <h3><?= $total_members ?></h3>
                <p>Total Anggota</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-warning-light">
                <i class="fa-solid fa-file-signature"></i>
            </div>
            <div class="stat-details">
                <h3><?= $pending_apps ?></h3>
                <p>Pengajuan Pending</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-info-light">
                <i class="fa-solid fa-envelope"></i>
            </div>
            <div class="stat-details">
                <h3><?= $unread_msgs ?></h3>
                <p>Pesan Baru</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon" style="background: rgba(40, 167, 69, 0.1); color: #28a745;">
                <i class="fa-solid fa-wallet"></i>
            </div>
            <div class="stat-details">
                <h3>Aktif</h3>
                <p>Status Sistem</p>
            </div>
        </div>
    </div>
</div>

<div class="row g-4">
    <div class="col-md-12">
        <div class="card-modern">
            <div class="card-header bg-white border-0 pt-4 pb-0 px-4 d-flex justify-content-between align-items-center">
                <span class="fw-bold">Pendaftar Anggota Baru</span>
                <a href="<?= BASE_URL ?>/admin-member" class="btn btn-sm btn-outline-primary rounded-pill">Lihat Semua</a>
            </div>
            <div class="card-body p-4">
                <div class="table-responsive">
                    <table class="table-modern">
                        <thead>
                            <tr>
                                <th class="ps-4">No. Anggota</th>
                                <th>Nama Lengkap</th>
                                <th>Email</th>
                                <th>Status</th>
                                <th class="text-end pe-4">Aksi</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php if(empty($latest_members)): ?>
                                <tr><td colspan="5" class="text-center py-4">Belum ada anggota</td></tr>
                            <?php else: ?>
                                <?php foreach($latest_members as $m): ?>
                                <tr>
                                    <td class="ps-4"><?= $m['member_code'] ?></td>
                                    <td class="fw-medium"><?= $m['name'] ?></td>
                                    <td><?= $m['email'] ?></td>
                                    <td><span class="badge-status <?= $m['status'] == 'active' ? 'approved' : 'pending' ?>"><?= ucfirst($m['status']) ?></span></td>
                                    <td class="text-end pe-4">
                                        <a href="<?= BASE_URL ?>/admin-member/show/<?= $m['id'] ?>" class="btn btn-sm btn-light"><i class="fa-solid fa-eye"></i></a>
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

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
