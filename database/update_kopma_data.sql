-- Update Data Koperasi Mawar berdasarkan LPJ RAT 2025

-- 1. Update Tabel Profiles
UPDATE profiles SET 
    koperasi_name = 'Koperasi Simpan Pinjam dan Pembiayaan Syariah Matholi''ul Anwar Jawa Timur',
    address = 'PP. Matholi''ul Anwar Dusun Simo RT 016 RW 005 Desa Sungelebak Kecamatan Karanggeneng Kabupaten Lamongan',
    phone = '085655352223',
    email = 'kjksMawar@gmail.com',
    wa_number = '085655352223',
    founded_year = 2008,
    vision = 'Menjadi koperasi terbaik di Indonesia',
    mission = '1. Menciptakan kesejahteraan bagi para anggota yang berkesinambungan.<br>2. Berdaya guna sebagai mitra strategis dan terpercaya bagi anggota.<br>3. Berkontribusi dalam perkembangan perkoperasian di Indonesia.<br>4. Mengelola Koperasi dan unit usaha secara profesional dengan menerapkan prinsip "good corporate governance".'
WHERE id = 1;

-- 2. Update Tabel Contacts
UPDATE contacts SET 
    koperasi_name = 'Koperasi Simpan Pinjam dan Pembiayaan Syariah Matholi''ul Anwar Jawa Timur',
    address = 'PP. Matholi''ul Anwar Dusun Simo RT 016 RW 005 Desa Sungelebak Kecamatan Karanggeneng Kabupaten Lamongan',
    phone = '085655352223',
    email = 'kjksMawar@gmail.com',
    wa_number = '085655352223'
WHERE id = 1;

-- 3. Matikan pengecekan Foreign Key sementara, lalu Kosongkan data produk lama
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE savings_products;
TRUNCATE TABLE financing_products;
SET FOREIGN_KEY_CHECKS = 1;

-- 4. Masukkan data Produk Simpanan terbaru
INSERT INTO savings_products (name, type, description, min_amount, margin_rate, terms, created_at) VALUES
('Tabungan Syariah', 'Sukarela', 'Simpanan syariah harian', 10000, 0, 'Sesuai prinsip wadiah', NOW()),
('Tabungan Haji', 'Berjangka', 'Simpanan untuk perencanaan ibadah haji', 50000, 0, 'Sesuai prinsip syariah', NOW()),
('Tabungan Umroh', 'Berjangka', 'Simpanan untuk perencanaan ibadah umroh', 50000, 0, 'Sesuai prinsip syariah', NOW()),
('Tabungan Qurban', 'Berjangka', 'Simpanan untuk perencanaan ibadah qurban', 10000, 0, 'Bisa diambil menjelang Idul Adha', NOW()),
('Tabungan Berjangka', 'Berjangka', 'Simpanan dengan jangka waktu tertentu', 1000000, 5, 'Jangka waktu 1, 3, 6, 12 bulan', NOW());

-- 5. Masukkan data Produk Pembiayaan terbaru
INSERT INTO financing_products (name, type, akad, description, min_amount, max_amount, margin_rate, max_tenor, terms, created_at) VALUES
('Pembiayaan Murabahah', 'Konsumtif/Produktif', 'Murabahah', 'Pembiayaan jual beli barang', 1000000, 100000000, 12, 60, 'Sesuai prinsip syariah', NOW()),
('Pembiayaan Mudharabah', 'Produktif', 'Mudharabah', 'Pembiayaan modal usaha (bagi hasil)', 5000000, 200000000, 0, 60, 'Bagi hasil disepakati', NOW()),
('Pembiayaan Hiwalah', 'Jasa', 'Hiwalah', 'Pembiayaan pengalihan utang', 1000000, 50000000, 0, 24, 'Sesuai prinsip syariah', NOW()),
('Talangan Haji', 'Jasa', 'Qardh/Ijarah', 'Talangan porsi haji', 25000000, 25000000, 0, 60, 'Ujroh disepakati', NOW()),
('Pembiayaan Qardh', 'Sosial/Konsumtif', 'Qardh', 'Pinjaman kebajikan tanpa margin', 500000, 5000000, 0, 12, 'Tanpa tambahan/margin', NOW()),
('Pembiayaan Rahn/Ijarah', 'Jasa', 'Rahn/Ijarah', 'Pembiayaan beragun emas/barang', 1000000, 50000000, 0, 12, 'Ujroh disepakati', NOW()),
('Pembiayaan Jualah', 'Jasa', 'Jualah', 'Pembiayaan atas jasa/pekerjaan tertentu', 1000000, 50000000, 0, 24, 'Fee disepakati', NOW());
