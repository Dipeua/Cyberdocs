# Structure d'une APK

- `AndroidManifest.xml` : le fichier de configuration manifeste au format XML binaire .

- `META-INF/` : dossier contenant le fichier `MANIFEST.MF`, qui stocke les métadonnées sur le contenu du JAR. qui sera parfois stocké dans un dossier nommé original. La signature de l'APK est également stockée dans ce dossier.

- `Assets/`: dossier optionnel contenant les actifs des applications, qui peuvent être récupérés par AssetManager.

- `resources.arsc` : fichier contenant les ressources applicatives précompilées, en XML binaire .

- `lib/` : dossier optionnel contenant du code compilé - c'est à dire des bibliothèques de code natif.

- `classes.dex` : code d'application compilé au format dex.

- `res/`: dossier contenant des ressources non compilées dans resources.arsc

> Lorsque vous créez un code d'application, le fichier apk contient un fichier .dex, qui contient le bytecode binaire Dalvik. 

> Smali est un langage assembleur qui s'exécute sur Dalvik VM, qui est la JVM d'Android.

## The Mobile Application Penetration Testing Process

- [Information Gathering (Google Play Store)](./00%20-%20Information%20Gathering%20(Google%20Play%20Store).md)

- [Static Analysic](./02%20-%20Static%20Analysic.md)

- [Dynamic Analysic](./03%20-%20Dynamic%20Analysic.md)

- Reporting


**Lien**

- [OWASP Mobile Application Pentesting Gitbook](https://mobile-security.gitbook.io/mobile-security-testing-guide/overview/0x03-overview)

- [OWASP Mobile Top 10](https://owasp.org/www-project-mobile-top-10)

- [APK Deguard](http://apk-deguard.com/)