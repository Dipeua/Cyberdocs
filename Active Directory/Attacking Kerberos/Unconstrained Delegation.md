# Unconstrained Delegation

Comment abuser de la délégation complète afin de récupérer le TGT d’un utilisateur, nous permettant ainsi de nous authentifier auprès de n’importe quel service en son nom.

# Exploitation

Cela signifie que maintenant, avec ces informations, le service peut demander n’importe quel ticket de service au nom de l’utilisateur. Je répète : il peut demander n’importe. quel. ticket de service. au nom de l’utilisateur. Il peut se faire passer pour l’utilisateur pour s’authentifier auprès de n’importe quel service.

Ainsi, les comptes ayant la délégation complète sont des cibles prioritaires pour les attaquants, puisqu’une fois un de ces comptes compromis, il suffit d’attendre des authentifications d’utilisateurs pour pouvoir s’authentifier n’importe où en leur nom.

# Exemple

Il y a ici la machine `WEB-SERVER-01`  qui est en “Unconstrained Delegation” sur le domaine `dom.local`

Il est possible de s’authentifier auprès de cette machine pour utiliser ses partages réseau. Nous imaginons qu’un attaquant ait réussi à compromettre cette machine, et qu’il est administrateur local de cette machine.

L’attaquant doit alors attendre qu’un utilisateur à privilèges se connecte sur la machine. 
Il va donc monitorer les connexions et inspecter les tickets de service afin de voir si un TGT est présent dans l’un deux.

Pour cela, il utilise l’outil `Rubeus` ou `kekeo`

```
Rubeus monitor /interval:5
```

Il se trouve qu’à un moment donné, le compte support-account, administrateur de domaine, doit aller voir quelque chose sur le disque dur de `WEB-SERVER-01`. Pour cela, il se connecte au partage réseau du serveur `\\WEB-SERVER-01\c$.`

Cette connexion est détectée par Rubeus
Comme cette machine est en “Unconstrained Delegation”, le ticket de service envoyé par l’administrateur de domaine contient une copie de son TGT, copie qui va être extrait par Rubeus.

Maintenant en possession du TGT d’un administrateur de domaine (encodé en base 64), l’attaquant peut demander un ticket de service pour utiliser le service LDAP du contrôleur de domaine `DC-01`. 

```
Rubeus.exe asktgs /ticket:<ticket en base64> /service:ldap/dc-01.dom.local /ptt
```

Tout fonctionne comme prévu.
Nous pouvons vérifier la présence du ticket de service en mémoire, pour l’utilisateur  (puisque l’attaquant a utilisé son TGT), et pour le service LDAP du contrôleur de domaine.

```
klist
```

Avec ce ticket de service, il est possible de demander au contrôleur de domaine de se synchroniser avec l’attaquant.

Ici, l’attaquant a uniquement demandé de synchroniser le compte krbtgt en vue de faire un “Golden Ticket” avec `mimikatz`

```
lsadump::dcsync /dc:dc-01.dom.local /domain:dom.local /user:krbtgt
```


Avec le hash NT du compte krbtgt, l’attaquant peut tout faire sur l’Active Directory.