<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola FAQ</h3>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addModal"><i class="fa-solid fa-plus me-2"></i>Tambah FAQ</button>
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
                                <button type="button" class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#editModal<?= $f['id'] ?>"><i class="fa-solid fa-edit"></i></button>
                                <form action="<?= BASE_URL ?>/admin-faq/delete/<?= $f['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Hapus FAQ ini?')"><i class="fa-solid fa-trash"></i></button>
                                </form>

                                <!-- Edit Modal -->
                                <div class="modal fade text-start" id="editModal<?= $f['id'] ?>" tabindex="-1">
                                    <div class="modal-dialog">
                                        <form action="<?= BASE_URL ?>/admin-faq/update/<?= $f['id'] ?>" method="POST" class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title">Edit FAQ</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                            </div>
                                            <div class="modal-body">
                                                <div class="mb-3">
                                                    <label class="form-label">Pertanyaan</label>
                                                    <input type="text" name="question" class="form-control" value="<?= $f['question'] ?>" required>
                                                </div>
                                                <div class="mb-3">
                                                    <label class="form-label">Jawaban</label>
                                                    <textarea name="answer" class="form-control" rows="3" required><?= $f['answer'] ?></textarea>
                                                </div>
                                                <div class="mb-3">
                                                    <label class="form-label">Kategori</label>
                                                    <input type="text" name="category" class="form-control" value="<?= $f['category'] ?>" required>
                                                </div>
                                                <div class="mb-3">
                                                    <label class="form-label">Urutan</label>
                                                    <input type="number" name="sort_order" class="form-control" value="<?= $f['sort_order'] ?>" required>
                                                </div>
                                                <div class="form-check form-switch">
                                                    <input class="form-check-input" type="checkbox" name="is_active" value="1" <?= $f['is_active'] ? 'checked' : '' ?>>
                                                    <label class="form-check-label">Aktif</label>
                                                </div>
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
                                                <button type="submit" class="btn btn-primary">Simpan Perubahan</button>
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<!-- Add Modal -->
<div class="modal fade" id="addModal" tabindex="-1">
    <div class="modal-dialog">
        <form action="<?= BASE_URL ?>/admin-faq/store" method="POST" class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Tambah FAQ</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label class="form-label">Pertanyaan</label>
                    <input type="text" name="question" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Jawaban</label>
                    <textarea name="answer" class="form-control" rows="3" required></textarea>
                </div>
                <div class="mb-3">
                    <label class="form-label">Kategori</label>
                    <input type="text" name="category" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Urutan</label>
                    <input type="number" name="sort_order" class="form-control" value="0" required>
                </div>
                <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" name="is_active" value="1" checked>
                    <label class="form-check-label">Aktif</label>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Batal</button>
                <button type="submit" class="btn btn-primary">Simpan</button>
            </div>
        </form>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
