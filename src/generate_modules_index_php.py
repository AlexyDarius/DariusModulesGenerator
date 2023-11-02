def generate_modules_index_php(directory_path, modules_index_title, full_body_tag, main_domain):

    php_code = f'''<?php
    require $_SERVER['DOCUMENT_ROOT']. '/modules/auth/checker.php'
?>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/head.php'
?>

    <meta name="robots" content="noindex, nofollow">
    <title>{modules_index_title}</title>
    <meta name="description" content="Bienvenue sur votre gestionnaire de site web.">
</head>

{full_body_tag}

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/navbar.php'
?>

    <h1 style="text-align: center;margin-top: 12px;margin-bottom: 12px;">Bienvenue sur votre page de gestion</h1>
    <section style="margin-top: 12px;margin-bottom: 12px;">
    <!-- Put modules links here -->
        <div class="container text-muted py-4 py-lg-5">
            <div class="row">
                <div class="col text-center"><a href="https://www.{main_domain}">Revenir au site</a></div>
            </div>
        </div>
    </section>

<?php
include $_SERVER['DOCUMENT_ROOT']. '/includes/footer.php'
?>
'''

    with open(f"{directory_path}/modules/modules-index.php", "w") as php_file:
        php_file.write(php_code)
