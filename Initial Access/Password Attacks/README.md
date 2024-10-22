- [Hashcat](./Hashcat.md)
- [John](./John.md)
- [Crunch](./Crunch.md)
- [Authentication Bruteforcing](./Authentication%20Bruteforcing.md)

## Default Password
Si nous connaissons le périphérique cible, nous pouvons rechercher les mots de passe par défaut et les essayer. Listes de sites Web fournissant des mots de passe par défaut pour divers produits.

https://cirt.net/passwords
https://default-password.info/
https://datarecovery.com/rd/default-passwords/
https://wiki.skullsecurity.org/index.php?title=Passwords

## cewl

```sh
cewl -d 5 -m <length> -w output.txt https://target-website.com
```

**Générateur de nom d'utilisateur**
Il est essentiel de recueillir les noms des employés au stade du dénombrement.
Pour créer une liste avec la plupart des combinaisons possibles a base du prénom et du nom.

```sh
echo "John Smith" > users.lst
python3 username_generator.py -w users.lst
```

## Password Profiling 
Si on onnais certains détails sur une cible spécifique, tels que sa date de naissance, le nom de son animal de compagnie, le nom de son entreprise, etc., cela pourrait être un outil utile pour générer des mots de passe basés sur ces informations connues.

```sh
cupp -i
```


