#!/bin/bash -e

source source.sh


echo EKS ClusterName: $AWS_EKS_CLUSTER
echo Kubernetes version: $AWS_EKS_K8S_VERSION

echo "Deleting EKS cluster..."
eksctl delete cluster --name ${AWS_EKS_CLUSTER}
