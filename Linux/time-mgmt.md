[<<Back](index.md)
# Time Sync 

* Ubuntu 18.04

```bash
timedatectl
```
*Output*
```
               Local time: Fri 2019-09-27 12:11:21 UTC
           Universal time: Fri 2019-09-27 12:11:21 UTC
                 RTC time: Fri 2019-09-27 12:11:12
                Time zone: Etc/UTC (UTC, +0000)
System clock synchronized: no
systemd-timesyncd.service active: yes

```

```bash
# Display Time Zones
timedatectl list-timezones
# Set a timezone
sudo timedatectl set-timezone America/New_York
# Sync it with network time NTP (on-off)
sudo timedatectl set-ntp no
sudo timedatectl set-ntp on

# If needed install ntp
sudo apt update
sudo apt install ntp

```
