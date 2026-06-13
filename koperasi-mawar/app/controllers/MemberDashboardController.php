<?php
class MemberDashboardController extends Controller {
    public function __construct() {
        Auth::requireMember();
    }

    public function index() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $savingModel = $this->model('SavingModel');
        $financingModel = $this->model('FinancingModel');
        $installmentModel = $this->model('InstallmentModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Dashboard Anggota',
            'member' => $member,
            'total_savings' => $savingModel->getTotalByMemberId($member['id']),
            'active_financings' => $financingModel->getActiveByMemberId($member['id']),
            'upcoming_installments' => $installmentModel->findByMemberId($member['id']) // Simplification
        ];
        $this->view('member/dashboard', $data);
    }

    public function profile() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        
        $data = [
            'title' => 'Profil Saya',
            'member' => $memberModel->findByUserId($user['id'])
        ];
        $this->view('member/profile', $data);
    }

    public function savings() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $savingModel = $this->model('SavingModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Simpanan Saya',
            'savings' => $savingModel->findByMemberId($member['id'])
        ];
        $this->view('member/savings', $data);
    }

    public function financing() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $financingModel = $this->model('FinancingModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Pembiayaan Saya',
            'financings' => $financingModel->findByMemberId($member['id'])
        ];
        $this->view('member/financing', $data);
    }

    public function applyFinancing() {
        $productModel = $this->model('FinancingProductModel');
        
        $data = [
            'title' => 'Ajukan Pembiayaan',
            'products' => $productModel->findActive()
        ];
        $this->view('member/apply_financing', $data);
    }

    public function submitApplication() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $user = Auth::getCurrentUser();
            $memberModel = $this->model('MemberModel');
            $appModel = $this->model('FinancingApplicationModel');
            
            $member = $memberModel->findByUserId($user['id']);
            
            $data = [
                'member_id' => $member['id'],
                'product_id' => $_POST['product_id'],
                'amount' => str_replace(['Rp', '.', ' '], '', $_POST['amount']),
                'tenor' => $_POST['tenor'],
                'purpose' => Helper::sanitize($_POST['purpose'])
            ];
            
            $appModel->create($data);
            
            Flash::set('success', 'Pengajuan berhasil dikirim. Menunggu persetujuan admin.');
            $this->redirect('/member-dashboard/financing');
        }
    }
    
    public function installments() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $installmentModel = $this->model('InstallmentModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Riwayat Angsuran',
            'installments' => $installmentModel->findByMemberId($member['id'])
        ];
        $this->view('member/installments', $data);
    }
}
