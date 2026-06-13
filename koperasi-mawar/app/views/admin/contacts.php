<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Pesan Masuk</h3>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Tanggal</th>
                        <th>Pengirim</th>
                        <th>Subjek</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($messages)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada pesan masuk</td></tr>
                    <?php else: ?>
                        <?php foreach($messages as $msg): ?>
                        <tr class="<?= !$msg['is_read'] ? 'fw-bold bg-light' : '' ?>">
                            <td class="ps-4"><?= date('d/m/Y H:i', strtotime($msg['created_at'])) ?></td>
                            <td>
                                <?= $msg['name'] ?><br>
                                <small class="text-muted fw-normal"><?= $msg['email'] ?></small>
                            </td>
                            <td><?= $msg['subject'] ?></td>
                            <td>
                                <?php if($msg['is_read']): ?>
                                    <span class="badge bg-secondary">Dibaca</span>
                                <?php else: ?>
                                    <span class="badge bg-primary">Baru</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-contact/show/<?= $msg['id'] ?>" class="btn btn-sm btn-info text-white"><i class="fa-solid fa-eye"></i></a>
                                <form action="<?= BASE_URL ?>/admin-contact/delete/<?= $msg['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Hapus pesan ini?')"><i class="fa-solid fa-trash"></i></button>
                                </form>
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
