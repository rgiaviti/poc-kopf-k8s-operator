# POC Kopf Kubernetes Operator
Docs: https://kopf.readthedocs.io/en/stable/
## Steps
### Install KOPF
```
$ pip install kopf
```

### Create a Cluster
```
$ kind create cluster --name kopf_cluster
```
Details: https://kind.sigs.k8s.io/docs/user/quick-start/

### Create a namespace
```
$ kubectl create namespace kopfns
```

### Deploy CRD on cluster
```
$ kubectl apply -f crd/crd.yaml
```

### Start KOPF
```
$ kopf run mycrd_controller.py --verbose
```

### Deploy CR in a namespace
```
$ kubectl apply -f crd_object.yaml -n kopfns
```