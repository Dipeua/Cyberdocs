> Permet d'automatiser le travail OSINT

#Started
Créera un espace de travail 

```C
workspaces create WORKSPACE_NAME
```

Commence la reconnaissance avec l'espace de travail spécifique.

```c
recon-ng -w WORKSPACE_NAME
```

---
Vérifier les noms des tables de notre base de données

```c
db schema
```

Insérer le nom de domaine `target-domain.com`dans la table des domaines

```c
db insert domains
#domain (TEXT): target-domain.com
```

---
Rechercher, installer, retirer et obtenir les informations sur les modules

```c
marketplace {search | install | remove | info} KEYWORD*
```

Travailler avec les modules installés

```c
modules search
modules {load | search} MODULE
```

Pour definir les valeurs d'une options

```C
options list
options set Name VALUES
run
```

---
### Clés

Certains modules ne peuvent pas être utilisés sans une clé pour l' API de service correspondante . `K`indique que vous devez fournir la clé de service appropriée pour utiliser le module en question.

- `keys list`liste les clés
- `keys add KEY_NAME KEY_VALUE`ajoute une clé
- `keys remove KEY_NAME`supprime une clé

Une fois l’ensemble des modules installés, vous pouvez procéder à leur chargement et à leur exécution.

- `modules load MODULE`charge un module installé
- `CTRL + C`décharge le module.
- `info`pour consulter les informations du module chargé.
- `options list`répertorie les options disponibles pour le module choisi.
- `options set NAME VALUE`
- `run`pour exécuter le module chargé.


