# Yara
Yara peut identifier des informations basées sur des `modèles binaires` et `textuels` dans un fichier.

> Par exemple, les règles Yara sont fréquemment écrites pour déterminer si un fichier est malveillant ou non, en fonction des fonctionnalités (ou modèles) qu'il présente.


## Yara Rules

> Votre règle n'est efficace que si vous comprenez les modèles que vous souhaitez rechercher.
> 
> Chaque règle doit avoir un nom et une condition.


**Anatomie d'une règle Yara**

![](../Fundamentals/Cyber%20Defence%20Frameworks/Images/yara.png)

Créez un fichier nommez : `myrules.yar`:

```sh
rule examplerule {
    meta:
        author = "Dipeua"
        description = "Demo"
    
    strings:
        pseudo = "Ber1y"
        skill = "Jr Analyste"

    condition: true
    
}
```

Executer une règles yara
```sh
yara myrules.yar somedirectory
yara myrules.yar somefile
```

-  [Les conditions](https://yara.readthedocs.io/en/stable/writingrules.html)
- [Aide mémoire](https://medium.com/malware-buddy/security-infographics-9c4d3bd891ef#18dd)

## Modules Yara

Des frameworks suivant permettent d'améliorer la technicité des règles Yara :

- [Cuckoo Sandbox](https://cuckoosandbox.org/) : Environnement d'analyse automatisé des programmes malveillants. permet de générer des règles Yara basées sur les comportements découverts à partir de Cuckoo Sandbox.

- [Python PE](https://pypi.org/project/pefile/) : Permet de créer des règles Yara à partir des différentes sections et éléments de la structure Windows Portable Executable (PE).


## Outils Yara

- [Loki](https://github.com/Neo23x0/Loki/blob/master/README.md) est un scanner IOC 

```sh
python loki.py --update
python loki.py -p .
```

- [THOR Lite](https://www.nextron-systems.com/thor-lite/) est aussi scanner IOC mais utilise mois de ressources CPU

- [Fenrir](https://github.com/Neo23x0/Fenrir)

- [YaYa](https://www.eff.org/deeplinks/2020/09/introducing-yaya-new-threat-hunting-tool-eff-threat-lab) Gére plusieurs référentiels de règles YARA, puis permet aux chercheurs d'ajouter leurs propres règles, de désactiver les autres.

- [yarGen](https://github.com/Neo23x0/yarGen) est un générateur de règles YARA

> Le principe est la création de règles Yara à partir de chaînes trouvées dans les fichiers de logiciels malveillants.

Générer une règle Yara pour file2

```sh
python3 yarGen.p --update
python3 yarGen.py -m /home/cmnatic/suspicious-files/file2 --excludegood -o /home/cmnatic/suspicious-files/file2.yar
```

- [yarAnalyzer](https://github.com/Neo23x0/yarAnalyzer/)

-  [Valhalla](https://www.nextron-systems.com/valhalla/) est un flux Yara en ligne

# Ressources

Lectures complémentaires sur la création de règles Yara et l’utilisation de yarGen

- [https://www.bsk-consulting.de/2015/02/16/write-simple-sound-yara-rules/](https://www.bsk-consulting.de/2015/02/16/write-simple-sound-yara-rules/)      
- [https://www.bsk-consulting.de/2015/10/17/how-to-write-simple-but-sound-yara-rules-part-2/](https://www.bsk-consulting.de/2015/10/17/how-to-write-simple-but-sound-yara-rules-part-2/)
- [https://www.bsk-consulting.de/2016/04/15/how-to-write-simple-but-sound-yara-rules-part-3/](https://www.bsk-consulting.de/2016/04/15/how-to-write-simple-but-sound-yara-rules-part-3/)

