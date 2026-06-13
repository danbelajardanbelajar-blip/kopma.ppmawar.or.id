<?php
class AdminNewsController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('NewsModel');
        $data = [
            'title' => 'Kelola Berita',
            'news' => $model->findAll()
        ];
        $this->view('admin/news', $data);
    }
    
    public function create() {
        $data = ['title' => 'Tambah Berita'];
        $this->view('admin/news_form', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('NewsModel');
            $user = Auth::getCurrentUser();
            
            $thumbnail = null;
            if (isset($_FILES['thumbnail']) && $_FILES['thumbnail']['error'] == UPLOAD_ERR_OK) {
                $thumbnail = Helper::uploadImage($_FILES['thumbnail'], UPLOAD_PATH);
            }
            
            $data = [
                'title' => Helper::sanitize($_POST['title']),
                'slug' => Helper::slugify($_POST['title']),
                'content' => $_POST['content'], // allow html
                'category' => Helper::sanitize($_POST['category']),
                'thumbnail' => $thumbnail,
                'author_id' => $user['id'],
                'is_published' => isset($_POST['is_published']) ? 1 : 0
            ];
            
            $model->create($data);
            Flash::set('success', 'Berita ditambahkan.');
            $this->redirect('/admin-news');
        }
    }

    public function delete($id) {
        $model = $this->model('NewsModel');
        $model->delete($id);
        Flash::set('success', 'Berita dihapus.');
        $this->redirect('/admin-news');
    }
}
