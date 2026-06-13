<?php
class AdminApplicationController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FinancingApplicationModel');
        $status = isset($_GET['status']) ? $_GET['status'] : null;
        
        $data = [
            'title' => 'Pengajuan Pembiayaan',
            'applications' => $model->findAll($status),
            'status' => $status
        ];
        $this->view('admin/applications', $data);
    }

    public function approve($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingApplicationModel');
            $model->updateStatus($id, 'approved', Helper::sanitize($_POST['notes'] ?? ''));
            
            // Logic to create financing record would go here
            
            Flash::set('success', 'Pengajuan disetujui.');
            $this->redirect('/admin-application');
        }
    }

    public function reject($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingApplicationModel');
            $model->updateStatus($id, 'rejected', Helper::sanitize($_POST['notes'] ?? ''));
            Flash::set('success', 'Pengajuan ditolak.');
            $this->redirect('/admin-application');
        }
    }
}
