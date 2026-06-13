<?php
class ProfileController extends Controller {
    public function index() {
        $profileModel = $this->model('ProfileModel');
        $data = [
            'title' => 'Tentang Koperasi',
            'profile' => $profileModel->get()
        ];
        $this->view('public/about', $data);
    }

    public function vision() {
        $profileModel = $this->model('ProfileModel');
        $data = [
            'title' => 'Visi dan Misi',
            'profile' => $profileModel->get()
        ];
        $this->view('public/vision', $data);
    }

    public function management() {
        $data = ['title' => 'Struktur Pengurus'];
        $this->view('public/management', $data);
    }

    public function dps() {
        $data = ['title' => 'Dewan Pengawas Syariah'];
        $this->view('public/dps', $data);
    }

    public function legality() {
        $data = ['title' => 'Legalitas'];
        $this->view('public/legality', $data);
    }
}
