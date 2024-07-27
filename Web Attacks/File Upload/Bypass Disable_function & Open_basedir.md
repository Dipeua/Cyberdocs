Les fonctions telles que `system()` ou `shell_exec()`sont souvent désactivées via les directives PHP définies dans le fichier de configuration `php.ini`. 

D'autres fonctions, peut-être moins connues sous le nom de `dl()` peuvent passer inaperçues auprès de l'administrateur système et ne pas être désactivées. 

Grâce à la fonction `putenv()`, nous pouvons modifier les variables d'environnement, nous permettant d'attribuer la valeur souhaitée à la variable `LD_PRELOAD`

L'outil #chankro nous permet d'échapper aux `Disable_functions` et `open_basedir`
https://www.tarlogic.com/es/blog/evadir-disable_functions-open_basedir/

```sh
python chankro.py --arch 64 --input c.sh --output tryhackme.php --path /var/www/html
```

#Remember
Dans le fichier `phpinfo.php` regarder les options suivantes:
- disable_functions
- SCRIPT_FILENAME

```sh
python chankro.py --arch 64 --input c.sh --output tryhackme.php --path SCRIPT_FILENAME + uploads
```

