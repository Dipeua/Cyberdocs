Lister tous les formats

```sh
john --list=formats
```

Identifier les hachages:
- https://hashes.com/en/tools/hash_identifier
- `hash-id HASH`
- `hash-identifier`

Mode de fissure unique
Le contenu du `hash.txt` doit etre de la forme suivante: `USER:HASH`

```sh
john --single --format=[format] hash.txt
```

---
#rules
https://www.openwall.com/john/doc/RULES.shtml
Les attaques basées sur des règles ou attaques hybrides. Ici ont supposent que l'attaquant connaît la politique de mot de passe.

Pour voir toutes les règles disponibles

```sh
cat /etc/john/john.conf|grep "List.Rules:" | cut -d"." -f3 | cut -d":" -f2 | cut -d"]" -f1 | awk NF
```

Modifier le fichier `/etc/john/john.conf` et ajouter a la fin:

```
[List.Rules:RULE_NAME]
Az"[0-9][0-9]" ^[!@]
cAz"[0-9] [!£$%@]"
```

Ont utilise ensuite une correspondance de modèle de style regex pour définir où le mot sera modifié

`Az`- Prend le mot et l'ajoute aux caractères que vous définissez
`A0`- Prend le mot et le ajoute aux caractères que vous définissez  
`c`- Met en majuscule le personnage en position

Enfin, nous devons ensuite définir quels caractères doivent être ajoutés, préfixés ou autrement inclus. Ceux-ci suivent directement les modèles de modificateurs à l’intérieur des guillemets doubles `" "`

`[0-9]`- Comprendra les numéros 0 à 9  
`[0]`- Incluera uniquement le chiffre 0  
`[A-z]`- Comprendra à la fois les majuscules et les minuscules  
`[A-Z]`- N'inclura que des lettres majuscules  
`[a-z]`- N'inclura que des lettres minuscules  
`[a]`- Comprendra seulement un  
`[!£$%@]`- Inclura les symboles `!£$%@`

Utilisation de règles personnalisées

```sh
john --rules=RULE_NAME --wordlist=wordlist.lst hash.txt
#--stdout
```

Pour plus d'information sur les rules : https://www.openwall.com/john/doc/RULES.shtml