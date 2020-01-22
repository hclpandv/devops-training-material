[DevOps Training](../../index.md) -> [Docker](../index.md) -> [Docker Network](index.md) -> [Bridge](.)

### Docker network supported by Bridge driver

* Lets create a user defined docker network `docker network create`

```bash
docker network create --driver bridge viki-alpine-net
```

* Inspect and observe
* Docker uses the default 172.17.0.0/16 subnet for container networking. If this subnet is not available for docker in your environment (for example because your network already uses this subnet), you must configure Docker to use a different subnet.

```
vagrant@vagrant:~$ docker network inspect viki-alpine-net
[
    {
        "Name": "viki-alpine-net",
        "Id": "57284e7cd72cad3b25af2797103bf993f2f564308cc4a518a36573776b9bdc8e",
        "Created": "2020-01-22T04:11:46.780266369Z",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": {},
            "Config": [
                {
                    "Subnet": "172.20.0.0/16",
                    "Gateway": "172.20.0.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]

```

* ifconfig on your docker host machine will also show you `docker0` network intercace created by docker 

![image](https://user-images.githubusercontent.com/13016162/72865051-6577da00-3cfc-11ea-82fe-ea97946c9a7d.png)




