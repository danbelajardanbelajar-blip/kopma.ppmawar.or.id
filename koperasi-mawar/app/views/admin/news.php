<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola Berita</h3>
    <a href="<?= BASE_URL ?>/admin-news/create" class="btn btn-primary"><i class="fa-solid fa-plus me-2"></i>Tambah Berita</a>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Judul</th>
                        <th>Kategori</th>
                        <th>Tanggal</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($news)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada berita</td></tr>
                    <?php else: ?>
                        <?php foreach($news as $n): ?>
                        <tr>
                            <td class="ps-4 fw-medium" style="max-width: 300px;">
                                <div class="text-truncate"><?= $n['title'] ?></div>
                            </td>
                            <td><span class="badge bg-secondary"><?= $n['category'] ?></span></td>
                            <td><?= date('d M Y', strtotime($n['created_at'])) ?></td>
                            <td>
                                <?php if($n['is_published']): ?>
                                    <span class="badge bg-success">Published</span>
                                <?php else: ?>
                                    <span class="badge bg-warning text-dark">Draft</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-news/edit/<?= $n['id'] ?>" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                                <form action="<?= BASE_URL ?>/admin-news/delete/<?= $n['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Yakin ingin menghapus berita ini?')"><i class="fa-solid fa-trash"></i></button>
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
