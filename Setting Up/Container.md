# Container

L'utilisation de conteneurs garantit que les ressources informatiques sont strictement séparées les unes des autres.

## Docker

Tout système sur lequel Docker Engine est installé peut utiliser des conteneurs Docker.

Docker on Linux

```sh
sudo apt update && sudo apt install -y docker.io
```

Docker on Windows

```sh
C:\> IEX((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
C:\> choco upgrade chocolatey
C:\> choco install docker-desktop
```

**Vagrant**

Vagrant est un outil permettant de créer, configurer et gérer des machines virtuelles ou des environnements de machines virtuelles.

Vagrant on Linux

```sh
sudo apt update -y && sudo apt install virtualbox virtualbox-dkms vagrant
```

Vagrant on Windows

```sh
C:\> IEX((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))
C:\> choco upgrade chocolatey
C:\> cinst virtualbox cyg-get vagrant
```