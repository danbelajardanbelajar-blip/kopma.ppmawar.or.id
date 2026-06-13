<?php
class Helper {
    public static function formatRupiah($amount) {
        return "Rp " . number_format($amount, 0, ',', '.');
    }

    public static function sanitize($input) {
        if (is_array($input)) {
            foreach ($input as $k => $v) {
                $input[$k] = self::sanitize($v);
            }
            return $input;
        }
        return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
    }

    public static function generateMemberCode($lastId = 0) {
        $year = date('Y');
        $nextId = $lastId + 1;
        return "ANG-" . $year . "-" . str_pad($nextId, 4, '0', STR_PAD_LEFT);
    }

    public static function timeAgo($datetime) {
        $time = strtotime($datetime);
        $diff = time() - $time;
        
        if ($diff < 60) return "Baru saja";
        if ($diff < 3600) return floor($diff / 60) . " menit lalu";
        if ($diff < 86400) return floor($diff / 3600) . " jam lalu";
        if ($diff < 2592000) return floor($diff / 86400) . " hari lalu";
        if ($diff < 31536000) return floor($diff / 2592000) . " bulan lalu";
        return floor($diff / 31536000) . " tahun lalu";
    }

    public static function truncate($text, $length = 150) {
        if (strlen($text) <= $length) return $text;
        return substr($text, 0, strrpos(substr($text, 0, $length), ' ')) . '...';
    }

    public static function slugify($text) {
        $text = preg_replace('~[^\pL\d]+~u', '-', $text);
        $text = iconv('utf-8', 'us-ascii//TRANSLIT', $text);
        $text = preg_replace('~[^-\w]+~', '', $text);
        $text = trim($text, '-');
        $text = preg_replace('~-+~', '-', $text);
        $text = strtolower($text);
        if (empty($text)) return 'n-a';
        return $text;
    }

    public static function uploadImage($file, $directory) {
        if ($file['error'] !== UPLOAD_ERR_OK) {
            return false;
        }

        if ($file['size'] > MAX_FILE_SIZE) {
            return false;
        }

        $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        $mimeType = finfo_file($finfo, $file['tmp_name']);
        finfo_close($finfo);

        if (!in_array($mimeType, $allowedTypes)) {
            return false;
        }

        $extension = pathinfo($file['name'], PATHINFO_EXTENSION);
        $filename = uniqid() . '.' . $extension;
        $target = rtrim($directory, '/') . '/' . $filename;

        if (!is_dir(dirname($target))) {
            mkdir(dirname($target), 0777, true);
        }

        if (move_uploaded_file($file['tmp_name'], $target)) {
            return $filename;
        }

        return false;
    }
}
