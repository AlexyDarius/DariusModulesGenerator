def generate_checker_php(directory_path, main_domain):

    php_code = f'''<?php

session_start();
if (!isset($_SESSION['authenticated']) || !$_SESSION['authenticated']) {{
    header('Location: https://www.{main_domain}/modules/login.php'); // Redirect to the login page if not authenticated
    exit;
}}

?>
'''

    with open(f"{directory_path}/modules/auth/checker.php", "w") as php_file:
        php_file.write(php_code)
