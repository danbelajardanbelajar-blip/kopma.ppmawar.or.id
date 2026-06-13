<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <div class="d-flex justify-content-between align-items-center">
                            <h4 class="fw-bold mb-0">Ajukan Pembiayaan</h4>
                            <a href="<?= BASE_URL ?>/member-dashboard/financing" class="btn btn-outline-secondary btn-sm rounded-pill">Kembali</a>
                        </div>
                    </div>
                    <div class="card-body p-4 p-md-5">
                        <form action="<?= BASE_URL ?>/member-dashboard/submitApplication" method="POST">
                            <div class="mb-4">
                                <label class="form-label fw-medium">Pilih Produk Pembiayaan</label>
                                <select name="product_id" class="form-select form-select-lg bg-light" required>
                                    <option value="">-- Pilih Produk --</option>
                                    <?php foreach($products as $p): ?>
                                        <option value="<?= $p['id'] ?>"><?= $p['name'] ?> (Maks. <?= Helper::formatRupiah($p['max_amount']) ?>)</option>
                                    <?php endforeach; ?>
                                </select>
                            </div>
                            
                            <div class="row g-4 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Jumlah Pengajuan (Rp)</label>
                                    <input type="text" name="amount" class="form-control form-control-lg bg-light" placeholder="Contoh: 10.000.000" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Tenor (Bulan)</label>
                                    <input type="number" name="tenor" class="form-control form-control-lg bg-light" min="1" max="120" required>
                                </div>
                            </div>
                            
                            <div class="mb-5">
                                <label class="form-label fw-medium">Tujuan Pembiayaan</label>
                                <textarea name="purpose" class="form-control bg-light" rows="3" placeholder="Jelaskan secara singkat tujuan penggunaan dana pembiayaan ini..." required></textarea>
                            </div>
                            
                            <div class="alert alert-warning border-0 bg-warning bg-opacity-10 mb-4">
                                <i class="fa-solid fa-circle-info me-2"></i> Pengajuan akan ditinjau oleh tim survey koperasi. Pastikan data yang dimasukkan benar.
                            </div>
                            
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-lg rounded-pill">Kirim Pengajuan</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
