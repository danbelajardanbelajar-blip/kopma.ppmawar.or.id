<?php
class AdminMemberController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('MemberModel');
        $keyword = isset($_GET['q']) ? $_GET['q'] : '';
        
        $data = [
            'title' => 'Kelola Anggota',
            'members' => $keyword ? $model->search($keyword) : $model->findAll(100),
            'keyword' => $keyword
        ];
        $this->view('admin/members', $data);
    }
}
