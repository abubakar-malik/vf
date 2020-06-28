#!/bin/sh -e

source ./source.sh

echo "ENVIRONMENT VARIABLES: "
echo $AWS_EKS_CLUSTER
echo $AWS_EKS_K8S_VERSION

echo "Deleting EKS cluster..."
eksctl delete cluster --name ${AWS_EKS_CLUSTER}
