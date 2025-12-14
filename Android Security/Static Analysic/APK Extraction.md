# APK Extraction

Using [APK Export](https://apkcombo.com/) an Android application that automatically extracts the APK file of any app installed on the device and saves it locally.

## Extracting The APK From The Device

Pour cela, vous devez avoir installé l'application sur votre appareil et connaître le nom du package.

> APKs are typically located in the directory `/data/app/<package-name>-1/base.apk`. For example, if the package name is `com.example.myapp`, the path would likely be `/data/app/com.example.myapp-1/base.apk`.

Liste les applications installer. 

```sh
adb shell pm list packages
# adb shell pm list packages | grep myaap
```

Recuperer le path d'une application (le chemin vers le fichier APK)

```sh
adb shell pm path <PACKAGE_NAME>
# adb shell pm path com.example.myapp
```

Telecharger l'APK

```sh
adb pull <PACKAGE_NAME>.apk NEW_APP_NAME.apk
# adb pull /data/app/com.example.myapp-1/base.apk myapp.apk
```

Une fois l'application extraite nous pouvons la [Disassembler](./Disassembling%20the%20APK.md)

