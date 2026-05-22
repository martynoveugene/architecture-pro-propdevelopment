#!/bin/bash

minikube kubectl -- delete pod pod-host-path-fixed  -n audit-zone
minikube kubectl -- delete pod pod-privileged-fixed -n audit-zone
minikube kubectl -- delete pod pod-root-user-fixed  -n audit-zone

echo "apply from secure-manifests/"
kubectl apply -f secure-manifests/

kubectl get pods -n audit-zone

read -p "Press Enter..."
