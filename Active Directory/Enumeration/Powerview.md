## PowerView
[Aide-mémoire](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)


Démarrez PowerView

```sh
. .\PowerView.ps1
```

Énumérer les utilisateurs du domaine :

```sh
Get-NetUser | select cn
```

Énumérer les groupes de domaines : 

```sh
Get-NetGroup -GroupName *admin*
```

Afficher les dossiers partager

```sh
Invoke-ShareFinder
```

Affiche les systèmes d’exploitation qui fonctionne à l’intérieur du réseau

```sh
Get-NetComputer -fulldata | select operatingsystem
```