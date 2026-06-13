import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

views = {
    r"app\views\admin\faq.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola FAQ</h3>
    <a href="#" class="btn btn-primary"><i class="fa-solid fa-plus me-2"></i>Tambah FAQ</a>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-0">
        <div class="table-responsive">
            <table class="table table-hover align-middle mb-0">
                <thead class="table-light">
                    <tr>
                        <th class="ps-4">Pertanyaan</th>
                        <th>Kategori</th>
                        <th>Urutan</th>
                        <th>Status</th>
                        <th class="text-end pe-4">Aksi</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if(empty($faqs)): ?>
                    <tr><td colspan="5" class="text-center py-4">Belum ada FAQ</td></tr>
                    <?php else: ?>
                        <?php foreach($faqs as $f): ?>
                        <tr>
                            <td class="ps-4 fw-medium" style="max-width: 300px;">
                                <div class="text-truncate"><?= $f['question'] ?></div>
                            </td>
                            <td><span class="badge bg-secondary"><?= $f['category'] ?></span></td>
                            <td><?= $f['sort_order'] ?></td>
                            <td>
                                <?php if($f['is_active']): ?>
                                    <span class="badge bg-success">Aktif</span>
                                <?php else: ?>
                                    <span class="badge bg-danger">Nonaktif</span>
                                <?php endif; ?>
                            </td>
                            <td class="text-end pe-4">
                                <a href="#" class="btn btn-sm btn-primary"><i class="fa-solid fa-edit"></i></a>
                                <form action="#" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-danger" onclick="return confirm('Hapus FAQ ini?')"><i class="fa-solid fa-trash"></i></button>
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

    r"app\views\admin\gallery.php": """<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-4">
    <h3 class="fw-bold mb-0">Kelola Galeri</h3>
    <a href="#" class="btn btn-primary"><i class="fa-solid fa-plus me-2"></i>Tambah Foto</a>
</div>

<div class="card shadow-sm border-0">
    <div class="card-body p-4">
        <div class="row g-4">
            <?php if(empty($galleries)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada foto dalam galeri.</h4>
                </div>
            <?php else: ?>
                <?php foreach($galleries as $g): ?>
                <div class="col-md-4 col-lg-3">
                    <div class="card h-100 border-0 shadow-sm rounded-4 overflow-hidden">
                        <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $g['image'] ?>" class="card-img-top" alt="<?= $g['title'] ?>" style="height: 150px; object-fit: cover;">
                        <div class="card-body p-3">
                            <h6 class="fw-bold mb-1 text-truncate"><?= $g['title'] ?></h6>
                            <span class="badge bg-secondary mb-2"><?= $g['category'] ?></span>
                            <div class="d-flex justify-content-between mt-2">
                                <a href="#" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-edit"></i></a>
                                <form action="#" method="POST" class="d-inline">
                                    <button class="btn btn-sm btn-outline-danger" onclick="return confirm('Hapus foto ini?')"><i class="fa-solid fa-trash"></i></button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
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

print("Admin Views 3 created successfully.")
