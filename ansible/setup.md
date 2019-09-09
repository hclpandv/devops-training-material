[<<Back](index.md)

Ansible is an agentless configuration management tool that uses YAML templates to define a list of tasks to be performed on hosts.

## How to Setup ansible ?

* ansible can be used to configure remote servers through remotely accessing them over ssh or winrm(in case of Windows).
* you can install ansible to any machine which has remote access to actual target servers. 
* the machine where you install ansible is refered as ansible control machine.
* ansible can only be installed on Linux machines but it can manage remote windows hosts/servers too. (at the time of writing this articles)
* since winodows OS coming with WSL (Windows subsystem linux) one can install ansible on linux subsystem.(ubuntu for example)

#### Linux | via ppa (ubuntu)

```bash
#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y software-properties-common
add-apt-repository -y ppa:ansible/ansible
apt-get update
apt-get install -y ansible
```

#### Linux | via python pip

```bash
#!/usr/bin/env bash

export DEBIAN_FRONTEND=noninteractive
apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y
apt-get install -y software-properties-common
apt-get install -y python3-pip
pip3 install ansible
```

#### Windows Subsystem Linux
* Use below link to learn how you can control your own windows host using ansible installed on WSL

[Setting up ansible on WSL](https://github.com/hclpandv/setting-up-wsl-ansible-to-control-windows-host)
