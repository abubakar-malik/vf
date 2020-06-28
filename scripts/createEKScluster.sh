#!/bin/sh -e

source ./source.sh

echo "ENVIRONMENT VARIABLES: "
echo $AWS_EKS_CLUSTER
echo $AWS_EKS_K8S_VERSION

echo "Bringing up EKS cluster..."
eksctl create cluster --name=${AWS_EKS_CLUSTER} \
                      --nodes=3 \
                      --version=${AWS_EKS_K8S_VERSION}

echo "Configuring kubectl config to use new cluster..."
aws eks update-kubeconfig --name=${AWS_EKS_CLUSTER}

echo "Verifing nodes are ready..."
kubectl get nodes
