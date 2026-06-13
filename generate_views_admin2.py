import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

views = {
    r"app\views\admin\profile.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

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
""",

    r"app\views\admin\saving_products.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Produk Simpanan</h3>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Nama Produk</th>
                        <th>Jenis</th>
                        <th>Min. Setoran</th>
                        <th>Bagi Hasil/Margin</th>
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
                            <td><span class="badge bg-secondary"><?= $p['type'] ?></span></td>
                            <td><?= Helper::formatRupiah($p['min_amount']) ?></td>
                            <td><?= $p['margin_rate'] ?>%</td>
                            <td>
                                <?php if($p['is_active']): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="#" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
""",

    r"app\views\admin\financing_products.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Produk Pembiayaan</h3>
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
                                <a href="#" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
""",

    r"app\views\admin\members.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Data Anggota</h3>
    <form action="<?= BASE_URL ?>/admin-member" method="GET" class="d-flex gap-2">
        <input type="text" name="search" class="form-control form-control-sm" placeholder="Cari nama/kode..." value="<?= $_GET['search'] ?? '' ?>">
        <button type="submit" class="btn btn-sm btn-primary"><i class="fa-solid fa-search"></i></button>
    </form>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">No. Anggota</th>
                        <th>Nama Lengkap</th>
                        <th>Email / HP</th>
                        <th>Tanggal Gabung</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($members)): ?>
                    <tr><td colspan="6" class="text-center py-4">Data tidak ditemukan</td></tr>
                    <?php else: ?>
                        <?php foreach($members as $m): ?>
                        <tr>
                            <td class="ps-4 fw-medium"><?= $m['member_code'] ?></td>
                            <td>
                                <?= $m['name'] ?><br>
                                <small class="text-muted">NIK: <?= $m['nik'] ?></small>
                            </td>
                            <td>
                                <?= $m['email'] ?><br>
                                <small class="text-muted"><?= $m['phone'] ?></small>
                            </td>
                            <td><?= date('d/m/Y', strtotime($m['join_date'])) ?></td>
                            <td>
                                <?php if($m['status'] == 'active'): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php elseif($m['status'] == 'pending'): ?>
                                    <span class="badge bg-warning text-dark">Pending</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-member/show/<?= $m['id'] ?>" class="btn btn-sm btn-info text-white" title="Detail"><i class="fa-solid fa-eye"></i></a>
                                <a href="#" class="btn btn-sm btn-primary" title="Edit"><i class="fa-solid fa-edit"></i></a>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
""",

    r"app\views\admin\applications.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Pengajuan Pembiayaan</h3>
    <div class="btn-group">
        <a href="<?= BASE_URL ?>/admin-application" class="btn btn-sm btn-outline-primary <?= empty($_GET['status']) ? 'active' : '' ?>">Semua</a>
        <a href="<?= BASE_URL ?>/admin-application?status=pending" class="btn btn-sm btn-outline-warning <?= ($_GET['status']??'') == 'pending' ? 'active' : '' ?>">Pending</a>
        <a href="<?= BASE_URL ?>/admin-application?status=approved" class="btn btn-sm btn-outline-success <?= ($_GET['status']??'') == 'approved' ? 'active' : '' ?>">Disetujui</a>
        <a href="<?= BASE_URL ?>/admin-application?status=rejected" class="btn btn-sm btn-outline-danger <?= ($_GET['status']??'') == 'rejected' ? 'active' : '' ?>">Ditolak</a>
    </div>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Tanggal</th>
                        <th>Nama Anggota</th>
                        <th>Produk</th>
                        <th>Plafon & Tenor</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($applications)): ?>
                    <tr><td colspan="6" class="text-center py-4">Data tidak ditemukan</td></tr>
                    <?php else: ?>
                        <?php foreach($applications as $app): ?>
                        <tr>
                            <td class="ps-4"><?= date('d/m/Y H:i', strtotime($app['created_at'])) ?></td>
                            <td><?= $app['member_name'] ?><br><small class="text-muted"><?= $app['member_code'] ?></small></td>
                            <td class="fw-medium"><?= $app['product_name'] ?></td>
                            <td>
                                <?= Helper::formatRupiah($app['amount']) ?><br>
                                <small class="text-muted"><?= $app['tenor'] ?> Bulan</small>
                            </td>
                            <td>
                                <?php if($app['status'] == 'pending'): ?>
                                    <span class="badge bg-warning text-dark">Pending</span>
                                <?php elseif($app['status'] == 'approved'): ?>
                                    <span class="badge bg-success">Disetujui</span>
                                <?php elseif($app['status'] == 'rejected'): ?>
                                    <span class="badge bg-danger">Ditolak</span>
                                <?php else: ?>
                                    <span class="badge bg-secondary">Dibatalkan</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <?php if($app['status'] == 'pending'): ?>
                                    <form action="<?= BASE_URL ?>/admin-application/approve/<?= $app['id'] ?>" method="POST" class="d-inline">
                                        <button class="btn btn-sm btn-success" onclick="return confirm('Setujui pengajuan ini?')"><i class="fa-solid fa-check"></i></button>
                                    </form>
                                    <form action="<?= BASE_URL ?>/admin-application/reject/<?= $app['id'] ?>" method="POST" class="d-inline">
                                        <button class="btn btn-sm btn-danger" onclick="return confirm('Tolak pengajuan ini?')"><i class="fa-solid fa-xmark"></i></button>
                                    </form>
                                <?php endif; ?>
                                <a href="<?= BASE_URL ?>/admin-application/show/<?= $app['id'] ?>" class="btn btn-sm btn-info text-white"><i class="fa-solid fa-eye"></i></a>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
