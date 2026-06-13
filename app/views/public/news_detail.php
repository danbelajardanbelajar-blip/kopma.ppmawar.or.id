<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header pb-5">
    <div class="container">
        <nav aria-label="breadcrumb">
            <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="<?= BASE_URL ?>/" class="text-white text-decoration-none">Beranda</a></li>
                <li class="breadcrumb-item"><a href="<?= BASE_URL ?>/news" class="text-white text-decoration-none">Berita</a></li>
                <li class="breadcrumb-item active text-white opacity-75" aria-current="page">Detail</li>
            </ol>
        </nav>
        <h1 class="display-6 fw-bold mt-3"><?= $news['title'] ?></h1>
        <div class="d-flex align-items-center mt-3 opacity-75">
            <span class="me-4"><i class="fa-regular fa-calendar me-2"></i> <?= date('d M Y', strtotime($news['created_at'])) ?></span>
            <span class="badge bg-secondary"><?= $news['category'] ?></span>
        </div>
    </div>
</div>

<section class="py-5" style="margin-top: -40px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-8">
                <div class="card shadow-sm border-0 rounded-4 overflow-hidden mb-5">
                    <?php if($news['thumbnail']): ?>
                        <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $news['thumbnail'] ?>" class="w-100" alt="<?= $news['title'] ?>">
                    <?php endif; ?>
                    <div class="card-body p-4 p-md-5">
                        <div class="content lh-lg fs-5 text-secondary-emphasis">
                            <?= $news['content'] ?>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="col-lg-4">
                <div class="card shadow-sm border-0 rounded-4 p-4 sticky-top" style="top: 100px;">
                    <h5 class="fw-bold mb-4 border-bottom pb-2">Berita Terbaru</h5>
                    <div class="d-flex flex-column gap-3">
                        <?php foreach($latest as $item): ?>
                        <div class="d-flex align-items-center gap-3">
                            <?php if($item['thumbnail']): ?>
                                <img src="<?= BASE_URL ?>/assets/img/uploads/<?= $item['thumbnail'] ?>" class="rounded-3" style="width: 80px; height: 80px; object-fit: cover;" alt="<?= $item['title'] ?>">
                            <?php else: ?>
                                <div class="bg-light rounded-3 d-flex justify-content-center align-items-center" style="width: 80px; height: 80px;">
                                    <i class="fa-regular fa-image text-muted opacity-50"></i>
                                </div>
                            <?php endif; ?>
                            <div>
                                <h6 class="fw-bold mb-1"><a href="<?= BASE_URL ?>/news/detail/<?= $item['slug'] ?>" class="text-dark text-decoration-none lh-sm d-block"><?= Helper::truncate($item['title'], 50) ?></a></h6>
                                <small class="text-muted"><?= date('d M Y', strtotime($item['created_at'])) ?></small>
                            </div>
                        </div>
                        <?php endforeach; ?>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
