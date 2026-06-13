import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

controllers = {
    r"app\controllers\HomeController.php": """<?php
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
""",

    r"app\controllers\ProfileController.php": """<?php
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
""",

    r"app\controllers\ProductController.php": """<?php
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
""",

    r"app\controllers\MembershipController.php": """<?php
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
""",

    r"app\controllers\SimulationController.php": """<?php
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
""",

    r"app\controllers\NewsController.php": """<?php
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
""",

    r"app\controllers\GalleryController.php": """<?php
class GalleryController extends Controller {
    public function index() {
        $galleryModel = $this->model('GalleryModel');
        $category = isset($_GET['category']) ? $_GET['category'] : null;
        
        $data = [
            'title' => 'Galeri',
            'galleries' => $galleryModel->findAll($category),
            'category' => $category
        ];
        $this->view('public/gallery', $data);
    }
}
""",

    r"app\controllers\FaqController.php": """<?php
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
""",

    r"app\controllers\ContactController.php": """<?php
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
""",

    r"app\controllers\AuthController.php": """<?php
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
""",

    r"app\controllers\MemberDashboardController.php": """<?php
class MemberDashboardController extends Controller {
    public function __construct() {
        Auth::requireMember();
    }

    public function index() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $savingModel = $this->model('SavingModel');
        $financingModel = $this->model('FinancingModel');
        $installmentModel = $this->model('InstallmentModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Dashboard Anggota',
            'member' => $member,
            'total_savings' => $savingModel->getTotalByMemberId($member['id']),
            'active_financings' => $financingModel->getActiveByMemberId($member['id']),
            'upcoming_installments' => $installmentModel->findByMemberId($member['id']) // Simplification
        ];
        $this->view('member/dashboard', $data);
    }

    public function profile() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        
        $data = [
            'title' => 'Profil Saya',
            'member' => $memberModel->findByUserId($user['id'])
        ];
        $this->view('member/profile', $data);
    }

    public function savings() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $savingModel = $this->model('SavingModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Simpanan Saya',
            'savings' => $savingModel->findByMemberId($member['id'])
        ];
        $this->view('member/savings', $data);
    }

    public function financing() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $financingModel = $this->model('FinancingModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Pembiayaan Saya',
            'financings' => $financingModel->findByMemberId($member['id'])
        ];
        $this->view('member/financing', $data);
    }

    public function applyFinancing() {
        $productModel = $this->model('FinancingProductModel');
        
        $data = [
            'title' => 'Ajukan Pembiayaan',
            'products' => $productModel->findActive()
        ];
        $this->view('member/apply_financing', $data);
    }

    public function submitApplication() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $user = Auth::getCurrentUser();
            $memberModel = $this->model('MemberModel');
            $appModel = $this->model('FinancingApplicationModel');
            
            $member = $memberModel->findByUserId($user['id']);
            
            $data = [
                'member_id' => $member['id'],
                'product_id' => $_POST['product_id'],
                'amount' => str_replace(['Rp', '.', ' '], '', $_POST['amount']),
                'tenor' => $_POST['tenor'],
                'purpose' => Helper::sanitize($_POST['purpose'])
            ];
            
            $appModel->create($data);
            
            Flash::set('success', 'Pengajuan berhasil dikirim. Menunggu persetujuan admin.');
            $this->redirect('/member-dashboard/financing');
        }
    }
    
    public function installments() {
        $user = Auth::getCurrentUser();
        $memberModel = $this->model('MemberModel');
        $installmentModel = $this->model('InstallmentModel');
        
        $member = $memberModel->findByUserId($user['id']);
        
        $data = [
            'title' => 'Riwayat Angsuran',
            'installments' => $installmentModel->findByMemberId($member['id'])
        ];
        $this->view('member/installments', $data);
    }
}
""",

    r"app\controllers\AdminDashboardController.php": """<?php
class AdminDashboardController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $memberModel = $this->model('MemberModel');
        $appModel = $this->model('FinancingApplicationModel');
        $msgModel = $this->model('MessageModel');
        
        $data = [
            'title' => 'Dashboard Admin',
            'total_members' => $memberModel->count(),
            'pending_apps' => $appModel->count('pending'),
            'unread_msgs' => $msgModel->countUnread(),
            'latest_members' => $memberModel->findAll(5)
        ];
        $this->view('admin/dashboard', $data);
    }
}
""",

    r"app\controllers\AdminProfileController.php": """<?php
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
""",

    r"app\controllers\AdminSavingProductController.php": """<?php
class AdminSavingProductController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('SavingProductModel');
        $data = [
            'title' => 'Kelola Produk Simpanan',
            'products' => $model->findAll()
        ];
        $this->view('admin/saving_products', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('SavingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'Produk ditambahkan.');
            $this->redirect('/admin-saving-product');
        }
    }

    public function update($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('SavingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->update($id, $data);
            Flash::set('success', 'Produk diperbarui.');
            $this->redirect('/admin-saving-product');
        }
    }

    public function delete($id) {
        $model = $this->model('SavingProductModel');
        $model->delete($id);
        Flash::set('success', 'Produk dihapus.');
        $this->redirect('/admin-saving-product');
    }
}
""",

    r"app\controllers\AdminFinancingProductController.php": """<?php
class AdminFinancingProductController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FinancingProductModel');
        $data = [
            'title' => 'Kelola Produk Pembiayaan',
            'products' => $model->findAll()
        ];
        $this->view('admin/financing_products', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'akad' => Helper::sanitize($_POST['akad']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'max_amount' => $_POST['max_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'max_tenor' => $_POST['max_tenor'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'Produk ditambahkan.');
            $this->redirect('/admin-financing-product');
        }
    }

    public function update($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingProductModel');
            $data = [
                'name' => Helper::sanitize($_POST['name']),
                'type' => Helper::sanitize($_POST['type']),
                'akad' => Helper::sanitize($_POST['akad']),
                'description' => Helper::sanitize($_POST['description']),
                'min_amount' => $_POST['min_amount'],
                'max_amount' => $_POST['max_amount'],
                'margin_rate' => $_POST['margin_rate'],
                'max_tenor' => $_POST['max_tenor'],
                'terms' => Helper::sanitize($_POST['terms']),
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->update($id, $data);
            Flash::set('success', 'Produk diperbarui.');
            $this->redirect('/admin-financing-product');
        }
    }

    public function delete($id) {
        $model = $this->model('FinancingProductModel');
        $model->delete($id);
        Flash::set('success', 'Produk dihapus.');
        $this->redirect('/admin-financing-product');
    }
}
""",

    r"app\controllers\AdminMemberController.php": """<?php
class AdminMemberController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('MemberModel');
        $keyword = isset($_GET['q']) ? $_GET['q'] : '';
        
        $data = [
            'title' => 'Kelola Anggota',
            'members' => $keyword ? $model->search($keyword) : $model->findAll(100),
            'keyword' => $keyword
        ];
        $this->view('admin/members', $data);
    }
}
""",

    r"app\controllers\AdminApplicationController.php": """<?php
class AdminApplicationController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FinancingApplicationModel');
        $status = isset($_GET['status']) ? $_GET['status'] : null;
        
        $data = [
            'title' => 'Pengajuan Pembiayaan',
            'applications' => $model->findAll($status),
            'status' => $status
        ];
        $this->view('admin/applications', $data);
    }

    public function approve($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingApplicationModel');
            $model->updateStatus($id, 'approved', Helper::sanitize($_POST['notes'] ?? ''));
            
            // Logic to create financing record would go here
            
            Flash::set('success', 'Pengajuan disetujui.');
            $this->redirect('/admin-application');
        }
    }

    public function reject($id) {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FinancingApplicationModel');
            $model->updateStatus($id, 'rejected', Helper::sanitize($_POST['notes'] ?? ''));
            Flash::set('success', 'Pengajuan ditolak.');
            $this->redirect('/admin-application');
        }
    }
}
""",

    r"app\controllers\AdminNewsController.php": """<?php
class AdminNewsController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('NewsModel');
        $data = [
            'title' => 'Kelola Berita',
            'news' => $model->findAll()
        ];
        $this->view('admin/news', $data);
    }
    
    public function create() {
        $data = ['title' => 'Tambah Berita'];
        $this->view('admin/news_form', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('NewsModel');
            $user = Auth::getCurrentUser();
            
            $thumbnail = null;
            if (isset($_FILES['thumbnail']) && $_FILES['thumbnail']['error'] == UPLOAD_ERR_OK) {
                $thumbnail = Helper::uploadImage($_FILES['thumbnail'], UPLOAD_PATH);
            }
            
            $data = [
                'title' => Helper::sanitize($_POST['title']),
                'slug' => Helper::slugify($_POST['title']),
                'content' => $_POST['content'], // allow html
                'category' => Helper::sanitize($_POST['category']),
                'thumbnail' => $thumbnail,
                'author_id' => $user['id'],
                'is_published' => isset($_POST['is_published']) ? 1 : 0
            ];
            
            $model->create($data);
            Flash::set('success', 'Berita ditambahkan.');
            $this->redirect('/admin-news');
        }
    }

    public function delete($id) {
        $model = $this->model('NewsModel');
        $model->delete($id);
        Flash::set('success', 'Berita dihapus.');
        $this->redirect('/admin-news');
    }
}
""",

    r"app\controllers\AdminGalleryController.php": """<?php
class AdminGalleryController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('GalleryModel');
        $data = [
            'title' => 'Kelola Galeri',
            'galleries' => $model->findAll()
        ];
        $this->view('admin/gallery', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('GalleryModel');
            
            $image = null;
            if (isset($_FILES['image']) && $_FILES['image']['error'] == UPLOAD_ERR_OK) {
                $image = Helper::uploadImage($_FILES['image'], UPLOAD_PATH);
            }
            
            if ($image) {
                $data = [
                    'title' => Helper::sanitize($_POST['title']),
                    'description' => Helper::sanitize($_POST['description']),
                    'category' => Helper::sanitize($_POST['category']),
                    'image' => $image
                ];
                $model->create($data);
                Flash::set('success', 'Foto ditambahkan.');
            } else {
                Flash::set('error', 'Gagal upload foto.');
            }
            $this->redirect('/admin-gallery');
        }
    }

    public function delete($id) {
        $model = $this->model('GalleryModel');
        $model->delete($id);
        Flash::set('success', 'Foto dihapus.');
        $this->redirect('/admin-gallery');
    }
}
""",

    r"app\controllers\AdminFaqController.php": """<?php
class AdminFaqController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('FaqModel');
        $data = [
            'title' => 'Kelola FAQ',
            'faqs' => $model->findAll()
        ];
        $this->view('admin/faq', $data);
    }

    public function store() {
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $model = $this->model('FaqModel');
            $data = [
                'question' => Helper::sanitize($_POST['question']),
                'answer' => $_POST['answer'],
                'category' => Helper::sanitize($_POST['category']),
                'sort_order' => (int)$_POST['sort_order'],
                'is_active' => isset($_POST['is_active']) ? 1 : 0
            ];
            $model->create($data);
            Flash::set('success', 'FAQ ditambahkan.');
            $this->redirect('/admin-faq');
        }
    }

    public function delete($id) {
        $model = $this->model('FaqModel');
        $model->delete($id);
        Flash::set('success', 'FAQ dihapus.');
        $this->redirect('/admin-faq');
    }
}
""",

    r"app\controllers\AdminContactController.php": """<?php
class AdminContactController extends Controller {
    public function __construct() {
        Auth::requireAdmin();
    }

    public function index() {
        $model = $this->model('MessageModel');
        $data = [
            'title' => 'Pesan Masuk',
            'messages' => $model->findAll(100)
        ];
        $this->view('admin/contacts', $data);
    }

    public function show($id) {
        $model = $this->model('MessageModel');
        $model->markRead($id);
        $this->redirect('/admin-contact'); // Normally would show detail view
    }

    public function delete($id) {
        $model = $this->model('MessageModel');
        $model->delete($id);
        Flash::set('success', 'Pesan dihapus.');
        $this->redirect('/admin-contact');
    }
}
"""
}

for rel_path, content in controllers.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Controllers created successfully.")
