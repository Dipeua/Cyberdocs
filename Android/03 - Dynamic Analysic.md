**Advenced**

Installer l'application avec adb

```c
adb install apkfile.apk
```

---

Intercepter le trafic de l'application avec Burp Suite
Installation d'une autorité de certification approuvée au niveau du système d'exploitation Android

```sh
openssl x509 -inform PEM -subject_hash -in BurpCA.pem | head -1
cat BurpCA.pem > 9a5ba580.0
openssl x509 -inform PEM -text -in BurpCA.pem -out /dev/null >> 9a5ba580.0
adb root
abd remount
adb push 9a5ba580.0 /system/etc/security/cacerts/
adb shell "chmod 644 /system/etc/security/cacerts/9a5ba580.0"
adb shell "reboot"
```

- PID Cat
Outil pour afficher les entrées de journal pour un package d'application spécifique lorsque `debug=true` est activé dans l'application.

- [[Drozer]]
C'est un cadre complet d’audit de sécurité et d’attaque pour Android.
La condition préalable est que vous ayez installé Drozer sur votre ordinateur et l'agent Drozer sur votre émulateur ou vos appareils.

Connecter:

```c
adb forward tcp:31415 tcp:31415
drozer console connect
```

Récupération des informations sur le package :

```c
run app.package.list -> see all the packages installed
```

```c
run app.package.info -a -> view package information.
```


Identifier la surface d'attaque -> activités non protégées et plus encore....

```c
run app.package.attacksurface package_name
```


Voir quelles activités peuvent être exploitées.

```c
run app.activity.info -f package_name
```


commencer  des activités sans protection  ! 

```c
run app.activity.start --component package name component_name
```



