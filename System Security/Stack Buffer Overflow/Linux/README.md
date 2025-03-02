Désactiver la protection mémoire et compiler le programme dans un binaire ELF 32 bits.

```sh
sudo echo 0 > /proc/sys/kernel/randomize_va_space
gcc -z execstack -fno-stack-protector -m32 bof.c -o debug

file debug | tr "," "\n"
```

Rendre la syntaxe en `Intel`

```sh
echo 'set disassembly-flavor intel' > ~/.gdbinit
```


Verifier si la stack est executable

```sh
readelf -l file
#   GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RWE 0x4
```

Les fonctions C vulnérables:

```c
strcpy
gets
sprintf
scanf
strcat
...
```

## Buffer Overflows  x86 Techniques

1. [shellcode](./Stack/shellcode.md)
2. [ret2libc](./Stack/ret2libc.md)
3. [reverse shell](./Stack/reverse-shell.md)

