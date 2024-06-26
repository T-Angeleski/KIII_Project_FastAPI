#!/bin/bash

# Apply namespaces and PVCs first
MANIFESTS=(
  "namespace.yaml"
  "database-postgres.yaml"
  "static-files-pvc.yaml"
  "app-deployment.yaml"
  "app-service.yaml"
  "ingress-traefik.yaml"
)
echo "Changing directory"
cd kubernetes
for manifest in "${MANIFESTS[@]}"; do
  echo "Applying $manifest"
  kubectl apply -f "$manifest"
done

echo "Finished..."