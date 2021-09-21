<html>
    <head>
        <title>HUB HOME</title>
    </head>

    <body>
        <h1>Welcome!</h1>
        <ul>
            <?php
            $json = file_get_contents('http://hub-service/');
            $obj = json_decode($json);
            $datasets = $obj->dataset_1;
            foreach ($datasets as $entity) {
                echo "<li>$entity</li>";
            }
            ?>
        </ul>
    </body>
</html>