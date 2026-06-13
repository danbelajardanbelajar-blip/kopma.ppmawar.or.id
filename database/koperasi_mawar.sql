-- Database: koperasi_mawar

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
('Admin Koperasi', 'admin@kopma.ppmawar.or.id', '$2y$10$oIF7qjywCm9zfbpfZpf6RuFCh6qLScooZ1Ao9wNfnwr3dPjwm0PIa', 'admin', 'active', NOW(), NOW()),
('Ahmad Anggota', 'anggota@kopma.ppmawar.or.id', '$2y$10$OEbTkv6KERIWOvNRdkSKU.erKBdIovqCwXKJPFHeVq2wI/sv3xw8G', 'member', 'active', NOW(), NOW());

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
