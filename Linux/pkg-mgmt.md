[<<Back](index.md)
## Ubuntu / Debian

* apt - Advanced Packaging Tool 

```bash
# To Install a package
sudo apt-get install <pkg_name>:[<pkg_version>]
# To List all Installed packages
sudo apt list --installed
# Logs
cat /var/log/dpkg.log | grep "\ install\ "
```

## Centos / RHEL / Fedora

* yum 

> The Yellowdog Updater, Modified (YUM) is a free and open-source command-line package-management utility for computers running the Linux operating system using the RPM Package Manager.

```bash
# To Install a package
sudo yum install <pkg_name>
```
