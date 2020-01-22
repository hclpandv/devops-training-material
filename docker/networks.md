[<<Back](index.md)
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

* Lets connect container alpine1 `docker attach alpine1` and do if config


