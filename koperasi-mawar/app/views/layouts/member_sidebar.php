<div class="card shadow-sm mb-4">
    <div class="card-body text-center p-4">
        <div class="avatar-placeholder mb-3 mx-auto" style="width:80px;height:80px;background:#1B6B3A;color:white;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:2rem;">
            <?= substr($_SESSION['name'], 0, 1) ?>
        </div>
        <h5 class="fw-bold mb-1"><?= $_SESSION['name'] ?></h5>
        <p class="text-muted small mb-0">Anggota Koperasi</p>
    </div>
    <div class="list-group list-group-flush border-top">
        <a href="<?= BASE_URL ?>/member-dashboard" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'member-dashboard') !== false && !strpos($_SERVER['REQUEST_URI'], '/') ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-gauge me-2 w-20px"></i> Dashboard
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/profile" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'profile') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-user me-2 w-20px"></i> Profil Saya
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/savings" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'savings') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-wallet me-2 w-20px"></i> Simpanan Saya
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/financing" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'financing') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-hand-holding-dollar me-2 w-20px"></i> Pembiayaan
        </a>
        <a href="<?= BASE_URL ?>/member-dashboard/installments" class="list-group-item list-group-item-action <?= strpos($_SERVER['REQUEST_URI'], 'installments') !== false ? 'active bg-primary border-primary' : '' ?>">
            <i class="fa-solid fa-calendar-check me-2 w-20px"></i> Riwayat Angsuran
        </a>
        <a href="<?= BASE_URL ?>/auth/logout" class="list-group-item list-group-item-action text-danger">
            <i class="fa-solid fa-right-from-bracket me-2 w-20px"></i> Keluar
        </a>
    </div>
</div>
