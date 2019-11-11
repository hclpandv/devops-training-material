[<<Back](index.md)
## Add a User
```bash
sudo adduser vpandey
```
```
# Output

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

## Provide sudo privilege to new user
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

## List all users and groups
```bash
# List Users
compgen -u
awk -F: '{ print $1}' /etc/passwd
# List Groups
compgen -g
awk -F: '{ print $1}' /etc/group
```
## Create a New group and add users
```bash
# Create group
sudo groupadd vikiscripts

# You could add the users to this new group
sudo usermod -a -G vikiscripts vpandey2
sudo usermod -a -G vikiscripts vpandey

# Verify
grep vikiscripts /etc/group
```
![image](https://user-images.githubusercontent.com/13016162/68592978-5eda1480-04ba-11ea-905f-d58c3f4d770e.png)

## Lets assign permission to a directory

```bash
chown <user_name>:<grp_name> dir_name
```
![image](https://user-images.githubusercontent.com/13016162/68593246-fd667580-04ba-11ea-85fc-44c6042f00f6.png)

