
> Toujours avoir une machine virtuelle Linux et Windows personnalisée et entièrement à jour.

# Linux

Distributions de tests d’intrusion 

- [ParrotOS](https://www.parrotsec.org/)

- [Kali](https://www.kali.org/)

- [BlackArch](https://blackarch.org/)

- [Linux BlackBox](https://linux.backbox.org)


Mise a jour complete

```sh
sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y
```

Installation des Outils

```sh
sudo apt install -y $(cat tools.list | tr "\n" " ")
```

### Virtualization

VMware on Linux

```sh
sudo apt install -y build-essential && sudo bash ~/Downloads/VMware*.bundle
```

VirtualBox on Linux

```sh
sudo apt install -y virtualbox virtualbox-ext-pack
```

# Windows

- CommandoVM

- Manuel

```sh
# Mises à jour 
PS C:\Temp> Get-ExecutionPolicy -List
PS C:\Temp> Set-ExecutionPolicy Unrestricted -Scope Process #A

# Mise à jour PSWindows
PS C:\Temp> Install-Module PSWindowsUpdate
PS C:\Temp> Import-Module PSWindowsUpdate
PS C:\Temp> Install-WindowsUpdate -AcceptAll  
PS C:\Temp> Restart-Computer -Force
```

Gestionnaire de paquets [chocolatey](https://docs.chocolatey.org/en-us/choco/commands/install)


```sh
PS C:\Temp> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Mise à jour, verification et installation

```sh
PS C:\Temp> choco upgrade chocolatey -y 
PS C:\Temp> choco install pkg1 pkg2 pkg3 
PS C:\Temp> choco info pkg 
```

Exemptions de Windows Defender pour les dossiers d'outils.

```sh
PS C:\Temp> Add-MpPreference -ExclusionPath "C:\Users\Dipeua\Tools\"
```