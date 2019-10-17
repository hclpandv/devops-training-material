[<<Back](index.md)

#### Permissions on files and dirs

```bash
# Permissions on a file or dir 
# In Linux file and dir are considered as similar objects, dir is a file with pointers of its child objs
chmod 755 my_file_or_dir_name
# Adding execute permissions (in addition to what perm already exists)
chmod +x my_file_or_dir_name
# Add write perm only for current user
chmod u+w my_file_or_dir_name
```

#### Ownership

```bash
# Change ownership
chown root_or_user my_file_or_dir_name
# Ownership with both user and group
chown user_name:grp_name my_file_or_dir_name
# Only grp change
chown :grp_name my_file_or_dir_name
```

#### Understanding Permissions

![image](https://user-images.githubusercontent.com/13016162/66981974-e22e6300-f0d2-11e9-9eb4-2cb4210db61a.png)  
![image](https://user-images.githubusercontent.com/13016162/66982042-fb371400-f0d2-11e9-9959-bd1b09b4329f.png)  

![image](https://user-images.githubusercontent.com/13016162/66982977-0db24d00-f0d5-11e9-9b38-4bb98f86ac3d.png)




