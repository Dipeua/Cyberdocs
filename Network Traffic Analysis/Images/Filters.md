# Capture Filter

Capture only traffic pertaining to a certain host

```
host x.x.x.x
```

Capture traffic to or from a specific network (using slash notation to specify the mask)

```
net x.x.x.x/24
```

Using `src` or `dst` net will only capture traffic sourcing from the
specified network or destined to the target network

```
src/dst net x.x.x.x/24
```

will filter out all traffic except the port you specify

```
port #
```

will capture everything except the variable specified. ex

```
not port 80
```

AND will concatenate your specified ports. ex

```
host 192.168.1.1 and port 80
```

Portrange will grab traffic from all ports within the range only

```
portrange x-x
```

These filters will only grab traffic from specified protocol headers.

```
ip / ether / tcp
```

Grabs a specific type of traffic. one to one, one to many, or one
to all.

```
broadcast /
multicast /
unicast
```

# Display Filter

Capture only traffic pertaining to a certain host. This is an OR
statement.

```
ip.addr == x.x.x.x
```

Capture traffic pertaining to a specific network. This is an OR
statement.

```
ip.addr == x.x.x.x/24
```

Capture traffic to or from a specific host.

```
ip.src/dst == x.x.x.x
```

Filter traffic by a specific protocol. There are many more
options.

```
dns / tcp / ftp / arp / ip
```

Filter by a specific tcp port.

```
tcp.port == x
```

will capture everything except the port specified

```
src.port / dst.port == x 
```

AND will concatenate, OR will find either of two options, NOT
will exclude your input option.

```
and / or / not
```

Allows us to follow a tcp session in which we captured the
entire stream. Replace (#) with the session to reassemble.

```
tcp.stream eq # 
```

This filter will display any packet with a jpeg image file.

```
http && image-jfif
```

Will filter for any control commands sent over ftp control
channel.

```
ftp.request.command
```

Will show any objects transfered over ftp.

```
ftp-data
```