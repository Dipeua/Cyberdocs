# XML External Entity (XXE)

Il existe deux types d'attaques XXE : 
- In-Band
- Out-Band (OOB-XXE).

#Comprendre_le_XML

- XML est un langage de balisage qui définit un ensemble de règles pour encoder des documents dans un format lisible à la fois par l'homme et par la machine.

- Chaque document XML commence principalement par ce que l'on appelle `XML Prolog`: 

```xml
<?xml version="1.0" encoding:="UTF-8"?>
```

- XML permet la validation à l'aide de `DTD` et `Schema`. Cette validation garantit que le document XML est exempt de toute erreur de syntaxe.


**DTD (Document Type Definition)**

```xml
# created the note.dtd file
<!DOCTYPE note [ 
	<!ELEMENT note (to,from,heading,body)> 
	<!ELEMENT to (#PCDATA)> 
	<!ELEMENT from (#PCDATA)> 
	<!ELEMENT heading (#PCDATA)> 
	<!ELEMENT body (#PCDATA)> 
]>
```

Nous pouvons maintenant utiliser cette DTD pour valider les informations d'un document XML et nous assurer que le fichier XML est conforme aux règles de cette DTD.

```xml
# use the note.dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">  
<note>  
    <to>falcon</to>  
    <from>feast</from>  
    <heading>hacking</heading>  
    <body>XXE attack</body>  
</note>
```

