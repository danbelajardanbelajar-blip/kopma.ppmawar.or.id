<?php
class App {
    protected $controller = 'HomeController';
    protected $method = 'index';
    protected $params = [];

    public function __construct() {
        $url = $this->parseUrl();

        // Check controller
        $controllerName = isset($url[0]) ? str_replace('-', '', ucwords($url[0], '-')) . 'Controller' : $this->controller;
        if (file_exists(APP_ROOT . '/app/controllers/' . $controllerName . '.php')) {
            $this->controller = $controllerName;
            unset($url[0]);
        }

        require_once APP_ROOT . '/app/controllers/' . $this->controller . '.php';
        $this->controller = new $this->controller;

        // Check method
        if (isset($url[1])) {
            $methodName = lcfirst(str_replace('-', '', ucwords($url[1], '-')));
            if (method_exists($this->controller, $methodName)) {
                $this->method = $methodName;
                unset($url[1]);
            }
        }

        // Setup params
        $this->params = $url ? array_values($url) : [];

        // Call method
        call_user_func_array([$this->controller, $this->method], $this->params);
    }

    public function parseUrl() {
        if (isset($_GET['url'])) {
            $url = rtrim($_GET['url'], '/');
            $url = filter_var($url, FILTER_SANITIZE_URL);
            $url = explode('/', $url);
            return $url;
        }
        return [];
    }
}
