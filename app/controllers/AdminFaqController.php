<?php
class AdminFaqController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FaqModel');
        $data = [
            'title' => 'Kelola FAQ',
            'faqs' => $model->findAll()
        ];
        $this->view('admin/faq', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FaqModel');
            $data = [
                'question' => Helper::sanitize($_POST['question']),
                'answer' => $_POST['answer'],
                'category' => Helper::sanitize($_POST['category']),
                'sort_order' => (int)$_POST['sort_order'],
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'FAQ ditambahkan.');
            $this->redirect('/admin-faq');
        }
    }

    public function delete($id) {
        $model = $this->model('FaqModel');
        $model->delete($id);
        Flash::set('success', 'FAQ dihapus.');
        $this->redirect('/admin-faq');
    }
}
