# Docker images deep dive

* `docker pull <image_name>` pulls the image from registry (default is docker hub | docker.io)

![image](https://user-images.githubusercontent.com/13016162/62443900-bb21ef80-b779-11e9-9835-b5d26a9c320e.png)

![image](https://user-images.githubusercontent.com/13016162/62444062-21a70d80-b77a-11e9-81c9-e1d5bcee4371.png)

* Pulling an Image is a 2 step process (from docker.io or any other registry i.e. google container registry aka gcr.io etc)

* It pulls a fat manifest and then checks for OS type and architecture to pull actual image manifest.
* images are then pulled in seperate layers

![image](https://user-images.githubusercontent.com/13016162/62444324-d4776b80-b77a-11e9-99e1-65edb184e229.png)

* Images are hashed for integrity

![image](https://user-images.githubusercontent.com/13016162/62444806-24a2fd80-b77c-11e9-834b-082ddf1fab97.png)

### Behind the sceene

* The storage driver keeps and manages the images cached locally

![image](https://user-images.githubusercontent.com/13016162/62444952-a2ff9f80-b77c-11e9-8261-c1d5ae5a18af.png)

* Lets browse the `Docker Root Dir: /var/lib/docker` to inspect the local images

![image](https://user-images.githubusercontent.com/13016162/62445124-202b1480-b77d-11e9-9419-34c2b3982b1e.png)

![image](https://user-images.githubusercontent.com/13016162/62445452-dbec4400-b77d-11e9-852f-e90c889957c0.png)

* `docker history <image_name>` will show you how the image is built by layers

![image](https://user-images.githubusercontent.com/13016162/62448515-aa777680-b785-11e9-8cdf-b21aac7688a4.png)

