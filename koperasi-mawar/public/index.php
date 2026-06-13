<?php
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
