<?php
class Auth {
    public static function isLoggedIn() {
        return isset($_SESSION['user_id']);
    }

    public static function isAdmin() {
        return self::isLoggedIn() && $_SESSION['role'] === 'admin';
    }

    public static function isMember() {
        return self::isLoggedIn() && $_SESSION['role'] === 'member';
    }

    public static function requireLogin() {
        if (!self::isLoggedIn()) {
            Flash::set('error', 'Anda harus login terlebih dahulu.');
            header('Location: ' . BASE_URL . '/auth/login');
            exit;
        }
    }

    public static function requireAdmin() {
        self::requireLogin();
        if (!self::isAdmin()) {
            Flash::set('error', 'Akses ditolak. Halaman khusus admin.');
            header('Location: ' . BASE_URL . '/');
            exit;
        }
    }

    public static function requireMember() {
        self::requireLogin();
        if (!self::isMember()) {
            Flash::set('error', 'Akses ditolak. Halaman khusus anggota.');
            header('Location: ' . BASE_URL . '/');
            exit;
        }
    }

    public static function getCurrentUser() {
        if (self::isLoggedIn()) {
            return [
                'id' => $_SESSION['user_id'],
                'name' => $_SESSION['name'],
                'role' => $_SESSION['role']
            ];
        }
        return null;
    }

    public static function login($user) {
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['name'] = $user['name'];
        $_SESSION['role'] = $user['role'];
    }

    public static function logout() {
        session_unset();
        session_destroy();
    }
}
