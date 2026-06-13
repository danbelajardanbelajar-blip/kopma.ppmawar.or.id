<?php
class AdminProfileController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $profileModel = $this->model('ProfileModel');
        $data = [
            'title' => 'Kelola Profil Koperasi',
            'profile' => $profileModel->get()
        ];
        $this->view('admin/profile', $data);
    }

    public function update() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $profileModel = $this->model('ProfileModel');
            
            $data = [
                'koperasi_name' => Helper::sanitize($_POST['koperasi_name']),
                'tagline' => Helper::sanitize($_POST['tagline']),
                'description' => $_POST['description'], // allow HTML if WYSIWYG
                'address' => Helper::sanitize($_POST['address']),
                'phone' => Helper::sanitize($_POST['phone']),
                'email' => Helper::sanitize($_POST['email']),
                'wa_number' => Helper::sanitize($_POST['wa_number']),
                'maps_embed' => $_POST['maps_embed'],
                'founded_year' => Helper::sanitize($_POST['founded_year']),
                'vision' => $_POST['vision'],
                'mission' => $_POST['mission']
            ];
            
            $profileModel->update($data);
            Flash::set('success', 'Profil berhasil diperbarui.');
            $this->redirect('/admin-profile');
        }
    }
}
