#!/bin/bash -e

source source.sh

echo EKS ClusterName: $AWS_EKS_CLUSTER
echo Kubernetes version: $AWS_EKS_K8S_VERSION

echo "Bringing up EKS cluster..."
eksctl create cluster --name=${AWS_EKS_CLUSTER} \
                      --nodes=1 \
                      --version=${AWS_EKS_K8S_VERSION}

echo "Configuring kubectl config to use new cluster..."
aws eks update-kubeconfig --name=${AWS_EKS_CLUSTER}

echo "Verifing nodes are ready..."
kubectl get nodes
