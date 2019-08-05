# Docker containers deep dive

* `docker container run -it <image_name> <program_to_start>` creates and starts a container from an image specified.
* It additinaly pulls an image if it is locally not available
* `docker run -it <image_name>` also works without explicit container keyword, but it considers a default `program_to_start` aka `entrypoint` is already defined in `Dockerfile` of the specified image (otherwise container is created but in exited state)

![image](https://user-images.githubusercontent.com/13016162/62452100-2628f180-b78d-11e9-8e0a-f9fddc6984af.png)


