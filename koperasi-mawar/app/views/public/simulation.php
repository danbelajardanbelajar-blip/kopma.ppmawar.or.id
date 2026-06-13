<?php include APP_ROOT . '/app/views/layouts/public_header.php'; ?>

<div class="page-header">
    <div class="container">
        <h1 class="display-5 fw-bold">Simulasi Pembiayaan</h1>
        <p class="lead opacity-75">Hitung estimasi angsuran pembiayaan syariah Anda</p>
    </div>
</div>

<section class="py-5 my-4">
    <div class="container">
        <div class="row g-5">
            <div class="col-lg-5">
                <div class="card shadow-sm border-0 rounded-4 p-4 p-md-5 bg-white">
                    <h4 class="fw-bold mb-4 border-bottom pb-3">Parameter Simulasi</h4>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Produk Pembiayaan</label>
                        <select class="form-select form-select-lg" id="sim_product" onchange="calculateSimulation()">
                            <option value="">Pilih Produk...</option>
                            <?php foreach($products as $p): ?>
                                <option value="<?= $p['id'] ?>" data-margin="<?= $p['margin_rate'] ?>"><?= $p['name'] ?> (<?= $p['akad'] ?> - Margin: <?= $p['margin_rate'] ?>%/thn)</option>
                            <?php endforeach; ?>
                        </select>
                    </div>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Jumlah Pembiayaan (Rp)</label>
                        <input type="text" class="form-control form-control-lg" id="sim_amount" placeholder="Contoh: 10.000.000" onkeyup="calculateSimulation()">
                    </div>
                    
                    <div class="mb-4">
                        <label class="form-label fw-medium">Tenor / Jangka Waktu (Bulan)</label>
                        <input type="number" class="form-control form-control-lg" id="sim_tenor" min="1" max="120" value="12" onkeyup="calculateSimulation()" onchange="calculateSimulation()">
                    </div>
                    
                    <button type="button" class="btn btn-primary w-100 btn-lg rounded-pill" onclick="calculateSimulation()">Hitung Sekarang</button>
                    <p class="text-muted small text-center mt-3">* Hasil simulasi ini adalah estimasi dan dapat berbeda dengan perhitungan riil.</p>
                </div>
            </div>
            
            <div class="col-lg-7">
                <div class="card shadow border-0 rounded-4 p-4 p-md-5 bg-primary text-white h-100" id="simulation_result" style="display:none; background-image: url('data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');">
                    <h3 class="fw-bold mb-4 text-secondary border-bottom border-light pb-3">Hasil Simulasi</h3>
                    
                    <div class="row g-4 mt-2">
                        <div class="col-sm-6">
                            <div class="p-3 bg-white bg-opacity-10 rounded-3">
                                <p class="mb-1 opacity-75">Pokok Pembiayaan</p>
                                <h4 class="fw-bold mb-0" id="res_amount">Rp 0</h4>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="p-3 bg-white bg-opacity-10 rounded-3">
                                <p class="mb-1 opacity-75">Estimasi Margin</p>
                                <h4 class="fw-bold mb-0" id="res_margin">Rp 0</h4>
                            </div>
                        </div>
                        <div class="col-12 mt-4">
                            <div class="p-4 bg-white rounded-4 text-dark text-center shadow-lg">
                                <p class="mb-1 text-muted fw-bold text-uppercase">Angsuran Per Bulan</p>
                                <h1 class="fw-bold text-primary mb-0 display-5" id="res_monthly">Rp 0</h1>
                            </div>
                        </div>
                        <div class="col-12 mt-4 text-center">
                            <p class="mb-1 opacity-75">Total Pengembalian (Pokok + Margin)</p>
                            <h4 class="fw-bold text-secondary mb-0" id="res_total">Rp 0</h4>
                        </div>
                    </div>
                    
                    <div class="text-center mt-5">
                        <a href="<?= BASE_URL ?>/membership/register" class="btn btn-secondary btn-lg rounded-pill px-5">Ajukan Pembiayaan</a>
                    </div>
                </div>
                
                <div class="card shadow-sm border-0 rounded-4 p-5 h-100 d-flex justify-content-center align-items-center text-center bg-light" id="simulation_empty" style="display:flex;">
                    <i class="fa-solid fa-calculator text-muted opacity-50 mb-4" style="font-size: 5rem;"></i>
                    <h4 class="text-muted">Masukkan parameter di samping untuk melihat hasil simulasi.</h4>
                </div>
            </div>
        </div>
    </div>
</section>

<script>
    // Hide empty state and show result when calculate is clicked
    const origCalculate = window.calculateSimulation;
    window.calculateSimulation = function() {
        if(origCalculate) origCalculate();
        if(document.getElementById('sim_product').value && document.getElementById('sim_amount').value) {
            document.getElementById('simulation_empty').style.display = 'none';
        }
    }
</script>

<?php include APP_ROOT . '/app/views/layouts/public_footer.php'; ?>
