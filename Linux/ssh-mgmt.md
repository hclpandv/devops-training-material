[<<Back](index.md)
#### Generating an SSH key-pair
```bash
ssh-keygen
# with advance options 
ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa  -q -N ""
```

#### Copying Public Key to Remote Hosts (On Ubuntu, for other linux you need to copy pub key to remote host ~/.ssh/authorized_keys )
```bash
ssh-copy-id -i ~/.ssh/id_rsa vagrant@10.10.10.61
ssh-copy-id -i ~/.ssh/id_rsa vagrant@10.10.10.62
```
* Now you can access these servers without a password
```
ssh vagrant@10.10.10.61
```

#### adding pvt Key to a shell session (then you dont need to specify pvt key to ssh commands)
```bash
eval $(ssh-agent)
ssh-add ~/.ssh/my-test-aws.pem
```
