# Shell

Nous pouvons forcer le serveur distant soit à nous envoyer un accès en ligne de commande ([Reverse shell](./Reverse%20shell.md)), soit à ouvrir un port sur le serveur auquel nous pouvons nous connecter afin d'exécuter d'autres commandes ([Bind shell](./Bind%20shell.md)).


## TTY
Stabilisation de la coque

BASH

```sh
/usr/bin/script -qc /bin/bash /dev/null
export TERM=xterm
```

Python

```sh
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
clear
Ctrl + Z
stty raw -echo; fg
```