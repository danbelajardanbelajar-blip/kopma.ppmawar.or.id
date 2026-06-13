<?php include APP_ROOT . '/app/views/layouts/admin_header.php'; ?>

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
