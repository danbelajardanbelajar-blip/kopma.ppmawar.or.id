<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Berita & Informasi</h1>
        <p class="lead opacity-75">Kabar terbaru dari Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row mb-5">
            <div class="col-md-8 mx-auto text-center">
                <div class="btn-group shadow-sm" role="group">
                    <a href="<?= BASE_URL ?>/news" class="btn btn-outline-primary <?= empty($category) ? 'active' : '' ?>">Semua</a>
                    <a href="<?= BASE_URL ?>/news?category=Artikel" class="btn btn-outline-primary <?= $category == 'Artikel' ? 'active' : '' ?>">Artikel</a>
                    <a href="<?= BASE_URL ?>/news?category=Kegiatan" class="btn btn-outline-primary <?= $category == 'Kegiatan' ? 'active' : '' ?>">Kegiatan</a>
                    <a href="<?= BASE_URL ?>/news?category=Pengumuman" class="btn btn-outline-primary <?= $category == 'Pengumuman' ? 'active' : '' ?>">Pengumuman</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            <?php if(empty($news)): ?>
                <div class="col-12 text-center py-5">
                    <h4 class="text-muted">Belum ada berita yang diterbitkan.</h4>
                </div>
            <?php else: ?>
                <?php foreach($news as $item): ?>
                <div class="col-lg-4 col-md-6">
                    <div class="card shadow-sm border-0 rounded-4 h-100 card-hover-lift overflow-hidden">
                        <?php if($item['thumbnail']): ?>
                            <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $item['thumbnail'] ?>" class="card-img-top" alt="<?= $item['title'] ?>" style="height: 200px; object-fit: cover;">
                        <?php else: ?>
                            <div class="bg-light d-flex justify-content-center align-items-center" style="height: 200px;">
                                <i class="fa-regular fa-image text-muted fs-1 opacity-50"></i>
                            </div>
                        <?php endif; ?>
                        <div class="card-body p-4">
                            <div class="d-flex justify-content-between mb-3 align-items-center">
                                <span class="badge bg-secondary"><?= $item['category'] ?></span>
                                <small class="text-muted"><i class="fa-regular fa-calendar me-1"></i> <?= date('d M Y', strtotime($item['created_at'])) ?></small>
                            </div>
                            <h5 class="card-title fw-bold mb-3"><a href="<?= BASE_URL ?>/news/detail/<?= $item['slug'] ?>" class="text-dark text-decoration-none"><?= $item['title'] ?></a></h5>
                            <p class="card-text text-muted"><?= Helper::truncate(strip_tags($item['content']), 100) ?></p>
                        </div>
                        <div class="card-footer bg-transparent border-top-0 px-4 pb-4 pt-0">
                            <a href="<?= BASE_URL ?>/news/detail/<?= $item['slug'] ?>" class="text-primary fw-bold text-decoration-none">Baca Selengkapnya <i class="fa-solid fa-arrow-right ms-1 small"></i></a>
                        </div>
                    </div>
                </div>
                <?php endforeach; ?>
            <?php endif; ?>
        </div>
        
        <?php if($total_pages > 1): ?>
        <nav class="mt-5">
            <ul class="pagination justify-content-center">
                <?php for($i=1; $i<=$total_pages; $i++): ?>
                    <li class="page-item <?= $i == $current_page ? 'active' : '' ?>">
                        <a class="page-link" href="<?= BASE_URL ?>/news?page=<?= $i ?><?= $category ? '&category='.$category : '' ?>"><?= $i ?></a>
                    </li>
                <?php endfor; ?>
            </ul>
        </nav>
        <?php endif; ?>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
