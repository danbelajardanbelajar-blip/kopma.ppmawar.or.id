<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Profil Koperasi</h3>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-4">
        <form action="<?= BASE_URL ?>/admin-profile/update" method="POST">
            <div class="row g-4 mb-4">
                <div class="col-md-6">
                    <label class="form-label fw-medium">Nama Koperasi</label>
                    <input type="text" name="koperasi_name" class="form-control" value="<?= $profile['koperasi_name'] ?? '' ?>" required>
                </div>
                <div class="col-md-6">
                    <label class="form-label fw-medium">Tahun Berdiri</label>
                    <input type="number" name="founded_year" class="form-control" value="<?= $profile['founded_year'] ?? '' ?>" required>
                </div>
                <div class="col-12">
                    <label class="form-label fw-medium">Slogan / Tagline</label>
                    <input type="text" name="tagline" class="form-control" value="<?= $profile['tagline'] ?? '' ?>" required>
                </div>
                <div class="col-12">
                    <label class="form-label fw-medium">Deskripsi Singkat</label>
                    <textarea name="description" class="form-control" rows="4" required><?= $profile['description'] ?? '' ?></textarea>
                </div>
                <div class="col-12">
                    <label class="form-label fw-medium">Visi</label>
                    <textarea name="vision" class="form-control" rows="2" required><?= $profile['vision'] ?? '' ?></textarea>
                </div>
                <div class="col-12">
                    <label class="form-label fw-medium">Misi</label>
                    <textarea name="mission" class="form-control" rows="5" required><?= $profile['mission'] ?? '' ?></textarea>
                </div>
            </div>
            
            <div class="d-flex justify-content-end">
                <button type="submit" class="btn btn-primary"><i class="fa-solid fa-save me-2"></i>Simpan Perubahan</button>
            </div>
        </form>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
