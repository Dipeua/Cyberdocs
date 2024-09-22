BASH

```sh
/usr/bin/script -qc /bin/bash /dev/null
export TERM=xterm
```

Python

```sh
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
clear
Ctrl + Z
stty raw -echo; fg
```