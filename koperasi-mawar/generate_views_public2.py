import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

views = {
    r"app\views\public\news_detail.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
""",

    r"app\views\public\gallery.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
""",

    r"app\views\public\faq.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
""",

    r"app\views\public\contact.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

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
                                <p class="mb-0"><?= $contact['address'] ?? 'Jl. Mawar Raya No. 1, Jakarta Selatan' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-solid fa-phone"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Telepon</h6>
                                <p class="mb-0"><?= $contact['phone'] ?? '021-1234567' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-brands fa-whatsapp"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">WhatsApp</h6>
                                <p class="mb-0"><?= $contact['wa_number'] ?? '081234567890' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-solid fa-envelope"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Email</h6>
                                <p class="mb-0"><?= $contact['email'] ?? 'info@kopma.ppmawar.or.id' ?></p>
                            </div>
                        </li>
                        <li class="d-flex align-items-start">
                            <div class="bg-white bg-opacity-25 rounded-circle p-3 me-3">
                                <i class="fa-regular fa-clock"></i>
                            </div>
                            <div>
                                <h6 class="fw-bold mb-1 opacity-75">Jam Operasional</h6>
                                <p class="mb-0"><?= nl2br($contact['office_hours'] ?? "Senin - Jumat: 08:00 - 16:00\nSabtu: 08:00 - 12:00") ?></p>
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
""",

    r"app\views\member\dashboard.php": """<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<section class="py-5 bg-light" style="min-height: calc(100vh - 200px);">
    <div class="container mt-4">
        <div class="row g-4">
            <div class="col-lg-3">
                <?php include APP_ROOT . '/app/views/layouts/member_sidebar.php'; ?>
            </div>
            
            <div class="col-lg-9">
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5 mb-4">
                    <div class="d-flex align-items-center justify-content-between mb-2">
                        <h3 class="fw-bold mb-0">Hai, <?= $member['name'] ?>!</h3>
                        <span class="badge <?= $member['status'] == 'active' ? 'bg-success' : 'bg-warning' ?> fs-6"><?= ucfirst($member['status']) ?></span>
                    </div>
                    <p class="text-muted mb-0">No. Anggota: <strong class="text-dark"><?= $member['member_code'] ?></strong></p>
                </div>
                
                <div class="row g-4 mb-4">
                    <div class="col-md-6">
                        <div class="card shadow-sm border-0 rounded-4 p-4 h-100 bg-primary text-white overflow-hidden position-relative">
                            <i class="fa-solid fa-wallet position-absolute" style="font-size: 8rem; right: -20px; bottom: -20px; opacity: 0.1;"></i>
                            <h5 class="opacity-75 mb-3">Total Saldo Simpanan</h5>
                            <h2 class="fw-bold mb-0 display-6"><?= Helper::formatRupiah($total_savings) ?></h2>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card shadow-sm border-0 rounded-4 p-4 h-100 bg-secondary text-white overflow-hidden position-relative">
                            <i class="fa-solid fa-hand-holding-dollar position-absolute" style="font-size: 8rem; right: -20px; bottom: -20px; opacity: 0.1;"></i>
                            <h5 class="opacity-75 mb-3">Pembiayaan Aktif</h5>
                            <h2 class="fw-bold mb-0 display-6"><?= count($active_financings) ?> <span class="fs-5 fw-normal">Kontrak</span></h2>
                        </div>
                    </div>
                </div>
                
                <div class="card shadow-sm border-0 rounded-4 mb-4">
                    <div class="card-header bg-white border-0 pt-4 pb-0 px-4">
                        <h5 class="fw-bold d-flex justify-content-between align-items-center">
                            Menu Cepat
                        </h5>
                    </div>
                    <div class="card-body p-4">
                        <div class="row g-3">
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/member-dashboard/applyFinancing" class="btn btn-outline-primary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-file-signature fs-3"></i>
                                    <span>Ajukan Pembiayaan</span>
                                </a>
                            </div>
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/member-dashboard/savings" class="btn btn-outline-primary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-money-bill-transfer fs-3"></i>
                                    <span>Riwayat Simpanan</span>
                                </a>
                            </div>
                            <div class="col-md-4">
                                <a href="<?= BASE_URL ?>/simulation" class="btn btn-outline-secondary w-100 py-3 rounded-3 d-flex flex-column align-items-center gap-2">
                                    <i class="fa-solid fa-calculator fs-3"></i>
                                    <span>Simulasi Angsuran</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="card shadow-sm border-0 rounded-4">
                    <div class="card-header bg-white border-bottom p-4">
                        <h5 class="fw-bold mb-0">Angsuran Mendatang</h5>
                    </div>
                    <div class="card-body p-0">
                        <div class="table-responsive">
                            <table class="table table-hover align-middle mb-0">
                                <thead class="table-light">
                                    <tr>
                                        <th class="ps-4">Tenggat Waktu</th>
                                        <th>Produk</th>
                                        <th>Jumlah Tagihan</th>
                                        <th>Status</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php if(empty($upcoming_installments)): ?>
                                    <tr>
                                        <td colspan="4" class="text-center py-4 text-muted">Belum ada tagihan angsuran.</td>
                                    </tr>
                                    <?php else: ?>
                                        <?php 
                                        $count = 0;
                                        foreach($upcoming_installments as $inst): 
                                            if($inst['status'] == 'pending' && $count < 3):
                                                $count++;
                                        ?>
                                        <tr>
                                            <td class="ps-4 fw-medium text-danger"><?= date('d M Y', strtotime($inst['due_date'])) ?></td>
                                            <td><?= $inst['product_name'] ?></td>
                                            <td class="fw-bold"><?= Helper::formatRupiah($inst['amount']) ?></td>
                                            <td><span class="badge bg-warning text-dark">Belum Dibayar</span></td>
                                        </tr>
                                        <?php endif; endforeach; ?>
                                        <?php if($count == 0): ?>
                                            <tr>
                                                <td colspan="4" class="text-center py-4 text-muted">Semua tagihan bulan ini sudah dilunasi.</td>
                                            </tr>
                                        <?php endif; ?>
                                    <?php endif; ?>
                                </tbody>
                            </table>
                        </div>
                    </div>
                    <?php if($count > 0): ?>
                    <div class="card-footer bg-white border-top p-3 text-center">
                        <a href="<?= BASE_URL ?>/member-dashboard/installments" class="text-decoration-none text-primary fw-medium">Lihat Semua Riwayat</a>
                    </div>
                    <?php endif; ?>
                </div>
                
            </div>
        </div>
    </div>
</section>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
"""
}

for rel_path, content in views.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Public Views 2 created successfully.")
