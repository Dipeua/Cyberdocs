
#Enumeration 
Avant cree notre phishlets nous devons enumerer la cible.

Aller dans la page de connexion du site cible et cree un compte, 
Une foie le compte cree connectez vous et recuperer les informations suivantes :

- Les requestes HTTP (donnees envoyer en POST)

Une fois tout information en main, faite une copie de `example.yaml` pour votre compagne

- `proxy_hosts`: Contient la liste de tout les domaines que le site cible a besoin pour faire un proxy inverse cela inclu les sous-domaines et bien d'autres
	- `domain`: Contient le domain principale
	- `phish_sub` - `orig_sub`: Contiennent les sous-domain lier au domain principale
	- `session:true`: indique le domain contient des cookies de sessions
	- `is_landing:true`: permet de rediriger un utlisateur vers la page d'origine

- `credentials`: Se sont les informations  (data) une fois connecter. qui sont generalement des noms utiliser dans les champs de formulaire

- `auth_tokens`
	- `domain`: le domain du **cookiee** responsable de l'authentification
	- `keys`: les noms des cookies a capturer

- `login`: les informations ou envoyer notre campage
	- `domain`: Contient le domain connection ceci peut etre un sous-domain aussi comment `login.target.com`
	- `path`: le chemin URL de login du site cible

[[Catching Phish]]