# Structure d'une APK

- `AndroidManifest.xml` : le fichier de configuration manifeste au format XML binaire .

- `META-INF/` : dossier contenant le fichier `MANIFEST.MF`, qui stocke les métadonnées sur le contenu du JAR. qui sera parfois stocké dans un dossier nommé original. La signature de l'APK est également stockée dans ce dossier.

- `Assets/`: dossier optionnel contenant les actifs des applications, qui peuvent être récupérés par AssetManager.

- `resources.arsc` : fichier contenant les ressources applicatives précompilées, en XML binaire .

- `lib/` : dossier optionnel contenant du code compilé - c'est à dire des bibliothèques de code natif.

- `classes.dex` : code d'application compilé au format dex.

- `res/`: dossier contenant des ressources non compilées dans resources.arsc
