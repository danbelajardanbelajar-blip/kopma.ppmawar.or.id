<?php
class AdminSavingProductController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('SavingProductModel');
        $data = [
            'title' => 'Kelola Produk Simpanan',
            'products' => $model->findAll()
        ];
        $this->view('admin/saving_products', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('SavingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'Produk ditambahkan.');
            $this->redirect('/admin-saving-product');
        }
    }

    public function update($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('SavingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->update($id, $data);
            Flash::set('success', 'Produk diperbarui.');
            $this->redirect('/admin-saving-product');
        }
    }

    public function delete($id) {
        $model = $this->model('SavingProductModel');
        $model->delete($id);
        Flash::set('success', 'Produk dihapus.');
        $this->redirect('/admin-saving-product');
    }
}
