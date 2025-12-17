# Structure d'une APK

Le fichier Android Package Kit (APK) est le format de fichier utilisé par le système d'exploitation Android pour distribuer et installer des applications. Un APK est une archive contenant tous les composants nécessaires à l'exécution d'une application Android. 

![alt text](image.png)

## META-INF

Ce dossier est généré lors de la signature de l'application et contient des informations de vérification. Toute modification apportée au fichier APK entraînera son invalidation et il faudra le resigner. Le contenu de ce répertoire révèle les fichiers suivants.

```sh
# Contient la clé publique et la signature de CERT.SF.
CERT.RSA 

# Contient une liste de noms/hachages des lignes correspondantes dans le fichier MANIFEST.MF.
CERT.SF

# Contient une liste de noms/hachages (généralement SHA256 en Base64) pour tous les fichiers de l'APK, et est utilisé pour invalider l'APK si l'un des fichiers est modifié.
MANIFEST.MF
```

## assets

Ce dossier contient les ressources que les développeurs intègrent à l'application et qui peuvent être récupérées par l'AssetManager. Ces ressources peuvent être des images, des vidéos, des documents, des bases de données et d'autres fichiers bruts. Les applications Xamarin, Cordova et React Native utilisent également ce dossier pour enregistrer le code et les DLL.


## lib

Ce dossier contient des bibliothèques natives avec du code compilé ciblant différentes architectures d'appareils.

## res

Ce dossier contient des ressources d'application prédéfinies qui, contrairement aux fichiers d'actifs, ne peuvent pas être modifiées par l'utilisateur lors de l'exécution. Ces ressources comprennent des fichiers XML définissant les listes d'états de couleur, les mises en page d'interface utilisateur, les polices, les valeurs, les configurations pour les versions du système d'exploitation, les orientations d'écran, les paramètres réseau, etc.


## AndroidManifest.xml

Le fichier manifeste contient des métadonnées sur l'application. Il définit les attributs et composants essentiels que le système utilise pour gérer l'application

## classes.dex

Ce fichier contient toutes les classes Java (ou Kotlin) compilées au format DEX (Dalvik Executable), exécutées par l'environnement d'exécution Android (ART) sur les appareils fonctionnant sous Android 5.0 ou version ultérieure, ou par la machine virtuelle Dalvik sur les versions antérieures.


## resources.arsc

Ce fichier contient des ressources précompilées utilisées par l'application lors de son exécution.
