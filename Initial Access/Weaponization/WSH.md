WSH (Windows Scripting Host) L'hôte de script Windows est un outil d'administration Windows intégré qui exécute des fichiers de commandes pour automatiser et gérer les tâches au sein du système d'exploitation.

Il s'agit d'un moteur natif Windows, `cscript.exe`  (pour les scripts de ligne de commande) et `wscript.exe`  (pour les scripts d'interface utilisateur), qui sont responsables de l'exécution de divers scripts Microsoft Visual Basic (VBScript), notamment `vbs`  et `vbe` .

Utilisons maintenant le VBScript `payload.vbs` pour exécuter des fichiers exécutables.

```js
Set shell = WScript.CreateObject("Wscript.Shell")
shell.Run("C:\Windows\System32\calc.exe " & WScript.ScriptFullName),0,True
```

```c
wscript c:\Temp\payload.vbs
```


Si les fichiers VBS sont sur la liste noire, nous pouvons alors renommer le fichier `.vbs` en  `.txt` et l'exécuter comme suit :

```js
wscript /e:VBScript c:\Temp\payload.txt
```
