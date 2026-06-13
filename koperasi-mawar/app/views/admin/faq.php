<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola FAQ</h3>
    <a href="#" class="btn btn-primary"><i class="fa-solid fa-plus me-2"></i>Tambah FAQ</a>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Pertanyaan</th>
                        <th>Kategori</th>
                        <th>Urutan</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($faqs)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada FAQ</td></tr>
                    <?php else: ?>
                        <?php foreach($faqs as $f): ?>
                        <tr>
                            <td class="ps-4 fw-medium" style="max-width: 300px;">
                                <div class="text-truncate"><?= $f['question'] ?></div>
                            </td>
                            <td><span class="badge bg-secondary"><?= $f['category'] ?></span></td>
                            <td><?= $f['sort_order'] ?></td>
                            <td>
                                <?php if($f['is_active']): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="#" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                                <form action="#" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Hapus FAQ ini?')"><i class="fa-solid fa-trash"></i></button>
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
