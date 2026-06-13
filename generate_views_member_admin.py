import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

views = {
    r"app\views\member\profile.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
""",

    r"app\views\member\savings.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <h4 class="fw-bold mb-0">Riwayat Simpanan Saya</h4>
                    </div>
                    <div class="card-body p-4">
                        
                        <div class="table-responsive">
                            <table class="table table-hover align-middle border">
                                <thead class="table-light">
                                    <tr>
                                        <th class="ps-4">Tanggal Daftar</th>
                                        <th>Produk Simpanan</th>
                                        <th>Jenis</th>
                                        <th class="text-end pe-4">Saldo Saat Ini</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($savings)): ?>
                                    <tr>
                                        <td colspan="4" class="text-center py-5 text-muted">Belum ada data simpanan.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php 
                                        $total = 0;
                                        foreach($savings as $s): 
                                            $total += $s['balance'];
                                        ?>
                                        <tr>
                                            <td class="ps-4 text-muted"><?= date('d M Y', strtotime($s['created_at'])) ?></td>
                                            <td class="fw-medium"><?= $s['product_name'] ?></td>
                                            <td><span class="badge bg-secondary"><?= $s['type'] ?></span></td>
                                            <td class="text-end pe-4 fw-bold text-success"><?= Helper::formatRupiah($s['balance']) ?></td>
                                        </tr>
                                        <?php endforeach; ?>
                                        <tr class="table-light">
                                            <td colspan="3" class="text-end fw-bold">TOTAL SALDO SIMPANAN</td>
                                            <td class="text-end pe-4 fw-bold fs-5 text-primary"><?= Helper::formatRupiah($total) ?></td>
                                        </tr>
                                    <?php endif; ?>
                                </tbody>
                            </table>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\member\financing.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="d-flex justify-content-between align-items-center mb-4">
                    <h4 class="fw-bold mb-0">Pembiayaan Saya</h4>
                    <a href="<?= BASE_URL ?>/member-dashboard/applyFinancing" class="btn btn-primary rounded-pill"><i class="fa-solid fa-plus me-2"></i>Ajukan Baru</a>
                </div>
                
                <?php if($flash = Flash::get()): ?>
                <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                    <?= $flash['message'] ?>
                </div>
                <?php endif; ?>

                <?php if(empty($financings)): ?>
                <div class="card shadow-sm border-0 rounded-4 p-5 text-center">
                    <i class="fa-solid fa-file-invoice-dollar text-muted opacity-50 mb-3" style="font-size: 4rem;"></i>
                    <h5 class="text-muted">Anda belum memiliki riwayat pembiayaan.</h5>
                </div>
                <?php else: ?>
                    <div class="row g-4">
                        <?php foreach($financings as $f): ?>
                        <div class="col-md-6">
                            <div class="card shadow-sm border-0 rounded-4 h-100">
                                <div class="card-header bg-white border-bottom p-3 d-flex justify-content-between align-items-center">
                                    <span class="badge bg-secondary"><?= $f['akad'] ?></span>
                                    <span class="badge <?= $f['status'] == 'active' ? 'bg-success' : 'bg-secondary' ?>"><?= ucfirst($f['status']) ?></span>
                                </div>
                                <div class="card-body p-4">
                                    <h5 class="fw-bold mb-1"><?= $f['product_name'] ?></h5>
                                    <p class="text-muted small mb-4">Mulai: <?= date('d/m/Y', strtotime($f['start_date'])) ?> &mdash; Selesai: <?= date('d/m/Y', strtotime($f['end_date'])) ?></p>
                                    
                                    <div class="d-flex justify-content-between mb-2 pb-2 border-bottom">
                                        <span class="text-muted">Pokok</span>
                                        <span class="fw-bold"><?= Helper::formatRupiah($f['amount']) ?></span>
                                    </div>
                                    <div class="d-flex justify-content-between mb-2 pb-2 border-bottom">
                                        <span class="text-muted">Tenor</span>
                                        <span class="fw-bold"><?= $f['tenor'] ?> Bulan</span>
                                    </div>
                                    <div class="d-flex justify-content-between mt-3">
                                        <span class="text-muted">Angsuran /bln</span>
                                        <h5 class="fw-bold text-danger mb-0"><?= Helper::formatRupiah($f['monthly_payment']) ?></h5>
                                    </div>
                                </div>
                                <div class="card-footer bg-white border-top p-3 text-center">
                                    <a href="<?= BASE_URL ?>/member-dashboard/installments" class="btn btn-outline-primary btn-sm w-100 rounded-pill">Lihat Jadwal Angsuran</a>
                                </div>
                            </div>
                        </div>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\member\apply_financing.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
""",

    r"app\views\member\installments.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <h4 class="fw-bold mb-0">Riwayat Angsuran</h4>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-hover align-middle mb-0">
                                <thead class="table-light">
                                    <tr>
                                        <th class="ps-4">Tenggat Waktu</th>
                                        <th>Produk</th>
                                        <th>Tagihan</th>
                                        <th>Terbayar</th>
                                        <th>Tanggal Bayar</th>
                                        <th class="text-end pe-4">Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($installments)): ?>
                                    <tr>
                                        <td colspan="6" class="text-center py-5 text-muted">Belum ada jadwal angsuran.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php foreach($installments as $i): ?>
                                        <tr>
                                            <td class="ps-4 fw-medium"><?= date('d M Y', strtotime($i['due_date'])) ?></td>
                                            <td><span class="text-muted small"><?= $i['product_name'] ?></span></td>
                                            <td class="fw-bold"><?= Helper::formatRupiah($i['amount']) ?></td>
                                            <td class="<?= $i['paid_amount'] > 0 ? 'text-success fw-bold' : 'text-muted' ?>">
                                                <?= Helper::formatRupiah($i['paid_amount']) ?>
                                            </td>
                                            <td class="text-muted small">
                                                <?= $i['paid_date'] ? date('d/m/Y', strtotime($i['paid_date'])) : '-' ?>
                                            </td>
                                            <td class="text-end pe-4">
                                                <?php if($i['status'] == 'paid'): ?>
                                                    <span class="badge bg-success rounded-pill px-3 py-2">Lunas</span>
                                                <?php elseif($i['status'] == 'late'): ?>
                                                    <span class="badge bg-danger rounded-pill px-3 py-2">Terlambat</span>
                                                <?php else: ?>
                                                    <span class="badge bg-warning text-dark rounded-pill px-3 py-2">Pending</span>
                                                <?php endif; ?>
                                            </td>
                                        </tr>
                                        <?php endforeach; ?>
                                    <?php endif; ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
