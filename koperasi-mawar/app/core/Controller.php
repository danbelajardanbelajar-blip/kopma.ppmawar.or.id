<?php
class Controller {
    public function view($view, $data = []) {
        if (file_exists(APP_ROOT . '/app/views/' . $view . '.php')) {
            extract($data);
            require_once APP_ROOT . '/app/views/' . $view . '.php';
        } else {
            die("View does not exist: " . $view);
        }
    }

    public function model($model) {
        if (file_exists(APP_ROOT . '/app/models/' . $model . '.php')) {
            require_once APP_ROOT . '/app/models/' . $model . '.php';
            return new $model();
        }
        die("Model does not exist: " . $model);
    }

    public function redirect($url) {
        header('Location: ' . BASE_URL . $url);
        exit;
    }

    public function json($data) {
        header('Content-Type: application/json');
        echo json_encode($data);
        exit;
    }
}
