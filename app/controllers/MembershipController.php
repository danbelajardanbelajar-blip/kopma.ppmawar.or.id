<?php
class MembershipController extends Controller {
    public function index() {
        $data = ['title' => 'Keanggotaan'];
        $this->view('public/membership', $data);
    }

    public function register() {
        $data = ['title' => 'Daftar Anggota'];
        $this->view('public/membership_form', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $userModel = $this->model('UserModel');
            $memberModel = $this->model('MemberModel');

            $email = Helper::sanitize($_POST['email']);
            if ($userModel->findByEmail($email)) {
                Flash::set('error', 'Email sudah terdaftar.');
                $this->redirect('/membership/register');
            }

            $userData = [
                'name' => Helper::sanitize($_POST['name']),
                'email' => $email,
                'password' => password_hash($_POST['password'], PASSWORD_DEFAULT),
                'role' => 'member',
                'status' => 'pending' // need admin approval
            ];
            
            $userId = $userModel->create($userData);

            $memberCode = Helper::generateMemberCode($memberModel->count());
            
            $memberData = [
                'user_id' => $userId,
                'member_code' => $memberCode,
                'nik' => Helper::sanitize($_POST['nik']),
                'phone' => Helper::sanitize($_POST['phone']),
                'address' => Helper::sanitize($_POST['address']),
                'status' => 'pending'
            ];
            
            $memberModel->create($memberData);

            Flash::set('success', 'Pendaftaran berhasil. Silakan tunggu persetujuan admin.');
            $this->redirect('/auth/login');
        }
    }
}
