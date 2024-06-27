# Project for KIII Course 2024
## Teodor Angeleski 211080

## Running:

With docker:
```
docker compose up
```

```
k3d cluster create gaming-app-cluster -s 1 -a 2 --port 80:80@loadbalancer

./deploy-manifests.sh
```
