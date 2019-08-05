# Docker images deep dive

* `docker pull <image_name>` pulls the image from registry (default is docker hub | docker.io)

![image](https://user-images.githubusercontent.com/13016162/62443900-bb21ef80-b779-11e9-9835-b5d26a9c320e.png)

![image](https://user-images.githubusercontent.com/13016162/62444062-21a70d80-b77a-11e9-81c9-e1d5bcee4371.png)

* Pulling an Image is a 2 step process (from docker.io or any other registry i.e. google container registry aka gcr.io etc)

* It pulls a fat manifest and then checks for OS type and architecture to pull actual image manifest.
* images are then pulled in seperate layers

![image](https://user-images.githubusercontent.com/13016162/62444324-d4776b80-b77a-11e9-99e1-65edb184e229.png)
