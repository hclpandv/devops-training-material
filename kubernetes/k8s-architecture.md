![image](https://user-images.githubusercontent.com/13016162/123603386-6899c280-d82c-11eb-8115-7159c0220604.png)

![image](https://user-images.githubusercontent.com/13016162/123604465-713ec880-d82d-11eb-9068-b7507d876e17.png)

![image](https://user-images.githubusercontent.com/13016162/123607049-1bb7eb00-d830-11eb-9042-418b5eeac874.png)

![image](https://user-images.githubusercontent.com/13016162/123607701-b44e6b00-d830-11eb-9832-c42286b0f221.png)

```
Controller-Manager monitors the k8s clsuter state:

if a POD dies --> Controller Manager detects --> asks Scheduler to re-schedule --> Scheduler checks for apropriate NODE -->
Asks the KUBELET of that node to re-create the dead POD
```

![image](https://user-images.githubusercontent.com/13016162/123610638-596a4300-d833-11eb-9d8e-4c81db71b3e2.png)

```
etcd records every k8s clsuter state changes
```
