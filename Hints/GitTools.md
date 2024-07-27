# Le référentiel GitTools contient trois outils :

**Dumper** peut être utilisé pour télécharger un .gitrépertoire exposé à partir d'un site Web si le propriétaire du site a oublié de le supprimer

**Extractor** peut être utilisé pour prendre un .gitrépertoire local et recréer le référentiel dans un format lisible. Ceci est conçu pour fonctionner en conjonction avec le Dumper, mais fonctionnera également sur le référentiel que nous avons volé sur le serveur Git. Malheureusement pour nous, alors que Extractor nous donnera chaque commit dans un format lisible, il ne triera pas les commits par date

**Finder** peut être utilisé pour rechercher sur Internet des sites avec .gitdes répertoires exposés. Ceci est nettement moins utile pour un hacker éthique, bien que cela puisse avoir des applications dans les programmes de primes de bogues

Utilisons Extractor pour obtenir un format lisible du référentiel:
```sh
extractor.sh REPO_DIR DESTINATION_DIR
```
C'est un peu déroutant, alors expliquez chaque option :

- Le `REPO_DIR` est le répertoire contenant le `.git` répertoire du référentiel. 
Notez qu'il ne s'agit pas du répertoire `.git` lui-même. 
L'extracteur recherche un répertoire `.git` dans le répertoire spécifié (c'est pourquoi nous avons dû changer le nom d'origine du répertoire en ".git")

- Le `DESTINATION_DIR` est le sous-répertoire dans lequel le référentiel sera créé

### Reconstituer l'ordre des commits
```sh
separator="======================================="; for i in $(ls); do printf "\n\n$separator\n\033[4;1m$i\033[0m\n$(cat $i/commit-meta.txt)\n"; done; printf "\n\n$separator\n\n\n"
```

Le nombre au début de ces répertoires est arbitraire et dépend de l'ordre dans lequel GitTools extrait les répertoires. Ce qui compte, c'est le hachage à la fin du nom de fichier.


## Analyse de code de site Web
Cherchons les fichiers PHP:
```php
find . -name "*.php"
```

