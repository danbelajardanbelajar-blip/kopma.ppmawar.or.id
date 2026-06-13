<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <h4 class="fw-bold mb-0">Profil Saya</h4>
                    </div>
                    <div class="card-body p-4 p-md-5">
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/member-dashboard/updateProfile" method="POST">
                            <div class="row g-4 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label text-muted">Nomor Anggota</label>
                                    <input type="text" class="form-control form-control-lg bg-light" value="<?= $member['member_code'] ?>" readonly>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label text-muted">Status</label>
                                    <input type="text" class="form-control form-control-lg bg-light text-success fw-bold" value="<?= ucfirst($member['status']) ?>" readonly>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nama Lengkap</label>
                                    <input type="text" name="name" class="form-control form-control-lg" value="<?= $member['name'] ?>" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Email</label>
                                    <input type="email" name="email" class="form-control form-control-lg" value="<?= $member['email'] ?>" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">NIK</label>
                                    <input type="text" name="nik" class="form-control form-control-lg" value="<?= $member['nik'] ?>" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nomor HP / WhatsApp</label>
                                    <input type="text" name="phone" class="form-control form-control-lg" value="<?= $member['phone'] ?>" required>
                                </div>
                                <div class="col-12">
                                    <label class="form-label fw-medium">Alamat Lengkap</label>
                                    <textarea name="address" class="form-control" rows="3" required><?= $member['address'] ?></textarea>
                                </div>
                            </div>
                            
                            <hr class="my-4 text-muted">
                            <h5 class="fw-bold mb-3">Ubah Password (Opsional)</h5>
                            <p class="text-muted small mb-4">Kosongkan jika tidak ingin mengubah password.</p>
                            
                            <div class="row g-4 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Password Baru</label>
                                    <input type="password" name="new_password" class="form-control form-control-lg">
                                </div>
                            </div>
                            
                            <div class="d-flex justify-content-end">
                                <button type="submit" class="btn btn-primary px-5 py-2 rounded-pill">Simpan Perubahan</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
