[<<Back](index.md)
## Docker Volumes Deep Dive

> By design, Docker containers do not store persistent data. Any data written to a container's writable layer will no longer be available once the container stops running. Also, getting data written to a container back out of it for another process can be difficult. To solve the issue of persisting data from a container docker uses volumes

* `docker volume ls` command will show all volumes
* Lets create one

![image](https://user-images.githubusercontent.com/13016162/62516040-94c78700-b841-11e9-885a-f84246794849.png)

* Lets Create another one and inspect

![image](https://user-images.githubusercontent.com/13016162/62516083-af99fb80-b841-11e9-89ac-036e0eac78ff.png)

* You can see those volumes mounted on `/var/lib/docker/volumes/` 

![image](https://user-images.githubusercontent.com/13016162/62516110-c2143500-b841-11e9-86f0-15b649b7edd0.png)

* Lets attach this volume to a new container. (`-v vikivol:/vol` and `--mount source=<vol_name>,target=<cont_mnt_dir>` are same however mount is preferred)

![image](https://user-images.githubusercontent.com/13016162/62516626-33a0b300-b843-11e9-85a0-92ff77d3e183.png)

* Now lets look into the volume. the Host machines directory is actually mounted into the container

![image](https://user-images.githubusercontent.com/13016162/62516781-942ff000-b843-11e9-8537-1fc6c2670a6e.png)

* This volume is persitent. even if you delete the container the volume with data will persist
* If you try to delete a volume which is being used by a container it will not be deleted thats a safety latch.
