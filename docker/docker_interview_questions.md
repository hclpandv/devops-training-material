[<<Back](index.md)
## Docker RUN vs CMD vs ENTRYPOINT

* RUN happens at build time. RUN executes command(s) in a new layer and creates a new image. E.g., it is often used for installing software packages.
* CMD happens at run time. CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.
* ENTRYPOINT configures a container that will run as an executable.

```
RUN apt-get install python3
CMD echo "Hello world"
ENTRYPOINT echo "Hello world"
```

* Are you building dependencies into your image? Use RUN.
* Are you launching / running your Dockerized process? Use CMD.

## Docker COPY vs ADD

* COPY and ADD are both Dockerfile instructions that serve similar purposes. They let you copy files from a specific location into a Docker image.
* COPY takes in a src and destination. It only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself.
* ADD lets you do that too, but it also supports 2 other sources. First, you can use a URL instead of a local file / directory. Secondly, you can extract a tar file from the source directly into the destination.

## Chain Your Docker RUN Instructions to Shrink Your Images

```bash
RUN wget -O myfile.tar.gz http://example.com/myfile.tar.gz \
    && tar -xvf myfile.tar.gz -C /usr/src/myapp \
    && rm myfile.tar.gz
```
* This is much better. Docker will only create 1 layer, and you still performed all 3 tasks. Shrinkage! You’ll even get faster build times too because each layer adds a bit of build time.

## Difference between an Array and String Based CMD

* The official terms for this are exec form and shell form commands. Both do nearly the same thing, but there's an important difference.
* Using [] is considered “exec form” and the plain string command is considered "shell form"
* Exec Form runs your CMD’s binary as is, along with any arguments you optionally pass in.

```
CMD ["gunicorn", "-c", "python:config.gunicorn", "hello.app:create_app()"]
```
* Shell Form runs your CMD’s binary through a shell which has the added benefit of using any shell functionality you want (such as using pipes and &&, etc.).

```
CMD gunicorn -c "python:config.gunicorn" "hello.app:create_app()"
```
* Which One Should You Use?

Shell form sounds better in theory, but it can mess with signal processing. It also means the shell process ends up being PID 1 instead of whatever binary you’re running in your CMD.

```
Showing what PID 1 is using both methods:
# The output of `ps` when you use exec form:
PID   USER     TIME   COMMAND
  1   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 15   root     0:02   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
188   root     0:00   ps

# The output of `ps` when you use shell form:
PID   USER     TIME   COMMAND
  1   root     0:00   /bin/sh -c gunicorn -c python:config.gunicorn hello.app:create_app()
  6   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 16   root     0:00   {gunicorn} /usr/local/bin/python /usr/local/bin/gunicorn
 29   root     0:00   ps
```
Docker (and I) both recommend that you use exec form whenever possible, which really is most of the time. If you need to do complicated shell scripting when a container starts, you should probably use an ENTRYPOINT script.

## Output All of Your Container's ENV Variables

```bash
docker container run --rm alpine:3.7 env

# The above command produces this output:
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=157baf151103
HOME=/root
```
## Show Total Disk Space Used by Docker

* Docker has a `system` sub-command that has a few useful commands. One of them is `docker system df` which reports back disk space usage stats of your Docker installation.

![image](https://user-images.githubusercontent.com/13016162/62266833-8b0be100-b447-11e9-8dc8-ec6b37aded63.png)

![image](https://user-images.githubusercontent.com/13016162/62266934-efc73b80-b447-11e9-9435-7b08b5dc1e03.png)

