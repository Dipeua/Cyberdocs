Comment contourner : 

1. Désactivez Javascript dans votre navigateur

2. Intercepter et modifier la page entrante. En utilisant Burpsuite

3. Intercepter et modifier le téléchargement du fichiers

4. Envoyez le fichier directement au point de téléchargement.

```sh
curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" target.com
```

Pour utiliser cette méthode, vous devez d'abord intercepter un téléchargement réussi (à l'aide de Burpsuite ou de la console du navigateur) pour voir les paramètres utilisés dans le téléchargement, qui peuvent ensuite être intégrés dans la commande ci-dessus.
