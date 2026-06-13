<?php
class AdminFinancingProductController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FinancingProductModel');
        $data = [
            'title' => 'Kelola Produk Pembiayaan',
            'products' => $model->findAll()
        ];
        $this->view('admin/financing_products', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'akad' => Helper::sanitize($_POST['akad']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'max_amount' => $_POST['max_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'max_tenor' => $_POST['max_tenor'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'Produk ditambahkan.');
            $this->redirect('/admin-financing-product');
        }
    }

    public function update($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'akad' => Helper::sanitize($_POST['akad']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'max_amount' => $_POST['max_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'max_tenor' => $_POST['max_tenor'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->update($id, $data);
            Flash::set('success', 'Produk diperbarui.');
            $this->redirect('/admin-financing-product');
        }
    }

    public function delete($id) {
        $model = $this->model('FinancingProductModel');
        $model->delete($id);
        Flash::set('success', 'Produk dihapus.');
        $this->redirect('/admin-financing-product');
    }
}
