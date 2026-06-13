<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Produk Pembiayaan</h3>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#addModal"><i class="fa-solid fa-plus me-2"></i>Tambah Produk</button>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Nama Produk</th>
                        <th>Akad</th>
                        <th>Margin/Thn</th>
                        <th>Maks. Plafon</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($products)): ?>
                    <tr><td colspan="6" class="text-center py-4">Data tidak ditemukan</td></tr>
                    <?php else: ?>
                        <?php foreach($products as $p): ?>
                        <tr>
                            <td class="ps-4 fw-medium"><?= $p['name'] ?></td>
                            <td><span class="badge bg-secondary"><?= $p['akad'] ?></span></td>
                            <td><?= $p['margin_rate'] ?>%</td>
                            <td><?= Helper::formatRupiah($p['max_amount']) ?></td>
                            <td>
                                <?php if($p['is_active']): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <button type="button" class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#editModal<?= $p['id'] ?>"><i class="fa-solid fa-edit"></i></button>

                                <!-- Edit Modal -->
                                <div class="modal fade text-start" id="editModal<?= $p['id'] ?>" tabindex="-1">
                                    <div class="modal-dialog">
                                        <form action="<?= BASE_URL ?>/admin-financing-product/update/<?= $p['id'] ?>" method="POST" class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title">Edit Produk Pembiayaan</h5>
                                                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                                            </div>
                                            <div class="modal-body">
                                                <div class="mb-3">
                                                    <label class="form-label">Nama Produk</label>
                                                    <input type="text" name="name" class="form-control" value="<?= $p['name'] ?>" required>
                                                </div>
                                                <div class="row mb-3">
                                                    <div class="col-6">
                                                        <label class="form-label">Jenis</label>
                                                        <input type="text" name="type" class="form-control" value="<?= $p['type'] ?>" required>
                                                    </div>
                                                    <div class="col-6">
                                                        <label class="form-label">Akad</label>
                                                        <input type="text" name="akad" class="form-control" value="<?= $p['akad'] ?>" required>
                                                    </div>
                                                </div>
                                                <div class="row mb-3">
                                                    <div class="col-6">
                                                        <label class="form-label">Min. Plafon</label>
                                                        <input type="number" name="min_amount" class="form-control" value="<?= $p['min_amount'] ?>" required>
                                                    </div>
                                                    <div class="col-6">
                                                        <label class="form-label">Maks. Plafon</label>
                                                        <input type="number" name="max_amount" class="form-control" value="<?= $p['max_amount'] ?>" required>
                                                    </div>
                                                </div>
                                                <div class="row mb-3">
                                                    <div class="col-6">
                                                        <label class="form-label">Margin (%) / Thn</label>
                                                        <input type="number" step="0.01" name="margin_rate" class="form-control" value="<?= $p['margin_rate'] ?>" required>
                                                    </div>
                                                    <div class="col-6">
                                                        <label class="form-label">Maks. Tenor (Bulan)</label>
                                                        <input type="number" name="max_tenor" class="form-control" value="<?= $p['max_tenor'] ?>" required>
                                                    </div>
                                                </div>
                                                <div class="mb-3">
                                                    <label class="form-label">Deskripsi</label>
                                                    <textarea name="description" class="form-control" rows="2" required><?= $p['description'] ?></textarea>
                                                </div>
                                                <div class="mb-3">
                                                    <label class="form-label">Syarat & Ketentuan</label>
                                                    <textarea name="terms" class="form-control" rows="2" required><?= $p['terms'] ?></textarea>
                                                </div>
                                                <div class="form-check form-switch">
                                                    <input class="form-check-input" type="checkbox" name="is_active" value="1" <?= $p['is_active'] ? 'checked' : '' ?>>
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
        <form action="<?= BASE_URL ?>/admin-financing-product/store" method="POST" class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Tambah Produk Pembiayaan</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <div class="mb-3">
                    <label class="form-label">Nama Produk</label>
                    <input type="text" name="name" class="form-control" required>
                </div>
                <div class="row mb-3">
                    <div class="col-6">
                        <label class="form-label">Jenis</label>
                        <input type="text" name="type" class="form-control" required>
                    </div>
                    <div class="col-6">
                        <label class="form-label">Akad</label>
                        <input type="text" name="akad" class="form-control" required>
                    </div>
                </div>
                <div class="row mb-3">
                    <div class="col-6">
                        <label class="form-label">Min. Plafon</label>
                        <input type="number" name="min_amount" class="form-control" required>
                    </div>
                    <div class="col-6">
                        <label class="form-label">Maks. Plafon</label>
                        <input type="number" name="max_amount" class="form-control" required>
                    </div>
                </div>
                <div class="row mb-3">
                    <div class="col-6">
                        <label class="form-label">Margin (%) / Thn</label>
                        <input type="number" step="0.01" name="margin_rate" class="form-control" required>
                    </div>
                    <div class="col-6">
                        <label class="form-label">Maks. Tenor (Bulan)</label>
                        <input type="number" name="max_tenor" class="form-control" required>
                    </div>
                </div>
                <div class="mb-3">
                    <label class="form-label">Deskripsi</label>
                    <textarea name="description" class="form-control" rows="2" required></textarea>
                </div>
                <div class="mb-3">
                    <label class="form-label">Syarat & Ketentuan</label>
                    <textarea name="terms" class="form-control" rows="2" required></textarea>
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
