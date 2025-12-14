# Disassembling the APK

Permet de simplement charger un APK et de regarder son code source.

## Analyzing with JADX and APKTool

**JADX**

En fait Jadx décompile l'APK en smali, puis reconvertit le smali en Java.

```sh
sudo apt install -y jadx
jadx-gui /full/path/to/myapp.apk
```

**APKTool**

```sh
apktool d myapp.apk
```

**Java Decompiler**

Convertir un APK en fichier JAR. Puis ouvrire le fichier `JAR` avec `JD-GUI` pour avoir le code Java.

```sh
d2j-dex2jar myapp.apk 
```

Apres cela nous pouvons passer a [l'enumeration](./Enumerations.md)