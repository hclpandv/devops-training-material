[<<Back](index.md)
## Docker Build Deep Dive (Containerize an app)

* Lets Create a new directory `viki-container-web-app` 
* Create a Edit `Dockerfile` with capital `D`
* Add the content as shown below, similar for index.html

![image](https://user-images.githubusercontent.com/13016162/62513403-9ee58780-b839-11e9-8833-4414eb329e3b.png)

* `docker build -t <image_name> .` OR `docker image build -t <image_name> .` command builds an Image from current directory (notice Dot `.` at the end of command)

![image](https://user-images.githubusercontent.com/13016162/62513871-0ea84200-b83b-11e9-9f34-991128f6aefe.png)

* Now you can use `docker run` to run a container from newly built image
* `--rm` in docker run command removes a container the moment it is exited.
* `-it` mode makes it interactive, you could also see the output of nginx web requests here.

![image](https://user-images.githubusercontent.com/13016162/62513971-5202b080-b83b-11e9-86de-854666d626bb.png)

* You can also build an image from a git repo

![image](https://user-images.githubusercontent.com/13016162/62514435-cee25a00-b83c-11e9-92ae-1ce21723d1d8.png)

* docker expects a `Dockerfile` in the directory where it is builing to get intructions to build the image
* Instructions in `Dockerfile` is like a `Key-Value` pair where Keys are kept as UPPERCASE (aka FROM, RUN, COPY)
* Below picture gives a detail about this

![image](https://user-images.githubusercontent.com/13016162/62511989-bd488480-b833-11e9-8e46-d0949a09a40e.png)

