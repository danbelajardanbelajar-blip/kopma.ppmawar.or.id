<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Keanggotaan</h1>
        <p class="lead opacity-75">Syarat, Hak, dan Kewajiban Anggota Koperasi Mawar</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <ul class="nav nav-pills nav-fill mb-4 custom-pills" id="membershipTab" role="tablist">
                    <li class="nav-item" role="presentation">
                        <button class="nav-link active rounded-pill fw-bold" id="syarat-tab" data-bs-toggle="tab" data-bs-target="#syarat-tab-pane" type="button" role="tab" aria-controls="syarat-tab-pane" aria-selected="true">Syarat Keanggotaan</button>
                    </li>
                    <li class="nav-item" role="presentation">
                        <button class="nav-link rounded-pill fw-bold" id="hak-tab" data-bs-toggle="tab" data-bs-target="#hak-tab-pane" type="button" role="tab" aria-controls="hak-tab-pane" aria-selected="false">Hak & Kewajiban</button>
                    </li>
                </ul>
                
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5">
                    <div class="tab-content" id="myTabContent">
                        <!-- Syarat -->
                        <div class="tab-pane fade show active" id="syarat-tab-pane" role="tabpanel" aria-labelledby="syarat-tab" tabindex="0">
                            <h4 class="fw-bold mb-4 text-primary"><i class="fa-solid fa-list-check me-2"></i>Syarat Menjadi Anggota</h4>
                            <ul class="list-group list-group-flush fs-5">
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Warga Negara Indonesia yang cakap hukum.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Memiliki KTP/Identitas yang sah.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Menyetujui Anggaran Dasar (AD) dan Anggaran Rumah Tangga (ART) Koperasi.</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Membayar Simpanan Pokok sebesar Rp 500.000 (sekali bayar).</li>
                                <li class="list-group-item py-3 px-0 border-light"><i class="fa-solid fa-check text-success me-3"></i>Bersedia membayar Simpanan Wajib sebesar Rp 50.000 setiap bulan.</li>
                            </ul>
                            <div class="text-center mt-5">
                                <a href="<?= BASE_URL ?>/membership/register" class="btn btn-primary btn-lg rounded-pill px-5">Daftar Sekarang</a>
                            </div>
                        </div>
                        
                        <!-- Hak & Kewajiban -->
                        <div class="tab-pane fade" id="hak-tab-pane" role="tabpanel" aria-labelledby="hak-tab" tabindex="0">
                            <h4 class="fw-bold mb-4 text-primary"><i class="fa-solid fa-scale-balanced me-2"></i>Hak Anggota</h4>
                            <ul class="list-group list-group-flush mb-5">
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Menghadiri, menyatakan pendapat, dan memberikan suara dalam RAT.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Memilih dan/atau dipilih menjadi anggota Pengurus atau Pengawas.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Meminta diadakan RAT sesuai ketentuan AD/ART.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Mengemukakan pendapat atau saran kepada Pengurus.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Memanfaatkan pelayanan koperasi.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-arrow-right text-secondary me-2"></i>Mendapat bagian Sisa Hasil Usaha (SHU).</li>
                            </ul>
                            
                            <h4 class="fw-bold mb-4 text-danger"><i class="fa-solid fa-clipboard-list me-2"></i>Kewajiban Anggota</h4>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Mematuhi AD, ART, dan Keputusan RAT.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Berpartisipasi dalam kegiatan usaha koperasi.</li>
                                <li class="list-group-item border-light py-2 px-0"><i class="fa-solid fa-circle-exclamation text-danger me-2"></i>Mengembangkan dan memelihara kebersamaan berdasar atas asas kekeluargaan.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<style>
.custom-pills .nav-link {
    color: var(--dark);
    transition: all 0.3s;
}
.custom-pills .nav-link.active {
    background-color: var(--primary);
    box-shadow: 0 4px 10px rgba(27, 107, 58, 0.3);
}
</style>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
