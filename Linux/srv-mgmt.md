[<<Back](index.md)
## Service in Linux

#### List all services

![image](https://user-images.githubusercontent.com/13016162/65593253-b45f6e00-dfad-11e9-93f3-1f06587d9e46.png)

```
+ = Running
- = Stopped
? = Service does not have status parameter
```

#### Service Status, Start, Stop, Restart

```bash
sudo systemctl apache2 restart
sudo systemctl apache2 status
sudo /etc/init.d/my_service restart
```
