[DevOps Training](../../index.md) >> [Docker](../index.md) >> [Docker Network](.)
## Docker networks deep dive


![image](https://user-images.githubusercontent.com/13016162/62511492-9ee18980-b831-11e9-97ed-4792d4df158f.png)

* Lets create two containers for some quick testing

```bash
docker run -dit --name alpine1 alpine ash
docker run -dit --name alpine2 alpine ash
```

* Now inspect the bridge network

![image](https://user-images.githubusercontent.com/13016162/72863360-5aba4680-3cf6-11ea-9388-dab79ce83960.png)

* Whenever we create a container it gets attached into this default network `Name: Bridge , Driver: Bridge`

* Lets connect container alpine1 `docker attach alpine1` and do ifconfig to inspect
* You will also notice `ping container_name` does not work (You can achive this by creating a user defined network)
* `Ctrl+P+Q` to exit the container withough stoping it.

![image](https://user-images.githubusercontent.com/13016162/72863745-c18c2f80-3cf7-11ea-990f-7ce7ff8a6d51.png)


* Stop and Remove these containers

```
docker container stop alpine1 alpine2
docker container rm alpine1 alpine2
```

* You could chose to create `Bridge` or `Host` type use defined network

[Bridge](nw-bridge.md)  
[host](nw-host.md)


