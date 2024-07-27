#### Liste de refus ou liste noire (Deny List)
C'est l'endroit où toutes les demandes sont acceptées, à l'exception des ressources spécifiées dans une liste ou correspondant à un modèle particulier. 

Ce filtre peur etre contourner à l'aide des techniques suivantes : 

1. En utilisant d'autres références localhost telles que :

```
0
0.0.0.0
0000
127.1
127.*.*.*
2130706433
017700000001
```

ou des sous-domaines qui ont un enregistrement DNS qui correspond à l'adresse IP 

```
127.0.0.1.
127.0.0.1.ghi
127.0.0.1.nip.io.

#Cloud
169.254.169.254
```

2. Enregistrez son propre nom de domaine qui se résout en `127.0.0.1`. Collaborator de Burp Suite fait bien cela.
3. Masquez les chaînes bloquées à l'aide du double encodage d'URL ou de la variation de casse.
4.  Fournissez une URL que vous contrôlez, qui redirige vers l'URL cible. Essayez d'utiliser différents codes de redirection, ainsi que différents protocoles pour l'URL cible (`http` et `https`)
5. Tranverse de chemin avec `x/../path`

---
#### Liste d'autorisation ou liste blanche (Allow List)
C'est l'endroit où toutes les demandes sont refusées à moins qu'elles n'apparaissent sur une liste ou ne correspondent à un modèle particulier.

Comme une règle selon laquelle une URL utilisée dans un paramètre doit commencer par  `https://website.com`

Ce filtre peur etre contourner à l'aide des techniques suivantes : 

1. En créant un sous-domaine sur le nom de domaine d'un attaquant, tel que :

```
https://website.com.attacker-domain.com
```

2. Intégrer des informations d'identification dans une URL avant le nom d'hôte

```
https://username@website.com
```

3. Indiquer un fragment d'URL

```
https://username#@website.com
```

4. Exploiter la hiérarchie de dénomination DNS pour placer les données requises dans un nom DNS complet que vous contrôlez

```
https://attacker.com.website.com
```

5. **Utiliser des combinaisons de ces techniques ensemble.**

---
#### Open Redirect
C'est un point de terminaison sur le serveur où le visiteur du site Web est automatiquement redirigé vers une autre adresse de site Web comme `https://website.com/link?url=https://google.com`

La fonctionnalité peut eter utiliser pour rediriger la requête HTTP interne vers un domaine de son choix.

```
https://website.com/link?url=https://127.0.0.1/api/users
```

> Utiliser le path de l'open redirect dans le parametre vulnerable au SSRF


