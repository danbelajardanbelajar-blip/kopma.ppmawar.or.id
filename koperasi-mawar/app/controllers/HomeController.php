<?php
class HomeController extends Controller {
    public function index() {
        $newsModel = $this->model('NewsModel');
        $savingModel = $this->model('SavingProductModel');
        $financingModel = $this->model('FinancingProductModel');
        $profileModel = $this->model('ProfileModel');

        $data = [
            'title' => 'Beranda',
            'profile' => $profileModel->get(),
            'latest_news' => $newsModel->findLatest(3),
            'savings' => $savingModel->findActive(),
            'financings' => $financingModel->findActive()
        ];
        $this->view('public/home', $data);
    }
}
