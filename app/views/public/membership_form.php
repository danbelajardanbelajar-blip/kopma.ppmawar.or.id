<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header pb-5">
    <div class="container">
        <h1 class="display-5 fw-bold">Daftar Anggota</h1>
        <p class="lead opacity-75">Bergabung dan jadilah bagian dari Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5" style="margin-top: -60px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card-modern border-0 overflow-hidden fade-in-section">
                    <div class="card-body p-4 p-md-5">
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/membership/store" method="POST" class="form-modern">
                            <h4 class="fw-bold mb-4 border-bottom pb-2">Informasi Pribadi</h4>
                            
                            <div class="row g-3 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nama Lengkap (Sesuai KTP)</label>
                                    <input type="text" name="name" class="form-control" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">NIK (16 Digit)</label>
                                    <input type="text" name="nik" class="form-control" pattern="[0-9]{16}" required>
                                </div>
                                <div class="col-12">
                                    <label class="form-label fw-medium">Alamat Lengkap</label>
                                    <textarea name="address" class="form-control" rows="3" required></textarea>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Nomor WhatsApp/HP</label>
                                    <input type="text" name="phone" class="form-control" required>
                                </div>
                            </div>
                            
                            <h4 class="fw-bold mb-4 border-bottom pb-2 mt-5">Informasi Akun Login</h4>
                            
                            <div class="row g-3 mb-4">
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Alamat Email</label>
                                    <input type="email" name="email" class="form-control" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="form-label fw-medium">Password</label>
                                    <input type="password" name="password" class="form-control" minlength="6" required>
                                </div>
                            </div>
                            
                            <div class="form-check mt-4 mb-4">
                                <input class="form-check-input" type="checkbox" id="terms" required>
                                <label class="form-check-label text-muted" for="terms">
                                    Saya telah membaca, memahami, dan menyetujui <a href="<?= BASE_URL ?>/membership">Syarat dan Ketentuan Keanggotaan</a> serta Anggaran Dasar Koperasi Syariah Mawar.
                                </label>
                            </div>
                            
                            <div class="d-grid">
                                <button type="submit" class="btn btn-primary btn-modern btn-lg w-100">Ajukan Pendaftaran</button>
                            </div>
                            
                            <div class="text-center mt-4">
                                <p class="text-muted">Sudah mendaftar dan disetujui? <a href="<?= BASE_URL ?>/auth/login" class="text-primary fw-bold text-decoration-none">Login di sini</a></p>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
