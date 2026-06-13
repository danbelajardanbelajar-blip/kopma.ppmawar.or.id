<?php
class GalleryController extends Controller {
    public function index() {
        $galleryModel = $this->model('GalleryModel');
        $category = isset($_GET['category']) ? $_GET['category'] : null;
        
        $data = [
            'title' => 'Galeri',
            'galleries' => $galleryModel->findAll($category),
            'category' => $category
        ];
        $this->view('public/gallery', $data);
    }
}
