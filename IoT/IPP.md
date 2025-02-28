Internet Printing Protocol (IPP) tourne sur le port 631, spécialisé pour la communication entre les périphériques clients et les imprimantes.

Lorsqu'un port IPP est ouvert sur Internet, il est possible pour n'importe qui d'imprimer sur l'imprimante ou même de transférer des données malveillantes. Cela peut exposer de nombreuses informations sensibles telles que le nom de l'imprimante, l'emplacement, le modèle, la version du micrologiciel ou même le SSID Wi-Fi de l'imprimante.

La plupart d'entre eux semblent exécuter le serveur CUPS (qui est un simple système d'impression UNIX).

## Exploitation 

```sh
git clone https://github.com/RUB-NDS/PRET
```

1. ps (Postscript)
2. pjl (Printer Job Language)
3. pcl (Printer Command Language)

> Vous devez essayer les trois langues juste pour voir laquelle sera comprise par l'imprimeur.

```sh
python pret.py 192.168.x.x pjl
python pret.py laserjet.lan ps
python pret.py /dev/usb/lp0 pcl
```

(La dernière option fonctionne si vous avez déjà une imprimante connectée à votre ordinateur)

