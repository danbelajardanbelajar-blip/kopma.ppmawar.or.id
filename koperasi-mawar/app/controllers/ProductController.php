<?php
class ProductController extends Controller {
    public function savings() {
        $savingModel = $this->model('SavingProductModel');
        $data = [
            'title' => 'Simpanan Syariah',
            'products' => $savingModel->findActive()
        ];
        $this->view('public/savings', $data);
    }

    public function financing() {
        $financingModel = $this->model('FinancingProductModel');
        $data = [
            'title' => 'Pembiayaan Syariah',
            'products' => $financingModel->findActive()
        ];
        $this->view('public/financing', $data);
    }
}