""",

    r"app\views\admin\news.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola Berita</h3>
    <a href="<?= BASE_URL ?>/admin-news/create" class="btn btn-primary"><i class="fa-solid fa-plus me-2"></i>Tambah Berita</a>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Judul</th>
                        <th>Kategori</th>
                        <th>Tanggal</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($news)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada berita</td></tr>
                    <?php else: ?>
                        <?php foreach($news as $n): ?>
                        <tr>
                            <td class="ps-4 fw-medium" style="max-width: 300px;">
                                <div class="text-truncate"><?= $n['title'] ?></div>
                            </td>
                            <td><span class="badge bg-secondary"><?= $n['category'] ?></span></td>
                            <td><?= date('d M Y', strtotime($n['created_at'])) ?></td>
                            <td>
                                <?php if($n['is_published']): ?>
                                    <span class="badge bg-success">Published</span>
                                <?php else: ?>
                                    <span class="badge bg-warning text-dark">Draft</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-news/edit/<?= $n['id'] ?>" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                                <form action="<?= BASE_URL ?>/admin-news/delete/<?= $n['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Yakin ingin menghapus berita ini?')"><i class="fa-solid fa-trash"></i></button>
                                </form>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</div>

<?php include APP_ROOT . '/app/views/layouts/admin_footer.php'; ?>
""",

    r"app\views\admin\contacts.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Pesan Masuk</h3>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Tanggal</th>
                        <th>Pengirim</th>
                        <th>Subjek</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($messages)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada pesan masuk</td></tr>
                    <?php else: ?>
                        <?php foreach($messages as $msg): ?>
                        <tr class="<?= !$msg['is_read'] ? 'fw-bold bg-light' : '' ?>">
                            <td class="ps-4"><?= date('d/m/Y H:i', strtotime($msg['created_at'])) ?></td>
                            <td>
                                <?= $msg['name'] ?><br>
                                <small class="text-muted fw-normal"><?= $msg['email'] ?></small>
                            </td>
                            <td><?= $msg['subject'] ?></td>
                            <td>
                                <?php if($msg['is_read']): ?>
                                    <span class="badge bg-secondary">Dibaca</span>
                                <?php else: ?>
                                    <span class="badge bg-primary">Baru</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="<?= BASE_URL ?>/admin-contact/show/<?= $msg['id'] ?>" class="btn btn-sm btn-info text-white"><i class="fa-solid fa-eye"></i></a>
                                <form action="<?= BASE_URL ?>/admin-contact/delete/<?= $msg['id'] ?>" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Hapus pesan ini?')"><i class="fa-solid fa-trash"></i></button>
                                </form>
                            </td>
                        </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
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

print("Admin Views 2 created successfully.")
