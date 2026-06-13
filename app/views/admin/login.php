<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Admin - <?= APP_NAME ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background: linear-gradient(135deg, rgba(27,107,58,0.95) 0%, rgba(13,61,34,0.98) 100%), url('../img/images.jpg') center/cover no-repeat; font-family: 'Plus Jakarta Sans', sans-serif; position: relative; }
        body::before { content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(13, 61, 34, 0.85); z-index: -1; }
        .login-card { border-radius: 1.5rem; box-shadow: 0 15px 35px rgba(0,0,0,0.3); background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px); }
        .form-control-modern { border-radius: 0.75rem; padding: 0.75rem 1rem; border: 1px solid #e0e0e0; background-color: #fcfcfc; transition: all 0.3s; }
        .form-control-modern:focus { background-color: #fff; border-color: #1B6B3A; box-shadow: 0 0 0 4px rgba(27, 107, 58, 0.1); }
        .btn-modern { border-radius: 50rem; padding: 0.6rem 1.5rem; font-weight: 600; letter-spacing: 0.5px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    </style>
    <link rel="icon" type="image/png" href="<?= BASE_URL ?>/assets/img/favicon.png">
</head>
<body class="d-flex align-items-center justify-content-center vh-100">

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card login-card border-0 overflow-hidden">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <img src="<?= BASE_URL ?>/assets/img/favicon.png" alt="Logo" class="rounded-circle shadow-sm mb-3" style="width: 64px; height: 64px; object-fit: cover;">
                            <h3 class="fw-bold text-dark">Admin Panel</h3>
                            <p class="text-muted">Masuk untuk mengelola sistem Koperasi</p>
                        </div>
                        
                        <?php if($flash = Flash::get()): ?>
                        <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                            <?= $flash['message'] ?>
                        </div>
                        <?php endif; ?>

                        <form action="<?= BASE_URL ?>/auth/authenticate" method="POST">
                            <div class="mb-3">
                                <label class="form-label text-muted fw-medium">Email Admin</label>
                                <input type="email" name="email" class="form-control form-control-modern" required>
                            </div>
                            <div class="mb-4">
                                <label class="form-label text-muted fw-medium">Password</label>
                                <input type="password" name="password" class="form-control form-control-modern" required>
                            </div>
                            <button type="submit" class="btn btn-warning btn-modern btn-lg w-100 text-dark">Login Sekarang</button>
                        </form>
                        
                        <div class="text-center mt-4">
                            <a href="<?= BASE_URL ?>/" class="text-muted text-decoration-none small"><i class="fa-solid fa-arrow-left me-1"></i> Kembali ke Website</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</body>
</html>
