## Docker Build Deep Dive (Containerize an app)

* Lets Create a new directory `viki-container-web-app` 
* Create a Edit `Dockerfile` with capital `D`
* Add the content as shown below, similar for index.html

![image](https://user-images.githubusercontent.com/13016162/62513403-9ee58780-b839-11e9-8833-4414eb329e3b.png)

* `docker build -t <image_name> .` OR `docker image build -t <image_name> .` command builds an Image from current directory (notice Dot `.` at the end of command)

![image](https://user-images.githubusercontent.com/13016162/62513871-0ea84200-b83b-11e9-9f34-991128f6aefe.png)

![image](https://user-images.githubusercontent.com/13016162/62513924-30092e00-b83b-11e9-807a-ed9fb9b699c7.png)

* docker expects a `Dockerfile` in current directory to get an intructions how to build a command
* Instructions in `Dockerfile` is like a `Key-Value` pair where Keys are kept as UPPERCASE (aka FROM, RUN, COPY)
* Below picture gives a detail about this

![image](https://user-images.githubusercontent.com/13016162/62511989-bd488480-b833-11e9-8e46-d0949a09a40e.png)