""",

    r"app\views\admin\login.php": """<!DOCTYPE html>
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
</head>
<body class="d-flex align-items-center justify-content-center vh-100">

    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-5">
                <div class="card login-card border-0 overflow-hidden">
                    <div class="card-body p-5">
                        <div class="text-center mb-4">
                            <i class="fa-solid fa-shield-halved text-warning mb-3" style="font-size: 3rem;"></i>
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
""",

    r"app\views\admin\dashboard.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Dashboard Statistik</h3>
</div>

<div class="row g-4 mb-4">
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-primary-light">
                <i class="fa-solid fa-users"></i>
            </div>
            <div class="stat-details">
                <h3><?= $total_members ?></h3>
                <p>Total Anggota</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-warning-light">
                <i class="fa-solid fa-file-signature"></i>
            </div>
            <div class="stat-details">
                <h3><?= $pending_apps ?></h3>
                <p>Pengajuan Pending</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon bg-info-light">
                <i class="fa-solid fa-envelope"></i>
            </div>
            <div class="stat-details">
                <h3><?= $unread_msgs ?></h3>
                <p>Pesan Baru</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="stat-card">
            <div class="stat-icon" style="background: rgba(40, 167, 69, 0.1); color: #28a745;">
                <i class="fa-solid fa-wallet"></i>
            </div>
            <div class="stat-details">
                <h3>Aktif</h3>
                <p>Status Sistem</p>
            </div>
        </div>
    </div>
</div>

<div class="row g-4">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header d-flex justify-content-between align-items-center">
                <span>Pendaftar Anggota Baru</span>
                <a href="<?= BASE_URL ?>/admin-member" class="btn btn-sm btn-outline-primary">Lihat Semua</a>
            </div>
            <div class="card-body p-0">
                <div class="table-responsive">
                    <table class="table table-hover mb-0">
                        <thead class="table-light">
                            <tr>
                                <th class="ps-4">No. Anggota</th>
                                <th>Nama Lengkap</th>
                                <th>Email</th>
                                <th>Status</th>
                                <th class="text-end pe-4">Aksi</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php if(empty($latest_members)): ?>
                                <tr><td colspan="5" class="text-center py-4">Belum ada anggota</td></tr>
                            <?php else: ?>
                                <?php foreach($latest_members as $m): ?>
                                <tr>
                                    <td class="ps-4"><?= $m['member_code'] ?></td>
                                    <td class="fw-medium"><?= $m['name'] ?></td>
                                    <td><?= $m['email'] ?></td>
                                    <td><span class="badge <?= $m['status'] == 'active' ? 'bg-success' : 'bg-warning' ?>"><?= $m['status'] ?></span></td>
                                    <td class="text-end pe-4">
                                        <a href="<?= BASE_URL ?>/admin-member/show/<?= $m['id'] ?>" class="btn btn-sm btn-light"><i class="fa-solid fa-eye"></i></a>
                                    </td>
                                </tr>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
"""
}

for rel_path, content in views.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Member & Admin Views created successfully.")
