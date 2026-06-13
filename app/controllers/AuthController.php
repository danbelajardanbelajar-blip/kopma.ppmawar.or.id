<?php
class AuthController extends Controller {
    public function login() {
        if (Auth::isLoggedIn()) {
            if (Auth::isAdmin()) $this->redirect('/admin-dashboard');
            else $this->redirect('/member-dashboard');
        }
        
        $data = ['title' => 'Login Anggota'];
        $this->view('public/login', $data);
    }

    public function authenticate() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $userModel = $this->model('UserModel');
            
            $email = Helper::sanitize($_POST['email']);
            $password = $_POST['password'];
            
            $user = $userModel->findByEmail($email);
            
            if ($user && password_verify($password, $user['password'])) {
                if ($user['status'] !== 'active') {
                    Flash::set('error', 'Akun Anda belum aktif/disetujui.');
                    $this->redirect('/auth/login');
                }
                
                Auth::login($user);
                
                if ($user['role'] === 'admin') {
                    $this->redirect('/admin-dashboard');
                } else {
                    $this->redirect('/member-dashboard');
                }
            } else {
                Flash::set('error', 'Email atau password salah.');
                $this->redirect('/auth/login');
            }
        }
    }

    public function adminLogin() {
        if (Auth::isLoggedIn()) {
            if (Auth::isAdmin()) $this->redirect('/admin-dashboard');
            else $this->redirect('/member-dashboard');
        }
        
        $data = ['title' => 'Login Admin'];
        $this->view('admin/login', $data);
    }

    public function logout() {
        Auth::logout();
        $this->redirect('/');
    }
}
