import os

base_dir = r"c:\Users\zenhk\OneDrive\Documents\GitHub\kopma.ppmawar.or.id\koperasi-mawar"

assets = {
    r"public\index.php": """<?php
// Start session
session_start();

// Load config
require_once dirname(__DIR__) . '/config/config.php';

// Autoload core and other classes
spl_autoload_register(function($class) {
    $paths = [
        APP_ROOT . '/app/core/' . $class . '.php',
        APP_ROOT . '/app/controllers/' . $class . '.php',
        APP_ROOT . '/app/models/' . $class . '.php',
        APP_ROOT . '/app/helpers/' . $class . '.php',
    ];
    foreach ($paths as $path) {
        if (file_exists($path)) {
            require_once $path;
            return;
        }
    }
});

// Run app
$app = new App();
""",

    r"public\.htaccess": """Options -Indexes
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-l
RewriteRule ^(.*)$ index.php?url=$1 [QSA,L]
""",

    r"public\assets\css\main.css": """@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
    --primary: #1B6B3A;
    --primary-dark: #0D3D22;
    --primary-light: #2A9D55;
    --secondary: #C9A84C;
    --secondary-light: #DFCD90;
    --dark: #212529;
    --light: #F8F9FA;
    --white: #ffffff;
    --gray: #6c757d;
}

body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: var(--dark);
    background-color: var(--light);
    overflow-x: hidden;
}

h1, h2, h3, h4, h5, h6, .navbar-brand {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
}

.text-primary { color: var(--primary) !important; }
.text-secondary { color: var(--secondary) !important; }
.bg-primary { background-color: var(--primary) !important; }
.bg-secondary { background-color: var(--secondary) !important; }

/* Buttons */
.btn-primary {
    background-color: var(--primary);
    border-color: var(--primary);
    color: var(--white);
    transition: all 0.3s ease;
}
.btn-primary:hover {
    background-color: var(--primary-dark);
    border-color: var(--primary-dark);
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(27, 107, 58, 0.2);
}

.btn-secondary {
    background-color: var(--secondary);
    border-color: var(--secondary);
    color: var(--white);
    transition: all 0.3s ease;
}
.btn-secondary:hover {
    background-color: #b39543;
    border-color: #b39543;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(201, 168, 76, 0.2);
}

.btn-outline-primary {
    color: var(--primary);
    border-color: var(--primary);
}
.btn-outline-primary:hover {
    background-color: var(--primary);
    color: var(--white);
}

/* Navbar */
.navbar {
    transition: all 0.3s ease;
    padding: 1rem 0;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.navbar.scrolled {
    padding: 0.5rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.navbar-nav .nav-link {
    font-weight: 500;
    color: var(--dark);
    padding: 0.5rem 1rem;
    position: relative;
    transition: all 0.3s ease;
}
.navbar-nav .nav-link:hover, .navbar-nav .nav-link.active {
    color: var(--primary);
}
.navbar-nav .nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: 0;
    left: 50%;
    background-color: var(--secondary);
    transition: all 0.3s ease;
    transform: translateX(-50%);
}
.navbar-nav .nav-link:hover::after, .navbar-nav .nav-link.active::after {
    width: 80%;
}

/* Dropdown */
.dropdown-menu {
    border: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border-radius: 8px;
    padding: 0.5rem 0;
}
.dropdown-item {
    padding: 0.5rem 1.5rem;
    font-weight: 500;
    transition: all 0.2s ease;
}
.dropdown-item:hover {
    background-color: rgba(27, 107, 58, 0.05);
    color: var(--primary);
}

/* Hero Section */
.hero {
    position: relative;
    padding: 120px 0 80px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: var(--white);
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('data:image/svg+xml,%3Csvg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%23c9a84c" fill-opacity="0.1"%3E%3Cpath d="M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');
    opacity: 0.5;
}
.hero-content {
    position: relative;
    z-index: 1;
}

/* Islamic Pattern Background */
.bg-pattern {
    position: relative;
}
.bg-pattern::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('data:image/svg+xml,%3Csvg width="60" height="60" viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="none" fill-rule="evenodd"%3E%3Cg fill="%231b6b3a" fill-opacity="0.05"%3E%3Cpath d="M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z"/%3E%3C/g%3E%3C/g%3E%3C/svg%3E');
    z-index: 0;
    pointer-events: none;
}
.bg-pattern > * {
    position: relative;
    z-index: 1;
}

/* Cards */
.card {
    border: none;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
    overflow: hidden;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}
.card-hover-lift {
    transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.card-hover-lift:hover {
    transform: translateY(-10px);
}

/* Section Headings */
.section-title {
    position: relative;
    margin-bottom: 2.5rem;
    padding-bottom: 1rem;
    color: var(--primary-dark);
}
.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 60px;
    height: 3px;
    background-color: var(--secondary);
    border-radius: 3px;
}
.section-title.text-start::after {
    left: 0;
    transform: none;
}

/* Badges */
.badge {
    padding: 0.5em 0.8em;
    font-weight: 500;
    border-radius: 6px;
}
.badge.bg-success { background-color: #2A9D55 !important; }
.badge.bg-warning { background-color: #C9A84C !important; color: #fff; }
.badge.bg-danger { background-color: #dc3545 !important; }

/* Footer */
.footer {
    background-color: var(--primary-dark);
    color: var(--white);
    padding: 60px 0 20px;
}
.footer a {
    color: rgba(255,255,255,0.7);
    text-decoration: none;
    transition: all 0.3s ease;
}
.footer a:hover {
    color: var(--secondary);
    padding-left: 5px;
}
.footer-bottom {
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.1);
    font-size: 0.9rem;
    color: rgba(255,255,255,0.6);
}

/* Page Header */
.page-header {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    padding: 80px 0 40px;
    color: white;
    text-align: center;
    position: relative;
}

/* Stats Counter */
.stat-card {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}
.stat-card .icon {
    font-size: 2.5rem;
    color: var(--secondary);
    margin-bottom: 1rem;
}
.stat-card h3 {
    font-size: 2.5rem;
    color: var(--primary);
    font-weight: 700;
}

/* Utilities */
.shadow-sm { box-shadow: 0 2px 10px rgba(0,0,0,0.03) !important; }
.shadow { box-shadow: 0 5px 20px rgba(0,0,0,0.05) !important; }
.shadow-lg { box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important; }

/* SPALoader */
#spa-loader {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background-color: var(--secondary);
    z-index: 9999;
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

/* Back to Top */
#back-to-top {
    position: fixed;
    bottom: 30px;
    right: 30px;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background-color: var(--primary);
    color: white;
    border: none;
    font-size: 1.2rem;
    display: none;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    z-index: 1000;
    transition: all 0.3s ease;
}
#back-to-top:hover {
    background-color: var(--secondary);
    transform: translateY(-3px);
}
""",

    r"public\assets\css\admin.css": """@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

:root {
    --primary: #1B6B3A;
    --sidebar-bg: #0D3D22;
    --sidebar-hover: rgba(255,255,255,0.1);
    --sidebar-active: #1B6B3A;
    --bg-light: #f4f6f9;
}

body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: var(--bg-light);
    overflow-x: hidden;
}

/* Admin Layout */
#admin-wrapper {
    display: flex;
    width: 100%;
    height: 100vh;
}

/* Sidebar */
#sidebar {
    width: 250px;
    background-color: var(--sidebar-bg);
    color: white;
    height: 100%;
    position: fixed;
    transition: all 0.3s ease;
    z-index: 100;
    overflow-y: auto;
}

.sidebar-header {
    padding: 20px;
    text-align: center;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}
.sidebar-header h3 {
    margin: 0;
    font-size: 1.2rem;
    font-weight: 700;
    color: #C9A84C;
}

.sidebar-menu {
    padding: 15px 0;
    list-style: none;
    margin: 0;
}
.sidebar-menu li {
    padding: 0 15px;
    margin-bottom: 5px;
}
.sidebar-menu a {
    color: rgba(255,255,255,0.8);
    text-decoration: none;
    display: flex;
    align-items: center;
    padding: 10px 15px;
    border-radius: 8px;
    transition: all 0.2s ease;
}
.sidebar-menu a i {
    width: 25px;
    font-size: 1.1rem;
}
.sidebar-menu a:hover {
    background-color: var(--sidebar-hover);
    color: white;
}
.sidebar-menu a.active {
    background-color: var(--sidebar-active);
    color: white;
    font-weight: 600;
}

/* Main Content */
#content {
    width: calc(100% - 250px);
    margin-left: 250px;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
}

/* Topbar */
.topbar {
    height: 60px;
    background: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
}
.topbar-btn {
    background: none;
    border: none;
    font-size: 1.2rem;
    color: #333;
    cursor: pointer;
}

.main-content {
    padding: 20px;
    flex: 1;
    overflow-y: auto;
}

/* Cards */
.card {
    border: none;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
    margin-bottom: 20px;
}
.card-header {
    background-color: white;
    border-bottom: 1px solid #eee;
    padding: 15px 20px;
    font-weight: 600;
    border-top-left-radius: 10px !important;
    border-top-right-radius: 10px !important;
}

/* Stat Cards */
.stat-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    display: flex;
    align-items: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.03);
}
.stat-icon {
    width: 60px;
    height: 60px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    margin-right: 15px;
}
.stat-icon.bg-primary-light { background: rgba(27, 107, 58, 0.1); color: var(--primary); }
.stat-icon.bg-warning-light { background: rgba(201, 168, 76, 0.1); color: #C9A84C; }
.stat-icon.bg-info-light { background: rgba(23, 162, 184, 0.1); color: #17a2b8; }

.stat-details h3 {
    margin: 0;
    font-size: 1.8rem;
    font-weight: 700;
}
.stat-details p {
    margin: 0;
    color: #6c757d;
    font-size: 0.9rem;
}

/* Tables */
.table th {
    font-weight: 600;
    color: #495057;
    border-top: none;
}
.table td {
    vertical-align: middle;
}

/* Toggling Sidebar */
#sidebar.collapsed {
    margin-left: -250px;
}
#content.expanded {
    width: 100%;
    margin-left: 0;
}

@media (max-width: 768px) {
    #sidebar {
        margin-left: -250px;
    }
    #content {
        width: 100%;
        margin-left: 0;
    }
    #sidebar.show {
        margin-left: 0;
    }
}
""",

    r"public\assets\js\app.js": """document.addEventListener('DOMContentLoaded', function() {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    }

    // Back to top button
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTop.style.display = 'flex';
            } else {
                backToTop.style.display = 'none';
            }
        });
        backToTop.addEventListener('click', function() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Auto dismiss flash messages
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Stats counter animation
    const counters = document.querySelectorAll('.counter');
    const speed = 200;

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 1);
                } else {
                    counter.innerText = target;
                }
            };
            updateCount();
        });
    }

    // Intersection Observer for counters
    if (counters.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                observer.disconnect();
            }
        });
        observer.observe(counters[0]);
    }

    // SPA Navigation Logic (Simple Fetch)
    /*
    const links = document.querySelectorAll('a.spa-link');
    const loader = document.getElementById('spa-loader');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.getAttribute('href');
            
            if (loader) loader.style.transform = 'scaleX(1)';
            
            fetch(url)
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    
                    // Replace main content
                    const newContent = doc.querySelector('main');
                    const oldContent = document.querySelector('main');
                    if(newContent && oldContent) {
                        oldContent.innerHTML = newContent.innerHTML;
                    }
                    
                    // Update title
                    document.title = doc.title;
                    
                    // Push state
                    history.pushState(null, doc.title, url);
                    
                    if (loader) loader.style.transform = 'scaleX(0)';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                })
                .catch(err => {
                    console.error('Failed to fetch page: ', err);
                    window.location.href = url; // Fallback
                });
        });
    });
    */
});

// Admin Sidebar Toggle
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    if (window.innerWidth > 768) {
        sidebar.classList.toggle('collapsed');
        content.classList.toggle('expanded');
    } else {
        sidebar.classList.toggle('show');
    }
}
""",

    r"public\assets\js\simulator.js": """function calculateSimulation() {
    const amountStr = document.getElementById('sim_amount').value;
    const amount = parseFloat(amountStr.replace(/[^0-9]/g, ''));
    const tenor = parseInt(document.getElementById('sim_tenor').value);
    
    const productSelect = document.getElementById('sim_product');
    const marginRate = parseFloat(productSelect.options[productSelect.selectedIndex].dataset.margin);
    
    if (isNaN(amount) || isNaN(tenor) || isNaN(marginRate)) return;
    
    const marginAmount = (amount * (marginRate / 100) * (tenor / 12));
    const totalPayment = amount + marginAmount;
    const monthlyPayment = totalPayment / tenor;
    
    document.getElementById('res_amount').innerText = formatRupiah(amount);
    document.getElementById('res_margin').innerText = formatRupiah(marginAmount);
    document.getElementById('res_total').innerText = formatRupiah(totalPayment);
    document.getElementById('res_monthly').innerText = formatRupiah(monthlyPayment);
    
    document.getElementById('simulation_result').style.display = 'block';
}

function formatRupiah(angka) {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(angka);
}

document.addEventListener('DOMContentLoaded', function() {
    const simAmount = document.getElementById('sim_amount');
    if (simAmount) {
        simAmount.addEventListener('keyup', function(e) {
            let val = this.value.replace(/[^0-9]/g, '');
            if(val) {
                this.value = new Intl.NumberFormat('id-ID').format(val);
            }
        });
    }
});
""",

    r"database\koperasi_mawar.sql": """-- Database: koperasi_mawar

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'member') DEFAULT 'member',
    status ENUM('active', 'inactive', 'pending') DEFAULT 'active',
    created_at DATETIME,
    updated_at DATETIME
);

CREATE TABLE members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    member_code VARCHAR(20) NOT NULL UNIQUE,
    nik VARCHAR(20) NOT NULL UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    join_date DATE,
    status ENUM('active', 'inactive', 'pending') DEFAULT 'active',
    photo VARCHAR(255),
    created_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    koperasi_name VARCHAR(100),
    tagline VARCHAR(255),
    description TEXT,
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    wa_number VARCHAR(20),
    maps_embed TEXT,
    founded_year INT,
    vision TEXT,
    mission TEXT,
    created_at DATETIME
);

CREATE TABLE savings_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    description TEXT,
    min_amount DECIMAL(15,2),
    margin_rate DECIMAL(5,2),
    terms TEXT,
    is_active TINYINT(1) DEFAULT 1,
    created_at DATETIME
);

CREATE TABLE financing_products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    akad VARCHAR(50),
    description TEXT,
    min_amount DECIMAL(15,2),
    max_amount DECIMAL(15,2),
    margin_rate DECIMAL(5,2),
    max_tenor INT,
    terms TEXT,
    is_active TINYINT(1) DEFAULT 1,
    created_at DATETIME
);

CREATE TABLE savings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    product_id INT NOT NULL,
    amount DECIMAL(15,2),
    balance DECIMAL(15,2),
    last_transaction DATETIME,
    status ENUM('active', 'closed') DEFAULT 'active',
    created_at DATETIME,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (product_id) REFERENCES savings_products(id)
);

CREATE TABLE financings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    product_id INT NOT NULL,
    amount DECIMAL(15,2),
    margin_rate DECIMAL(5,2),
    tenor INT,
    monthly_payment DECIMAL(15,2),
    start_date DATE,
    end_date DATE,
    status ENUM('active', 'completed', 'defaulted') DEFAULT 'active',
    purpose TEXT,
    created_at DATETIME,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (product_id) REFERENCES financing_products(id)
);

CREATE TABLE installments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    financing_id INT NOT NULL,
    member_id INT NOT NULL,
    due_date DATE,
    amount DECIMAL(15,2),
    paid_amount DECIMAL(15,2) DEFAULT 0,
    paid_date DATETIME NULL,
    status ENUM('pending', 'paid', 'late') DEFAULT 'pending',
    created_at DATETIME,
    FOREIGN KEY (financing_id) REFERENCES financings(id),
    FOREIGN KEY (member_id) REFERENCES members(id)
);

CREATE TABLE financing_applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    product_id INT NOT NULL,
    amount DECIMAL(15,2),
    tenor INT,
    purpose TEXT,
    status ENUM('pending', 'approved', 'rejected', 'cancelled') DEFAULT 'pending',
    admin_notes TEXT,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (member_id) REFERENCES members(id),
    FOREIGN KEY (product_id) REFERENCES financing_products(id)
);

CREATE TABLE news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) NOT NULL UNIQUE,
    content LONGTEXT,
    category VARCHAR(50),
    thumbnail VARCHAR(255),
    author_id INT,
    is_published TINYINT(1) DEFAULT 1,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (author_id) REFERENCES users(id)
);

CREATE TABLE galleries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    image VARCHAR(255) NOT NULL,
    category VARCHAR(50),
    created_at DATETIME
);

CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    category VARCHAR(50),
    sort_order INT DEFAULT 0,
    is_active TINYINT(1) DEFAULT 1,
    created_at DATETIME
);

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    koperasi_name VARCHAR(100),
    address TEXT,
    phone VARCHAR(20),
    email VARCHAR(100),
    wa_number VARCHAR(20),
    maps_embed TEXT,
    office_hours TEXT,
    created_at DATETIME
);

CREATE TABLE messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    subject VARCHAR(200),
    message TEXT,
    is_read TINYINT(1) DEFAULT 0,
    created_at DATETIME
);

-- SEED DATA
-- Admin pass: admin123, Member pass: anggota123
INSERT INTO users (name, email, password, role, status, created_at, updated_at) VALUES 
('Admin Koperasi', 'admin@kopma.ppmawar.or.id', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'admin', 'active', NOW(), NOW()),
('Ahmad Anggota', 'anggota@kopma.ppmawar.or.id', '$2y$10$TKh8H1.PkoxRs5M37kN2OubNNJa4XxW8r.mX3E9N2YFx0oiG4UHq6', 'member', 'active', NOW(), NOW());

INSERT INTO members (user_id, member_code, nik, phone, address, join_date, status, created_at) VALUES
(2, 'ANG-2024-0001', '3174000000000001', '08123456789', 'Jl. Mawar Raya No 123', '2024-01-01', 'active', NOW());

INSERT INTO profiles (koperasi_name, tagline, description, address, phone, email, wa_number, founded_year, vision, mission, created_at) VALUES
('Koperasi Syariah Mawar', 'Membangun Ekonomi Ummat Berlandaskan Syariah', 'Koperasi Syariah Mawar adalah lembaga keuangan mikro syariah yang bertujuan mensejahterakan anggota.', 'Jl. Mawar Raya No. 1, Jakarta Selatan', '021-1234567', 'info@kopma.ppmawar.or.id', '081234567890', 2010, 'Menjadi koperasi syariah terpercaya', 'Memberikan layanan keuangan syariah', NOW());

INSERT INTO savings_products (name, type, description, min_amount, margin_rate, terms, created_at) VALUES
('Simpanan Pokok', 'Wajib', 'Simpanan awal saat menjadi anggota', 500000, 0, 'Dibayar sekali di awal', NOW()),
('Simpanan Wajib', 'Wajib', 'Simpanan bulanan', 50000, 0, 'Dibayar rutin setiap bulan', NOW()),
('Simpanan Sukarela', 'Sukarela', 'Simpanan yang bisa diambil kapan saja', 10000, 0, 'Fleksibel', NOW());

INSERT INTO financing_products (name, type, akad, description, min_amount, max_amount, margin_rate, max_tenor, terms, created_at) VALUES
('Pembiayaan Usaha', 'Produktif', 'Mudharabah', 'Untuk modal usaha', 1000000, 50000000, 12, 36, 'Memiliki usaha berjalan', NOW()),
('Pembiayaan Kendaraan', 'Konsumtif', 'Murabahah', 'Untuk beli motor/mobil', 5000000, 200000000, 10, 60, 'DP minimal 20%', NOW());

INSERT INTO faqs (question, answer, category, created_at) VALUES
('Bagaimana cara mendaftar jadi anggota?', 'Silakan klik menu Daftar dan isi formulir', 'Keanggotaan', NOW()),
('Apakah ada bunga?', 'Kami menggunakan sistem syariah tanpa bunga', 'Layanan', NOW());
""",

    r"README.md": """# Koperasi Syariah Mawar

Website Sistem Informasi Koperasi Syariah Mawar dengan menggunakan PHP Native MVC.

## Fitur
- Halaman Profil Publik
- Sistem Keanggotaan
- Dashboard Anggota
- Dashboard Admin
- CRUD Produk, Berita, Galeri
- Simulasi Pembiayaan

## Cara Instalasi
1. Clone repositori ini
2. Pindahkan ke folder `htdocs` (XAMPP) atau direktori web server Anda
3. Buat database `koperasi_mawar` di phpMyAdmin
4. Import file `database/koperasi_mawar.sql`
5. Sesuaikan konfigurasi di `config/config.php` (DB_USER, DB_PASS, BASE_URL)
6. Akses aplikasi melalui browser

## Akun Demo
- Admin: `admin@kopma.ppmawar.or.id` | Pass: `admin123`
- Anggota: `anggota@kopma.ppmawar.or.id` | Pass: `anggota123`
"""
}

for rel_path, content in assets.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Assets and DB created successfully.")
