Determine is we are using `mac80211` drivers

```sh
lsmod | grep mac80211
```

List all adapters

```sh
iw list
```

Changer channel of card to 11

```sh
sudo iwconfig wlan0 channel 11
sudo iw dev wlan0 channel 11
```


> [!NOTE] Remember that
> By default, many wireless adapter are configure to work with regdomain set to 0, make adapter will not deliver their maximum performance.
> 
> Note that using an high transmission power may be **illegal** in your country

To maximum transmit power we have to set country code to Bolivia

```sh
sudo iw reg set BO
sudo iw dev wlan0 set txpower fixed 30dbm
```

Monitor interface use to sniff traffic and perform low level network operations though your adapter

First run this command to resolve blocked device 

```sh
sudo airmon-ng check kill
```

```sh
sudo airmon-ng start wlan0
sudo airmon-ng stop wlan0mon
```

Testing our equipment if everything is ok

> [!NOTE] Remember
> Start your monitor interface first and set the card to the desired channel.

```sh
sudo aireplay-ng -9 wlan0mon
```

