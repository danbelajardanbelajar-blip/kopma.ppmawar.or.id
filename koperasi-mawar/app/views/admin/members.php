<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Data Anggota</h3>
    <form action="<?= BASE_URL ?>/admin-member" method="GET" class="d-flex gap-2">
        <input type="text" name="search" class="form-control form-control-sm" placeholder="Cari nama/kode..." value="<?= $_GET['search'] ?? '' ?>">
        <button type="submit" class="btn btn-sm btn-primary"><i class="fa-solid fa-search"></i></button>
    </form>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">No. Anggota</th>
                        <th>Nama Lengkap</th>
                        <th>Email / HP</th>
                        <th>Tanggal Gabung</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($members)): ?>
                    <tr><td colspan="6" class="text-center py-4">Data tidak ditemukan</td></tr>
                    <?php else: ?>
                        <?php foreach($members as $m): ?>
                        <tr>
                            <td class="ps-4 fw-medium"><?= $m['member_code'] ?></td>
                            <td>
                                <?= $m['name'] ?><br>
                                <small class="text-muted">NIK: <?= $m['nik'] ?></small>
                            </td>
                            <td>
                                <?= $m['email'] ?><br>
                                <small class="text-muted"><?= $m['phone'] ?></small>
                            </td>
                            <td><?= date('d/m/Y', strtotime($m['join_date'])) ?></td>
                            <td>
                                <?php if($m['status'] == 'active'): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php elseif($m['status'] == 'pending'): ?>
                                    <span class="badge bg-warning text-dark">Pending</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-member/show/<?= $m['id'] ?>" class="btn btn-sm btn-info text-white" title="Detail"><i class="fa-solid fa-eye"></i></a>
                                <a href="#" class="btn btn-sm btn-primary" title="Edit"><i class="fa-solid fa-edit"></i></a>
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
