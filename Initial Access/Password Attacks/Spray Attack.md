# Spray Attack

Une attaque par pulvérisation de mot de passe cible de nombreux noms d'utilisateur en utilisant un mot de passe faible commun, ce qui pourrait aider à éviter une politique de verrouillage de compte.

Pour réussir l'attaque par pulvérisation de mot de passe, nous devons énumérer la cible et créer une liste de noms d'utilisateur valides (ou une liste d'adresses e-mail).

RPD 
[RDPassSpray](https://github.com/xFreed0m/RDPassSpray)  

```sh
python3 RDPassSpray.py
```

Outlook Web Access (OWA)

- [SprayingToolkit](https://github.com/byt3bl33d3r/SprayingToolkit) (atomizer.py)
- [MailSniper](https://github.com/dafthack/MailSniper)

```sh
msf6> search owa_login
```

SMB

```sh
use auxiliary/scanner/smb/smb_login
```

SMTP

```sh
use auxiliary/scanner/smtp/smtp_enum
```
