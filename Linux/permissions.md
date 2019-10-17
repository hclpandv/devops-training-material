[<<Back](index.md)
## Permissions on files and dirs

```bash
# Permissions on a file or dir 
# In Linux file and dir are comsidered as similar objects, dir is a file with pointers of its child objs
chmod 755 my_file_or_dir_name
# Adding execute permissions (in addition to what perm already exists)
chmod +x my_file_or_dir_name
# Add write perm only for current user
chmod u+w my_file_or_dir_name

# Change ownership
chown root_or_user my_file_or_dir_name
# Ownership with both user and group
chown user_name:grp_name my_file_or_dir_name
# Only grp change
chown :grp_name my_file_or_dir_name
```


