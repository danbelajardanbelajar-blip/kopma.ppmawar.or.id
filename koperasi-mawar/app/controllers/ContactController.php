<?php
class ContactController extends Controller {
    public function index() {
        $contactModel = $this->model('ContactModel');
        $data = [
            'title' => 'Kontak Kami',
            'contact' => $contactModel->get()
        ];
        $this->view('public/contact', $data);
    }

    public function send() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $messageModel = $this->model('MessageModel');
            
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'email' => Helper::sanitize($_POST['email']),
                'phone' => Helper::sanitize($_POST['phone']),
                'subject' => Helper::sanitize($_POST['subject']),
                'message' => Helper::sanitize($_POST['message'])
            ];
            
            $messageModel->create($data);
            
            Flash::set('success', 'Pesan Anda berhasil dikirim.');
            $this->redirect('/contact');
        }
    }
}
