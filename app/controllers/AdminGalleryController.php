<?php
class AdminGalleryController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('GalleryModel');
        $data = [
            'title' => 'Kelola Galeri',
            'galleries' => $model->findAll()
        ];
        $this->view('admin/gallery', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('GalleryModel');
            
            $image = null;
            if (isset($_FILES['image']) && $_FILES['image']['error'] == UPLOAD_ERR_OK) {
                $image = Helper::uploadImage($_FILES['image'], UPLOAD_PATH);
            }
            
            if ($image) {
                $data = [
                    'title' => Helper::sanitize($_POST['title']),
                    'description' => Helper::sanitize($_POST['description']),
                    'category' => Helper::sanitize($_POST['category']),
                    'image' => $image
                ];
                $model->create($data);
                Flash::set('success', 'Foto ditambahkan.');
            } else {
                Flash::set('error', 'Gagal upload foto.');
            }
            $this->redirect('/admin-gallery');
        }
    }

    public function delete($id) {
        $model = $this->model('GalleryModel');
        $model->delete($id);
        Flash::set('success', 'Foto dihapus.');
        $this->redirect('/admin-gallery');
    }
}
