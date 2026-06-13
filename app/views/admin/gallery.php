<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola Galeri</h3>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addModal"><i class="fa-solid fa-plus me-2"></i>Tambah Foto</button>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-4">
        <div class="row g-4">
            <?php if(empty($galleries)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada foto dalam galeri.</h4>
                </div>
            <?php else: ?>
                <?php foreach($galleries as $g): ?>
                <div class="col-md-4 col-lg-3">
                    <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
                        <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $g['image'] ?>" class="card-img-top" alt="<?= $g['title'] ?>" style="height: 150px; object-fit: cover;">
                        <div class="card-body p-3">
                            <h6 class="fw-bold mb-1 text-truncate"><?= $g['title'] ?></h6>
                            <span class="badge bg-secondary mb-2"><?= $g['category'] ?></span>
                            <div class="d-flex justify-content-end mt-2">
                                <form action="<?= BASE_URL ?>/admin-gallery/delete/<?= $g['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-outline-danger" onclick="return confirm('Hapus foto ini?')"><i class="fa-solid fa-trash"></i> Hapus</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
</div>

<!-- Add Modal -->
<div class="modal fade" id="addModal" tabindex="-1">
    <div class="modal-dialog">
        <form action="<?= BASE_URL ?>/admin-gallery/store" method="POST" enctype="multipart/form-data" class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Tambah Foto</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label class="form-label">Judul Foto</label>
                    <input type="text" name="title" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Kategori</label>
                    <select name="category" class="form-select" required>
                        <option value="foto">Foto</option>
                        <option value="dokumentasi">Dokumentasi</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label class="form-label">Upload Gambar</label>
                    <input type="file" name="image" class="form-control" accept="image/*" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Deskripsi</label>
                    <textarea name="description" class="form-control" rows="2"></textarea>
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
