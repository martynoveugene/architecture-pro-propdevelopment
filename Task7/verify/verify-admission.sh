#!/bin/bash

minikube kubectl -- delete pod pod-host-path  -n audit-zone
minikube kubectl -- delete pod pod-privileged -n audit-zone
minikube kubectl -- delete pod pod-root-user  -n audit-zone

echo "apply from insecure-manifests/"
kubectl apply -f insecure-manifests/

kubectl get pods -n audit-zone

read -p "Press Enter..."
