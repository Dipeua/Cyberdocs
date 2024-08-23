Désactiver la protection mémoire et compiler le programme dans un binaire ELF 32 bits.

```sh
sudo echo 0 > /proc/sys/kernel/randomize_va_space
gcc -z execstack -fno-stack-protector -m32 bof.c -o debug
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

Verifier si une stack est executable

```sh
readelf -l file
#   GNU_STACK      0x000000 0x00000000 0x00000000 0x00000 0x00000 RWE 0x4
```

---
# Buffer Overflows  x86 Techniques

1. [[ret2libc]]
2. [[shellcode]]
3. [[reverse-shell]]

