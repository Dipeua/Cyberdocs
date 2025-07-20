# Shodan

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


https://sankalppatil12112001.medium.com/shodan-for-pentesting-the-ultimate-detailed-guide-part-1-8b618e40acd5