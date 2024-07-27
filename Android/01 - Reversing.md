Dans cette partie, nous allons extraire l'apk légitime de l'émulateur ou de l'appareil et obtenir le code source.

#Initialisation

Visualiser les appareils connecter 

```c
adb devices
```

Interagire avec l'appareil

```c
adb shell
```

---
#Extraire-apk-a-analyser 

Pour cela, vous devez avoir installé l'application sur votre appareil et connaître le nom du package.
Liste les applications installer. 

Cette commande imprime le chemin d'accès à l'APK du fichier donné

```c
adb shell pm list packages
```

Recuperer le path d'une application (le chemin vers le fichier APK)

```c
adb shell pm path PACKAGE_NAME
```

Telecharger l'APK

```c
adb pull PACKAGE_NAME.apk NEW_APP_NAME.apk
```

---
#Obtenir-le-code-source

Permet de simplement charger un APK et de regarder son code source Java. Ce qui se passe sous le capot, c'est que jADX décompile l'APK en smali, puis reconvertit le smali en Java.

```sh
jadx -d [path-output-folder] [path-apk-or-dex-file].apk|.dex
```

Convertir un APK en fichier JAR. Puis ouvrire le fichier JAR JD- GUI  pour avoir le code Java.

```c
d2j-dex2jar file.apk 
```


Récupère le code source en smali.

```c
apktool d file.apk
```