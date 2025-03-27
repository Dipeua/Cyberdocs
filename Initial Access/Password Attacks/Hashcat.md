# Hashcat

- `?d` indique à hashcat d'utiliser un chiffre

## Dictionnaire

Une attaque par dictionnaire est une technique utilisée pour deviner des mots de passe en utilisant des mots ou des expressions bien connus.

```sh
hashcat -a 0 -m <mode> hash.txt wordlist.lst
```

## Brute Force 

Le forçage brutal est une attaque courante utilisée par l'attaquant pour obtenir un accès non autorisé à un compte personnel. 

```sh
hashcat -a 3 -m <mode> hash.txt wordlist.lst
```

```sh
hashcat -a 3 -m 0 05A5CF06982BA7892ED2A6D38FE832D6 ?d?d?d?d
```

