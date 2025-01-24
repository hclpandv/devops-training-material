[<<Back](index.md)
## Basic CLI

```bash
# Basic ping module
ansible localhost -m ping
# Use -a to provide the value of parameters
ansible localhost -m debug -a "msg='Msg from Ansible...'"
# Get the details of the target server (Complete facts). Usefull for hacks
ansible windows_servers -m setup
# Execute a playbook
ansible-playbook playbook-to-target.yml
```
## Adhoc Commands

```bash
# Try mulipls times and observe the parrelism
# target_group from inventory
ansible target_group -a "hostname" 
ansible app_servers -a "hostname"
ansible db_servers -a "hostname"
ansible target_group -a "df -h"
ansible target_group -a "free -m"
ansible target_group -a "date"

# Details of ansible facts | setup is a module
ansible target_servers -m setup

# Configure app servers | Install python and django 
# `-b` is become sudo
ansible app -b -m yum -a "name=MySQL-python state=present"
ansible app -b -m yum -a "name=MySQL-python state=present"
ansible app -b -m yum -a "name=python-setuptools state=present"
ansible app -b -m easy_install -a "name=django<2 state=present"
ansible app -a "python -c 'import django; print django.get_version()'"

# Configure db server | Install mariadb
ansible db -b -m yum -a "name=mariadb-server state=present"
ansible db -b -m service -a "name=mariadb state=started enabled=yes"
ansible db -b -a "iptables -F"
ansible db -b -a "iptables -A INPUT -s 192.168.60.0/24 -p tcp -m tcp --dport 3306 -j ACCEPT"

ansible db -b -m yum -a "name=MySQL-python state=present"
ansible db -b -m mysql_user -a "name=django host=% password=12345 priv=*.*:ALL state=present"
```
