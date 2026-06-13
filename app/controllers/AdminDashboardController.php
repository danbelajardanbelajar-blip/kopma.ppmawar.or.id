<?php
class AdminDashboardController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $memberModel = $this->model('MemberModel');
        $appModel = $this->model('FinancingApplicationModel');
        $msgModel = $this->model('MessageModel');
        
        $data = [
            'title' => 'Dashboard Admin',
            'total_members' => $memberModel->count(),
            'pending_apps' => $appModel->count('pending'),
            'unread_msgs' => $msgModel->countUnread(),
            'latest_members' => $memberModel->findAll(5)
        ];
        $this->view('admin/dashboard', $data);
    }
}
