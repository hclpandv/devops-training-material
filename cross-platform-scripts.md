#### Get OS version /Distribution name

```bash
#!/usr/bin/env bash
cat /etc/*-release
lsb_release -a
```

```powershell
# PowerShell
[psobject]$envOS = Get-WmiObject -Class 'Win32_OperatingSystem' -ErrorAction 'SilentlyContinue'
$envOS.Caption.Trim()
$envOS.version
```

#### Get hostname

```bash
#!/usr/bin/env bash
HOSTNAME=$(hostname -s)
FQDN=$(hostname -f)
```

```powershell
# PowerShell
$Hostname = $env:COMPUTERNAME
$fqdn = ([System.Net.Dns]::GetHostByName(($env:computerName))).hostname
```


#### Get the IP address of system

```bash
#!/usr/bin/env bash
IPADDR=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 
```

```powershell
# PowerShell
$IPADDR = (Get-NetIPAddress | ?{ $_.AddressFamily -eq "IPv4" -and !($_.IPAddress -match "169") -and !($_.IPaddress -match "127") } | Select-Object -First 1).IPAddress
```

#### Is the session run by admin/sudo?

```bash
#!/usr/bin/env bash
 
```

```powershell
# PowerShell
[boolean]$IsAdmin = [boolean]($CurrentProcessToken.Groups -contains [Security.Principal.SecurityIdentifier]'S-1-5-32-544')
```

