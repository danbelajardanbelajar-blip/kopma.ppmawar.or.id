<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Admin - <?= APP_NAME ?></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body { background-color: #0D3D22; font-family: 'Plus Jakarta Sans', sans-serif; }
        .login-card { border-radius: 15px; box-shadow: 0 15px 35px rgba(0,0,0,0.2); }
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
                                <input type="email" name="email" class="form-control form-control-lg bg-light" required>
                            </div>
                            <div class="mb-4">
                                <label class="form-label text-muted fw-medium">Password</label>
                                <input type="password" name="password" class="form-control form-control-lg bg-light" required>
                            </div>
                            <button type="submit" class="btn btn-warning btn-lg w-100 fw-bold">Login Sekarang</button>
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
