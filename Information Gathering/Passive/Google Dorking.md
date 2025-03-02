- https://www.exploit-db.com/google-hacking-database/
- https://www.google.com/advanced_search
- https://archive.org/web/
- https://tineye.com/

PDF documents in a specific site or domain can be searched

```c
site:example.com filetype:pdf
```

References to email addresses of a specific domain, excluding the domain's site

```c
"@example" -site:example.com
```

Administrative sites with the word admin in the title or the URL in
example.com 

```c
intitle:admin OR inurl:admin site:example.com
```


You can also look for a specific error message indicating a possible SQL injection
vulnerability

```c
"SQL Server Driver][SQL Server]Line 1: Incorrect syntax near"
 site:example.com
```

Trouver des résultats avec une expression de recherche exacte

```c
"search phrase"
```

Rechercher des fichiers de type `PDF` lié à un certain terme.

```c
OSINT filetype:pdf
```

Limitez les résultats de recherche à un site spécifique

```c
salary site:blog.tryhackme.com
```

Exclure un site spécifique des résultats

```c
pentest -site:example.com
```

Recherchez des pages avec un terme spécifique dans le titre de la page.

```c
walkthrough intitle:TryHackMe
```

Rechercher dans un titre

```c
intitle:"index of" "parent directory"
```


