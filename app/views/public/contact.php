<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header pb-5">
    <div class="container">
        <h1 class="display-5 fw-bold">Kontak Kami</h1>
        <p class="lead opacity-75">Kami siap membantu dan melayani Anda</p>
    </div>
</div>

<section class="py-5" style="margin-top: -60px; position: relative; z-index: 10;">
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-5">
                <div class="card shadow border-0 rounded-4 p-4 p-md-5 mb-4 bg-primary text-white">
                    <h3 class="fw-bold mb-4">Informasi Kontak</h3>
                    <ul class="list-unstyled d-flex flex-column gap-4 fs-5">
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-solid fa-location-dot"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Alamat Kantor</h6>
                                <p class="mb-0"><?= $contact['address'] ?? 'PP. Matholi''ul Anwar Dusun Simo RT 016 RW 005 Desa Sungelebak Kecamatan Karanggeneng Kabupaten Lamongan' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-solid fa-phone"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Telepon</h6>
                                <p class="mb-0"><?= $contact['phone'] ?? '085655352223' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-brands fa-whatsapp"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">WhatsApp</h6>
                                <p class="mb-0"><?= $contact['wa_number'] ?? '085655352223' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Email</h6>
                                <p class="mb-0"><?= $contact['email'] ?? 'kjksMawar@gmail.com' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-regular fa-clock"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Jam Operasional</h6>
                                <p class="mb-0"><?= nl2br($contact['office_hours'] ?? "Senin - Jumat: 08:00 - 16:00
Sabtu: 08:00 - 12:00") ?></p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            
            <div class="col-lg-7">
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5 bg-white">
                    <h3 class="fw-bold mb-4">Kirim Pesan</h3>
                    
                    <?php if($flash = Flash::get()): ?>
                    <div class="alert alert-<?= $flash['type'] == 'error' ? 'danger' : 'success' ?> mb-4">
                        <?= $flash['message'] ?>
                    </div>
                    <?php endif; ?>
                    
                    <form action="<?= BASE_URL ?>/contact/send" method="POST">
                        <div class="row g-3 mb-3">
                            <div class="col-md-6">
                                <label class="form-label fw-medium">Nama Lengkap</label>
                                <input type="text" name="name" class="form-control form-control-lg bg-light border-0" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-medium">Email</label>
                                <input type="email" name="email" class="form-control form-control-lg bg-light border-0" required>
                            </div>
                        </div>
                        <div class="row g-3 mb-3">
                            <div class="col-md-6">
                                <label class="form-label fw-medium">No. Telepon / WA</label>
                                <input type="text" name="phone" class="form-control form-control-lg bg-light border-0" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-medium">Subjek Pesan</label>
                                <input type="text" name="subject" class="form-control form-control-lg bg-light border-0" required>
                            </div>
                        </div>
                        <div class="mb-4">
                            <label class="form-label fw-medium">Isi Pesan</label>
                            <textarea name="message" class="form-control form-control-lg bg-light border-0" rows="5" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary btn-lg rounded-pill px-5">Kirim Pesan Sekarang</button>
                    </form>
                </div>
            </div>
        </div>
        
        <?php if(!empty($contact['maps_embed'])): ?>
        <div class="row mt-5">
            <div class="col-12">
                <div class="card shadow-sm border-0 rounded-4 overflow-hidden p-2">
                    <div style="border-radius: 12px; overflow: hidden;">
                        <?= $contact['maps_embed'] ?>
                    </div>
                </div>
            </div>
        </div>
        <?php endif; ?>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
