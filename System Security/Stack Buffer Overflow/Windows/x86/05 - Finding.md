# Finding Bad Characters
- Permet de savoir quel caractere est ideal pour notre shellcode ou non
- Ce qui peut se faire en executant tous les caracteres hexadecimaux dans notre programme et voir si l'un d'eux agit.

- Par defaut l'octect null `\x00` agit

https://bulbescurity.com/finding-bad-characters-with-immunity-debuger-and-mona-py/

```c
badchars = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
```

```c
for x in range(1, 256):
  print("\\x" + "{:02x}".format(x), end='')
```

- Qui vas executer tout les mauvais caractere et nous retourne celle que nous ne devons pas utiliser

sur le registrre ESP -> click droit -> follow in dump [dans Immunity debuger]


###0 Finding the Right Module
- C'est rechercher une DLL ou quelque chose similaire a l'interieur d'un programme qui n'a pas de protection de memoire ce qui signifie pas de DAP, pas de profondeur ASLR.

- Pour cela on vas utiliser un module appeler "mona.py" qui permet de voir la protection des proccess
https://github.com/corelan/mona

- Demarrer immunity debugger sans le lancer, sur la barre de rechercher taper `!mona modules` pour lister les modules. 

- Ce qui nous interesse est celle avec une protection `False` et rattacher au serveur vulnerable.

- Pour trouver reellement l'opcode (qui est un 'saut')
`msf-nasm_shell> JMP ESP` qui est une commande de saut que l'on vas utiliser comme pointeur qui vas sauter vers notre shellcode. 

- On peut utiliser le resultat de 'msf-nasm_shell' et aller dans immunity taper: `!mona find -s "\xff\xe4" -m essfunc.dll` le fichier dll qui a le modules avec aucune protection activer.

- Ce qui est interesent ici est la addresse retourner [Results] que nous pouvons tester et voir quel fonctionne
Avec cette address on peut modifier notre script et remplacer la partie `"B"*4` par le caractere inverse trouver dans debugger: (<---)

Dans debugger:
- Rechercher l'adresse de retour trouver dans [Results]
- `F2` pour mettre un breakpoints

Lancer le script

- Dans l'EIP on obtient exactement la meme adresse de retour trouver dans [Results] ce qui signifie que on controle l'EIP et nous pouvons generer notre shell code.