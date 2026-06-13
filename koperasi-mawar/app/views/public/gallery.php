<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Galeri Koperasi</h1>
        <p class="lead opacity-75">Dokumentasi kegiatan dan acara Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row mb-5">
            <div class="col-md-8 mx-auto text-center">
                <div class="btn-group shadow-sm" role="group">
                    <a href="<?= BASE_URL ?>/gallery" class="btn btn-outline-primary <?= empty($category) ? 'active' : '' ?>">Semua</a>
                    <a href="<?= BASE_URL ?>/gallery?category=Foto" class="btn btn-outline-primary <?= $category == 'Foto' ? 'active' : '' ?>">Foto Kegiatan</a>
                    <a href="<?= BASE_URL ?>/gallery?category=Dokumentasi" class="btn btn-outline-primary <?= $category == 'Dokumentasi' ? 'active' : '' ?>">Dokumentasi</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            <?php if(empty($galleries)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada foto dalam galeri.</h4>
                </div>
            <?php else: ?>
                <?php foreach($galleries as $item): ?>
                <div class="col-lg-4 col-md-6">
                    <div class="card shadow-sm border-0 rounded-4 overflow-hidden card-hover-lift h-100">
                        <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $item['image'] ?>" class="card-img-top" alt="<?= $item['title'] ?>" style="height: 250px; object-fit: cover;">
                        <div class="card-body p-4">
                            <span class="badge bg-secondary mb-2"><?= $item['category'] ?></span>
                            <h5 class="fw-bold mb-2"><?= $item['title'] ?></h5>
                            <?php if($item['description']): ?>
                                <p class="text-muted small mb-0"><?= Helper::truncate($item['description'], 80) ?></p>
                            <?php endif; ?>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
