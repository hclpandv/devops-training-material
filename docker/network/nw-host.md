[DevOps Training](../../index.md) >> [Docker](../index.md) >> [Docker Network](index.md) >> [Host](.)

### Docker network supported by Host Driver (Host only network, attached to host's network)

>standalone containers which bind directly to the Docker host’s network, with no network isolation

Create a container and connect it to `host` network already created by docker

```bash
docker run --rm -d --network host --name my_nginx nginx
```

* access Nginx by browsing to http://localhost:80/.

* Examine all network interfaces and verify that a new one was not created.
```
ip addr show

```
* Verify which process is bound to port 80, using the netstat command. You need to use sudo because the process is owned by the Docker daemon user and you otherwise won’t be able to see its name or PID.

```
sudo netstat -tulpn | grep :80
```
