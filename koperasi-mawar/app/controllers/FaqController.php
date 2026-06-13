<?php
class FaqController extends Controller {
    public function index() {
        $faqModel = $this->model('FaqModel');
        $data = [
            'title' => 'FAQ',
            'faqs' => $faqModel->findActive()
        ];
        $this->view('public/faq', $data);
    }
}
