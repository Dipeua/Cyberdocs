# Enumerations

Lors de l'enumeration nous recherchons des données sensibles dans le code, comme des noms utilisateurs, des mots de passe, IP interne et plus encore...

Ouvrire le fichier `AndroidManifest.xml`  avec un editeur de text et regarder les elements suivantes:

### Permissions

Android vous demandera toujours d'approuver les autorisations dangereuses.

```sh
cat AndroidManifest.xml | grep "android.permission" --color
```

Some permissions that should carefully evaluate:

```
READ_SMS, SEND_SMS, RECEIVE_SMS
READ_CALL_LOG, WRITE_CALL_LOG
READ_CONTACTS, WRITE_CONTACTS
ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE
GET_ACCOUNTS
CAMERA
RECORD_AUDIO
INSTALL_PACKAGES, REQUEST_INSTALL_PACKAGES
SYSTEM_ALERT_WINDOW
```

### Application Class

L'element `<application>`, contient plusieurs  attribut. Par exemple l'un des attributs peut contenir la valeur `Init` (This means the `Init` class will run immediately when the app starts and before the user interacts)

### Network Security Configurations

This attribute refers to a file that
contains network security configurations of the app, where we can specify custom trusted Certificate Authorities, permit or deny cleartext (HTTP) trafic, and other network-related settings

```sh
cat AndroidManifest.xml | grep "android:networkSecurityConfig" --color
```

> Certificate pinning is a security measure that ensures the application is actually connecting to the intended server and not an imposter. Knowing the above configurations, the pen-tester could use the appropriate techniques to bypass this protection layer and intercept the trafic. In both cases, the tester should reconfigure the app to trust another certificate that will be used from the proxy tool to intercept the trafic


### Components

Il s'agit de l'element `<activity>`

**Activités de préférence exportées**

```sh
cat AndroidManifest.xml | grep activity | grep "android:exported" --color # if true
```

The `android:exported="true"` indicates that the activity is accessible from outside the app, meaning it can be launched by external apps or system components. 

Elle est donc accessible à toute autre application sur l'appareil (exploitez ça en analyse dynamique). 

Because of this, the activity can also be triggered by ADB.

Demarrer une activitées exposer 

```sh
adb shell am start ACTIVITY
# adb shell am start b3nac.injuredandroid/.b25lActivity
```

Another important attribute is the `<action android:name="android.intent.action.MAIN"/>` designates the activity as the main entry point of the application, the first screen launched when the user taps the app icon. Only one activity in the app should define this action

By identifying the application's entry point, the pentester gains a logical starting point for the testing process.

### Autres...

**Applications qui permettent les sauvegardes**

Considéré comme un problème de sécurité car les gens pourraient sauvegarder votre application via ADB, puis obtenir des données privées de votre application sur leur PC

```sh
cat AndroidManifest.xml | grep "activity:allowBackup" --color # if true
```

**Applications déboguables**

Activé sur l'application, ce qui permet aux rétro-ingénieurs d'y connecter plus facilement un débogueur. Cela permet de vider une trace de pile et d'accéder aux classes d'assistance de débogage. (exploitez ça en analyse dynamique). 

```sh
cat AndroidManifest.xml | grep "activity:debuggable" --color # if true
```


**Instance(s) Firebase**

Identifier les instances Firebase mal configurées.

```sh
git clone https://github.com/shivsahni/FireBaseScanner
python FireBaseScanner.py -p /path/myapp
```

```sh
git clone https://github.com/Sambal0x/firebaseEnum
pip install -r requirements
python firebaseEnum.py -k  /path/myapp
```

Exemple d'exploitation firebase:
- https://website.firebaseio.com/.json
- https://website.firebaseio.com/folder/.json



**Utilisation de la cryptographie faible ou inappropriée**

peuvent entraîner l'exposition de données sensibles, une fuite de clé, une authentification brisée, une session non sécurisée et une attaque par usurpation d'identité.

```sh
grep -r "SecretKeySpec" *
grep -rli "aes" *
grep -rli "iv"
```