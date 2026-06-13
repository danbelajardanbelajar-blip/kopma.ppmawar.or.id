<?php
class NewsController extends Controller {
    public function index() {
        $newsModel = $this->model('NewsModel');
        $page = isset($_GET['page']) ? (int)$_GET['page'] : 1;
        $category = isset($_GET['category']) ? $_GET['category'] : null;
        
        $limit = PER_PAGE;
        $offset = ($page - 1) * $limit;
        
        $news = $newsModel->findAll($limit, $offset, $category);
        $total = $newsModel->count($category);
        
        $data = [
            'title' => 'Berita Koperasi',
            'news' => $news,
            'current_page' => $page,
            'total_pages' => ceil($total / $limit),
            'category' => $category
        ];
        $this->view('public/news', $data);
    }

    public function detail($slug) {
        $newsModel = $this->model('NewsModel');
        $news = $newsModel->findBySlug($slug);
        
        if (!$news) {
            $this->redirect('/news');
        }
        
        $data = [
            'title' => $news['title'],
            'news' => $news,
            'latest' => $newsModel->findLatest(5)
        ];
        $this->view('public/news_detail', $data);
    }
}
