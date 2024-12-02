> Se fait sans exécuter le programme, qu'allons-nous identifier ?

- Utilisation faible ou inappropriée de la cryptographie
- Activités de préférence exportées
- Applications qui permettent les sauvegardes
- Applications déboguables
- Autorisations des applications.
- Instance(s) Firebase
- Données sensibles dans le code
- Les cles API Secret
- Les stockage S3 Bucket

**AndroidManifest.xml**

C'est l'endroit ou est defini la base de l'application elle peut contenir des elements comme:
- minSDKVersion
- Permissions
- Activities: les activites a proteger son:
	- Account Details
	- Money Transfer Screens
	- Hidden Screen
- Content Providers

## Quoi chercher?
Données sensibles dans le code
Ont peut trouver noms d'utilisateurs, des mots de passe, IP interne et plus encore...


 - Utilisation de la cryptographie faible ou inappropriée
peuvent entraîner l'exposition de données sensibles, une fuite de clé, une authentification brisée, une session non sécurisée et une attaque par usurpation d'identité.

```sh
grep -r "SecretKeySpec" *
grep -rli "aes" *
grep -rli "iv"
```

---

- Activités de préférence exportées
Lorsqu'une activité est partagée avec d'autres applications sur l'appareil, elle est donc accessible à toute autre application sur l'appareil (exploitez ça en analyse dynamique). 

```sh
cat AndroidManifest.xml | grep activity | grep "android:exported" --color # if true
```

---

- Applications qui permettent les sauvegardes
Considéré comme un problème de sécurité car les gens pourraient sauvegarder votre application via ADB, puis obtenir des données privées de votre application sur leur PC

```sh
cat AndroidManifest.xml | grep "activity:allowBackup" --color # if true
```

---

- Applications déboguables
Activé sur l'application, ce qui permet aux rétro-ingénieurs d'y connecter plus facilement un débogueur. Cela permet de vider une trace de pile et d'accéder aux classes d'assistance de débogage. (exploitez ça en analyse dynamique). 

```sh
cat AndroidManifest.xml | grep "activity:debuggable" --color # if true
```

---

- Autorisations d'application.
Android vous demandera toujours d'approuver les autorisations dangereuses.

```sh
cat AndroidManifest.xml | grep "android.permission" --color
```

---

- Instance(s) Firebase
Les scripts aident les analystes de sécurité à identifier les instances Firebase mal configurées.

```sh
git clone https://github.com/shivsahni/FireBaseScanner
python FireBaseScanner.py -p /path/apk
```

```sh
git clone https://github.com/Sambal0x/firebaseEnum
pip install -r requirements
python firebaseEnum.py -k  /path/apk
```

Exemple d'exploitation firebase:

```http
https://website.firebaseio.com/.json
https://website.firebaseio.com/folder/.json
```

---

- Demarrer une activitées exposer
 
```c
adb shell am start ACTIVITY
# adb shell am start b3nac.injuredandroid/.b25lActivity
 ```

