<?php
class AdminContactController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('MessageModel');
        $data = [
            'title' => 'Pesan Masuk',
            'messages' => $model->findAll(100)
        ];
        $this->view('admin/contacts', $data);
    }

    public function show($id) {
        $model = $this->model('MessageModel');
        $model->markRead($id);
        $this->redirect('/admin-contact'); // Normally would show detail view
    }

    public function delete($id) {
        $model = $this->model('MessageModel');
        $model->delete($id);
        Flash::set('success', 'Pesan dihapus.');
        $this->redirect('/admin-contact');
    }
}
