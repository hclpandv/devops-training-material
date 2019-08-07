[<<Back](index.md)
# Docker containers deep dive

* `docker container run -it <image_name> <program_to_start>` creates and starts a container from an image specified.
* It additinaly pulls an image if it is locally not available
* `docker run -it <image_name>` also works without explicit container keyword, but it considers a default `program_to_start` aka `entrypoint` or `cmd` is already defined in `Dockerfile` of the specified image (otherwise container is created but in exited state)
* `docker run -it` starts the container, attaches your terminal shell's I/O to Containers shell's I/O.

![image](https://user-images.githubusercontent.com/13016162/62453065-2a560e80-b78f-11e9-9050-2bbfe4c04816.png)

* Observe in the above example that one process is running i.e. `sh`.
* microservices architecture reccomends to run a container limited to one process implementing one service, however docker container supports multiple processes to run inside a container.
* `docker container ls` OR `docker ps` shows active containers, `docker ps -a` Includes exited containers too

![image](https://user-images.githubusercontent.com/13016162/62452350-a0597600-b78d-11e9-96aa-68f504609fbe.png)

* If you are into a container on the same terminal you can press `Ctrl+P+Q` to gracefully come out of the container session without existing it. 
* Lets start multiple containers from the same image. `docker run -d` will start a container in `detached` mode.

![image](https://user-images.githubusercontent.com/13016162/62454318-b6693580-b791-11e9-9bf0-c2ba1df2f99a.png)

* You can stop a container `docker container stop <container_name>` or `docker container stop <container_id>` You can use shorthand to provide the ID value only to its uniquness

![image](https://user-images.githubusercontent.com/13016162/62454652-5d4dd180-b792-11e9-81d8-933ab72fa603.png)

* `docker container stop` and `docker stop` is same. `container` keyword is almost reduntant since docker is a container in itself ;)
* `docker rm <container_id>` will remove it and `docker start <container_id>` will start an exited container.
* Stop and Start a container will persist any data kept in container. however, it is not reccomended to keep any data in a container.

![image](https://user-images.githubusercontent.com/13016162/62455042-262bf000-b793-11e9-8f58-24c7918960ab.png)

* if you want to access a running container us `docker exec -it <container_id or name> <program_to_start>`

![image](https://user-images.githubusercontent.com/13016162/62455571-545dff80-b794-11e9-81cc-faa74e381f49.png)

* You can also execute a command against a container rather running a program 

![image](https://user-images.githubusercontent.com/13016162/62456009-23ca9580-b795-11e9-8221-6618621cba55.png)

* You can also start a container assigning it a name.
* Lets quickly run an nginx container with an assigned name and access it via a custom port

![image](https://user-images.githubusercontent.com/13016162/62457912-5d9d9b00-b799-11e9-9011-f0db69e593ca.png)
![image](https://user-images.githubusercontent.com/13016162/62457958-73ab5b80-b799-11e9-83a8-7cb4228ff428.png)


* Lets try and remove all containers `docker container rm $(docker container ls -aq) -f`
* docker help shows q in `ls -aq` is an option of quite which shows only container IDs and `-f` to force and remove running containers too

![image](https://user-images.githubusercontent.com/13016162/62456363-def32e80-b795-11e9-8a5d-ba4db3c8db5c.png)



