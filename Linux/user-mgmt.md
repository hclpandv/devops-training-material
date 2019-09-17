## Add a User
```bash
$ sudo adduser vpandey
Adding user `vpandey' ...  
Adding new group `vpandey' (1001) ... 
Adding new user `vpandey' (1001) with group `lubos' ...
Creating home directory `/home/vpandey' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for lubos
Enter the new value, or press ENTER for the default
        Full Name []: 
        Room Number []: 
        Work Phone []: 
        Home Phone []: 
        Other []: 
Is the information correct? [Y/n] y

```

## Provide sudo sudo privilege
```bash
usermod -aG sudo vpandey
```

## Enable passwordless sudo
```bash
# make sudoers file wriatble
chmod u+w /etc/sudoers

# Add below line
echo vpandey ALL=(ALL) NOPASSWD:ALL >> /etc/sudoers

# remove write access again
chmod u-w /etc/sudoers
```
