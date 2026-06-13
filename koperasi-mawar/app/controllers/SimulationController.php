<?php
class SimulationController extends Controller {
    public function index() {
        $financingModel = $this->model('FinancingProductModel');
        $data = [
            'title' => 'Simulasi Pembiayaan',
            'products' => $financingModel->findActive()
        ];
        $this->view('public/simulation', $data);
    }

    public function calculate() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $amount = floatval(str_replace(['Rp', '.', ' '], '', $_POST['amount']));
            $margin = floatval($_POST['margin']);
            $tenor = intval($_POST['tenor']);

            if ($amount <= 0 || $margin <= 0 || $tenor <= 0) {
                $this->json(['error' => 'Input tidak valid']);
            }

            $marginAmount = ($amount * ($margin / 100) * ($tenor / 12));
            $totalPayment = $amount + $marginAmount;
            $monthlyPayment = $totalPayment / $tenor;

            $this->json([
                'amount' => Helper::formatRupiah($amount),
                'margin_amount' => Helper::formatRupiah($marginAmount),
                'total_payment' => Helper::formatRupiah($totalPayment),
                'monthly_payment' => Helper::formatRupiah($monthlyPayment)
            ]);
        }
    }
}
