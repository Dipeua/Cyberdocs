# Server-Side Request Forgery (SSRF)
Vulnérabilité qui permet à un attaquant de forcer l'application côté serveur à effectuer des requêtes vers un emplacement non prévu permettant d'accéder aux ressources internes du serveur.

###### Attaques SSRF courantes

- Contre le serveur lui-meme: `localhost`
- Contre d'autres systèmes back-end: `qui sont des adresses IP privées non routables` `192.168.x.x`

---
**Ou chercher une SSRF ?**
- Lorsqu'une URL complète est utilisée dans un paramètre dans les requetes `GET` ou `POST`

```http
http://website.com/page?param=http://website.com/store
```

- Un champ caché dans un formulaire

```html
<balise attribut="http://website.com/store">
```

- Une URL partielle telle que uniquement le nom d'hôte

```http
http://website.com/page?param=api
```

- Ou peut-être seulement le chemin de l'URl

```http
http://website.com/page?param=/api/user
```

- Dans l'en-tête `Referer`

```http
GET / HTTP/1.1
Referer: http://website.com/
```

---
Ajoutez `&x=` à la fin pour empêcher le chemin restant d'être ajouté à la fin de l'URL de l'attaquant et la transforme à la place en paramètre (?x=) sur la chaîne de requête.

```http
http://website.com/stock?server=api&id=123
http://website.com/stock?server=api.website.com/api/user&x=&id=123
```

