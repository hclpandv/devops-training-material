[<<Back](index.md)
## Accessing a Remote Cloud VM via PowerShell Remote (Azure, AWS EC2 Instance etc)

####  Steps to be performed on Portal or via cloud mgmt PS module (Azure/AWS)

* Open WinRM Port on your security group configuration (Below example on azure portal)

![image](https://user-images.githubusercontent.com/13016162/65591674-862c5f00-dfaa-11e9-8bda-0b2eb22876b1.png)


#### Steps to be performed on cloud VM Instance 

```powershell
# Config winrm
winrm quickconfig
# Enable PS remoting
Enable-PSRemoting -Verbose
# Create a Local cert
$cert = New-SelfSignedCertificate -CertStoreLocation Cert:\LocalMachine\My -DnsName $env:COMPUTERNAME
# Add cert to wsman localhost
New-Item -Path WSMan:\localhost\Listener -Transport HTTPS -Address * -CertificateThumbPrint $cert.Thumbprint -Force
# Add a new firewall rule on OS 
New-NetFirewallRule -DisplayName 'WinRM HTTPS-In' -Name 'WinRM HTTPS-In' -Profile any -LocalPort 5986 -Protocol TCP
```

#### Steps to be performed on Local machine (Typically Your laptop)

```powershell
# Config winrm
winrm quickconfig
$IP = "10.10.10.10"
$azure_vm_cred = Get-Credential -UserName "$IP\vikiscripts" -Message "Password Pls"
# Add the cloud instance ip to your trusted host
Set-Item WSMan:\localhost\Client\TrustedHosts -Value $IP
# connect
Enter-PSSession -ComputerName $IP -Credential $azure_vm_cred -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck) -UseSSL

# OR

Enter-PSSession -ConnectionUri https://"$IP":5986 -Credential $azure_vm_cred -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck -SkipRevocationCheck) -Authentication Negotiate
```

![image](https://user-images.githubusercontent.com/13016162/65743343-c78b4e80-e111-11e9-8378-7ab08054df85.png)

![image](https://user-images.githubusercontent.com/13016162/65743399-015c5500-e112-11e9-8ded-20b5f36d7442.png)




