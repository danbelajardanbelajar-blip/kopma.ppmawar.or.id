<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Tanya Jawab (FAQ)</h1>
        <p class="lead opacity-75">Pertanyaan yang sering diajukan seputar Koperasi Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                
                <?php if(empty($faqs)): ?>
                    <div class="text-center py-5">
                        <h4 class="text-muted">Belum ada FAQ.</h4>
                    </div>
                <?php else: ?>
                    <div class="accordion shadow-sm rounded-4 overflow-hidden" id="accordionFaq">
                        <?php foreach($faqs as $index => $faq): ?>
                        <div class="accordion-item border-0 border-bottom">
                            <h2 class="accordion-header">
                                <button class="accordion-button <?= $index == 0 ? '' : 'collapsed' ?> fw-bold py-4 fs-5" type="button" data-bs-toggle="collapse" data-bs-target="#faq<?= $faq['id'] ?>">
                                    <?= $faq['question'] ?>
                                </button>
                            </h2>
                            <div id="faq<?= $faq['id'] ?>" class="accordion-collapse collapse <?= $index == 0 ? 'show' : '' ?>" data-bs-parent="#accordionFaq">
                                <div class="accordion-body pb-4 pt-0 lh-lg text-secondary-emphasis fs-5">
                                    <span class="badge bg-light text-dark mb-3"><?= $faq['category'] ?></span><br>
                                    <?= nl2br($faq['answer']) ?>
                                </div>
                            </div>
                        </div>
                        <?php endforeach; ?>
                    </div>
                <?php endif; ?>
                
                <div class="text-center mt-5 pt-4">
                    <h5 class="fw-bold">Masih punya pertanyaan lain?</h5>
                    <p class="text-muted mb-4">Jangan ragu untuk menghubungi tim layanan kami.</p>
                    <a href="<?= BASE_URL ?>/contact" class="btn btn-primary rounded-pill px-4">Hubungi Kami</a>
                </div>
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
