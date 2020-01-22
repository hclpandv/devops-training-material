[DevOps Training](../../index.md) -> [Docker](../index.md) -> [Docker Network](index.md) -> [Host](.)

### Docker network supported by Host Driver (Host only network, attached to host's network)

>standalone containers which bind directly to the Docker host’s network, with no network isolation

Create a container and connect it to `host` network already created by docker

```bash
docker run --rm -d --network host --name my_nginx nginx
```

