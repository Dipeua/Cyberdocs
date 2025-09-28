# Organization

Lors de l'organisation de nos activités ou de celles de toute une équipe, nous devons veiller à respecter une procédure précise. Chacun doit savoir où il se situe et où chaque membre intervient tout au long du processus de test d'intrusion. Il est également essentiel d'avoir une compréhension commune des activités de chaque membre. Sinon, des éléments risquent de se retrouver dans le mauvais sous-répertoire, ou des preuves nécessaires à la création de rapports pourraient être perdues ou corrompues.

## Gestionnaire de mots de passe

- [1Password](https://1password.com/)
- [LastPass](https://www.lastpass.com/)
- [Keeper](https://www.keepersecurity.com/)
- [Bitwarden](https://bitwarden.com/)
- [Proton Pass](https://proton.me/pass)

## Prise de notes

- [Notion.so](https://notion.so/)
- Anytype
- [Obsidian](https://obsidian.md/)
- [Xmind](https://xmind.com/) éditeur de cartes mentales qui peut très bien visualiser les composants et processus d'informations pertinents

For Pentest Report Generator

- [GhostWriter](https://github.com/GhostManager/Ghostwriter) et [Pwndoc](https://github.com/pwndoc/pwndoc) nous permettent de générer notre documentation et d'avoir une vue d'ensemble claire des étapes réalisées.

**Journalisation**

La journalisation est essentielle à la fois pour la documentation et pour notre protection. Si des tiers attaquent l'entreprise pendant notre test d'intrusion et que des dommages surviennent, nous pouvons prouver que ces dommages ne résultent pas de nos activités. Pour cela, nous pouvons utiliser les outils `script` et `date`. 

Date pour afficher la date et l'heure exactes de chaque commande dans notre ligne de commande. Grâce à script, chaque commande et son résultat sont enregistrés dans un fichier d'arrière-plan. Pour afficher la date et l'heure, nous pouvons remplacer la variable `PS1` de notre fichier `.bashrc` par le contenu suivant.

```sh
PS1="\[\033[1;32m\]\342\224\200\$([[ \$(/opt/vpnbash.sh) == *\"10.\"* ]] && echo \"[\[\033[1;34m\]\$(/opt/vpnserver.sh)\[\033[1;32m\]]\342\224\200[\[\033[1;37m\]\$(/opt/vpnbash.sh)\[\033[1;32m\]]\342\224\200\")[\[\033[1;37m\]\u\[\033[01;32m\]@\[\033[01;34m\]\h\[\033[1;32m\]]\342\224\200[\[\033[1;37m\]\w\[\033[1;32m\]]\n\[\033[1;32m\]\342\224\224\342\224\200\342\224\200\342\225\274 [\[\e[01;33m\]$(date +%D-%r)\[\e[01;32m\]]\\$ \[\e[0m\]"
```

Pour démarrer la journalisation avec script(sous Linux) et Start-Transcript (sous Windows), nous pouvons utiliser la commande suivante

```sh
$ script 03-21-2021-0200pm-exploitation.log
$ <ALL THE COMMANDS>
$ exit
```

```sh
C:\> Start-Transcript -Path "C:\Pentesting\03-21-2021-0200pm-exploitation.log"

Transcript started, output file is C:\Pentesting\03-21-2021-0200pm-exploitation.log

C:\> ...SNIP...
C:\> Stop-Transcript
```

-  Nous pouvons utiliser une application appelée [Peek](https://github.com/phw/peek) pour créer des GIF qui enregistrent toutes les actions nécessaires.