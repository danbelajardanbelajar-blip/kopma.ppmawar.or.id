<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px); display: flex; align-items: center;">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card-modern border-0 overflow-hidden fade-in-section">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <img src="<?= BASE_URL ?>/assets/img/favicon.png" alt="Logo" class="rounded-circle shadow-sm mb-2" style="width: 64px; height: 64px; object-fit: cover;">
                            <h3 class="fw-bold mt-3 text-primary-dark">Login Anggota</h3>
                            <p class="text-muted">Silakan masuk ke dashboard Anda</p>
                        </div>
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/auth/authenticate" method="POST" class="form-modern">
                            <div class="mb-3">
                                <label class="form-label fw-medium">Email</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light"><i class="fa-solid fa-envelope text-muted"></i></span>
                                    <input type="email" name="email" class="form-control" required placeholder="Email terdaftar">
                                </div>
                            </div>
                            <div class="mb-4">
                                <label class="form-label fw-medium">Password</label>
                                <div class="input-group">
                                    <span class="input-group-text bg-light"><i class="fa-solid fa-lock text-muted"></i></span>
                                    <input type="password" name="password" class="form-control" required placeholder="********">
                                </div>
                            </div>
                            <div class="d-grid mb-4">
                                <button type="submit" class="btn btn-primary btn-modern btn-lg w-100">Masuk</button>
                            </div>
                            <div class="text-center">
                                <p class="text-muted mb-0">Belum menjadi anggota? <a href="<?= BASE_URL ?>/membership/register" class="text-secondary fw-bold text-decoration-none">Daftar sekarang</a></p>
                            </div>
                        </form>
                    </div>
                </div>
                
                <div class="text-center mt-4">
                    <a href="<?= BASE_URL ?>/auth/adminLogin" class="text-muted small text-decoration-none"><i class="fa-solid fa-shield-halved me-1"></i> Login sebagai Admin</a>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
