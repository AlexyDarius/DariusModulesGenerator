def generate_auth_php(directory_path, main_domain):

    php_code = f'''<?php
session_start();

// Replace these with your actual username and password
$valid_username = 'username';
$hashed_password = password_hash('password', PASSWORD_DEFAULT);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {{
    $entered_username = $_POST['username'];
    $entered_password = $_POST['password'];

    if ($entered_username === $valid_username && password_verify($entered_password, $hashed_password)) {{
        $_SESSION['authenticated'] = true;
        $_SESSION['username'] = $entered_username; // Set the username in the session
        header('Location: "https://www.{main_domain}/modules/modules-index.php"'); // Redirect to the opening hours editing page
        exit;
    }} else {{
        // Authentication failed
        echo "Authentication failed. Please try again.";
    }}
}}
?>
'''

    with open(f"{directory_path}/modules/auth/auth.php", "w") as php_file:
        php_file.write(php_code)
