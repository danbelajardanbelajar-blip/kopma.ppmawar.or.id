<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Visi dan Misi</h1>
        <p class="lead opacity-75">Arah dan tujuan Koperasi Syariah Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-5 justify-content-center">
            <div class="col-lg-10">
                <div class="card shadow-sm border-0 rounded-4 overflow-hidden mb-5 card-hover-lift">
                    <div class="row g-0">
                        <div class="col-md-4 bg-primary text-white p-5 d-flex flex-column justify-content-center align-items-center text-center">
                            <i class="fa-solid fa-eye fs-1 mb-3 text-secondary"></i>
                            <h2 class="fw-bold m-0">VISI</h2>
                        </div>
                        <div class="col-md-8 p-5 d-flex align-items-center">
                            <p class="fs-4 lh-base text-secondary-emphasis fst-italic mb-0">
                                "<?= $profile['vision'] ?? 'Menjadi koperasi terbaik di Indonesia.' ?>"
                            </p>
                        </div>
                    </div>
                </div>

                <div class="card shadow-sm border-0 rounded-4 overflow-hidden card-hover-lift">
                    <div class="row g-0">
                        <div class="col-md-4 bg-secondary text-white p-5 d-flex flex-column justify-content-center align-items-center text-center order-md-2">
                            <i class="fa-solid fa-bullseye fs-1 mb-3 text-primary-dark"></i>
                            <h2 class="fw-bold m-0 text-primary-dark">MISI</h2>
                        </div>
                        <div class="col-md-8 p-5 order-md-1">
                            <div class="fs-5 lh-lg text-secondary-emphasis">
                                <?= nl2br($profile['mission'] ?? "1. Menciptakan kesejahteraan bagi para anggota yang berkesinambungan.
2. Berdaya guna sebagai mitra strategis dan terpercaya bagi anggota.
3. Berkontribusi dalam perkembangan perkoperasian di Indonesia.
4. Mengelola Koperasi dan unit usaha secara profesional dengan menerapkan prinsip \"good corporate governance\".") ?>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
