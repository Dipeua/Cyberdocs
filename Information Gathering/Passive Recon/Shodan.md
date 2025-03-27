# Shodan

https://pen-testing.sans.org/blog/2015/12/08/effective-shodan-searches

Servers exposed to the internet belonging to some domain

```sh
hostname:example.com
```

Specific types of devices, such as CCTV cameras or Industrial Control Systems
(ICS), can be found by specifying the Server parameter:

```sh
Server: SQ-WEBCAM
```

Specific open ports or services can be found, for example, web servers using
common ports:

```sh
port:80,443,8080
```

Hosts in a specific network range can be found

```sh
net:192.168.1.1/24
```
