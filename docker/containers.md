# Docker containers deep dive

* `docker container run -it <image_name> <program_to_start>` creates and starts a container from an image specified.
* It additinaly pulls an image if it is locally not available
* `docker run -it <image_name>` also works without explicit container keyword, but it considers a default `program_to_start` aka `entrypoint` is already defined in `Dockerfile` of the specified image (otherwise container is created but in exited state)

![image](https://user-images.githubusercontent.com/13016162/62453065-2a560e80-b78f-11e9-9050-2bbfe4c04816.png)

* Observe in the above example that one process is running i.e. `sh` (here microservices architecture recoomends to run a container limited to one process implementing one service)

* `docker container ls` OR `docker ps` shows active containers
* `docker ps -a` Includes exited containers too

![image](https://user-images.githubusercontent.com/13016162/62452350-a0597600-b78d-11e9-96aa-68f504609fbe.png)
