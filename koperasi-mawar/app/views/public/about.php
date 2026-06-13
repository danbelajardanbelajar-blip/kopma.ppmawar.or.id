<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Tentang Koperasi</h1>
        <p class="lead opacity-75">Mengenal lebih dekat Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card shadow-sm border-0 rounded-4 p-md-5 p-4">
                    <div class="text-center mb-5">
                        <i class="fa-solid fa-building-columns text-primary mb-3" style="font-size: 4rem;"></i>
                        <h2 class="fw-bold"><?= $profile['koperasi_name'] ?? 'Koperasi Mawar' ?></h2>
                        <p class="text-secondary fs-5"><?= $profile['tagline'] ?? '' ?></p>
                    </div>
                    
                    <div class="content lh-lg fs-5 text-secondary-emphasis">
                        <p><?= nl2br($profile['description'] ?? 'Deskripsi belum tersedia.') ?></p>
                    </div>
                    
                    <hr class="my-5 text-muted">
                    
                    <h3 class="fw-bold mb-4 text-center">Informasi Umum</h3>
                    <div class="row g-4">
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-light rounded-3">
                                <i class="fa-solid fa-calendar-check text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0 text-muted">Tahun Berdiri</h6>
                                    <h5 class="mb-0 fw-bold"><?= $profile['founded_year'] ?? '-' ?></h5>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="d-flex align-items-center p-3 bg-light rounded-3">
                                <i class="fa-solid fa-location-dot text-primary fs-3 me-3"></i>
                                <div>
                                    <h6 class="mb-0 text-muted">Lokasi</h6>
                                    <h5 class="mb-0 fw-bold">Jakarta Selatan</h5>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
