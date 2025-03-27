# Environment Setup

**Hardware**
- External USB Wi-Fi dongle : `ALFA AWUS036H 802.11g`
- For wifi adapter pay attention on:
	- Signal Power
	- Receiver sentivity
	- Linux driver support


Determine is we are using `mac80211` drivers

```sh
lsmod | grep mac80211
```

Changer channel of card to 11

```sh
sudo iwconfig wlan0 channel 11
sudo iw dev wlan0 channel 11
```

> Remember that by default, many wireless adapter are configure to work with regdomain set to 0, make adapter will not deliver their maximum performance. Also using an high transmission power may be **illegal** in your country

To maximum transmit power we have to set country code to Bolivia

```sh
sudo iw reg set BO
sudo iw dev wlan0 set txpower fixed 30dbm
```

First run this commands to resolve blocked device and start monitor mode to sniff traffic and perform low level network operations

```sh
sudo airmon-ng check kill
sudo airmon-ng start wlan0
```

> **Remember: Start your monitor interface first and set the card to the desired channel.**
