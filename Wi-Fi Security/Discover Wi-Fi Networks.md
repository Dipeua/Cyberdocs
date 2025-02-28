It is just traffic sniffing

This first thing to do when using tools in linux is to putting your adapter to monitor mode
# Tools
#windows 
InSSIDer Office, WirelessNetView

#linux 

```sh
sudo kismet -c wlan0mon
```

- N (None)
- W (Wep)
- O (Other), WPA or WPA2

```sh
sudo airodump-ng wlan0mon -w output -c <channel> -b <BSSID> -t wpa
```

---
# Hidden SSID
#De-cloaking-Attack
Use wireshark and start sniffing on monitor interface. just look the `Probe requests/response` by using the filter:
 
```
wlan.fc.type_subtype == 0x05
```

#Deauthenticate-Attack
Involve sending pakect for  active station who connect to AP

```sh
sudo aireplay-ng -0 1 -c <client_mac> -a <BSSID> wlan0mon
```

