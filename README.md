# Introduction
This project will deploy a simple Python based API. It has couple of POST methods. You can use one method to insert date-time stamp into your database while one method to see existing data from the database. The application is scaleable and have persistent data in case of application failure or unexpected crash of database. Below you can see logical diagram of the solution and architecture diagram of one of the possible solutions. There are also PDFs (architecture.pdf, logical_design.pdf) available in the repository 

## Logical design and Architecture diagram
![Logical Design](images/logical_design.png)
![Architecture Diagram](images/architecture.png)

## How to test if POC is working?
Use one or all of the below curl commands 

* To get welcome/landing message
```
 curl -X POST http://{HOST}
 ```
 * To insert the DateTime stamp into the database
```
 curl -X POST http://{HOST}/app
 ```
 * To get data from database
```
 curl -X POST http://{HOST}/show
 ```
 HOST has one of the below values;
 1. a387bfbc1b8dd11ea98b40ad3723e932-2083732890.eu-west-2.elb.amazonaws.com
 2. ip1
 3. ip2
 4. ip3

 ## Solution Explanation
 ***IMPORTANT:*** The solution was deployed and tested on Ubuntu 18 and on MAC catalina version 10.15.5
 ### Prerequisites
* [Amazon AWS account](https://aws.amazon.com/)
* [AWS Configured](https://docs.aws.amazon.com/cli/latest/reference/configure/)
* [Amazon CLI](https://aws.amazon.com/cli/)
* [Amazon EKS CLI](https://eksctl.io/)
* [Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Docker](https://docs.docker.com/get-docker/)

 #### Get source code
 ```
  git clone https://github.com/abubakar-malik/vf.git
 ```
 #### Create EKS cluster
  ```
 cd scripts/
 ./createEKScluster.sh
 ```
 This should take 5-10 minutes to setup EKS cluster for you. Meanwhile you can create a Docker image as described below
 #### Create Docker image
 ```
 cd docker/
 sudo docker build --tag vf .
 sudo docker login --username={DOCKERHUB_USER_NAME}
 sudo docker images
 sudo docker tag {IMAGE_ID} {DOCKERHUB_USER_NAME}/vf:latest
 sudo docker images
 sudo docker push {DOCKERHUB_USER_NAME}/vf:latest
 ```
 #### Deploy APP/DB stack
 ```
 kubectl apply -k ./
 ```
 This will run kustomization.yaml exists in the root directory of the repo. kustomization.yaml will create kubernetes resources required to run application and database. This will also create an AWS loadbalancer to access application.
 #### Test APP/DB
 You can run below command to check if resources have been created successfully in Kubernetes
 ```
 kubectl get all
 ```
 for full end to end testing you can run below to check if app is running and inserting/retrieving data from database
 ```
 curl -X POST http://{HOST}
 curl -X POST http://{HOST}/show
 curl -X POST http://{HOST}/app
 ```
 where HOST can be AWS Loadbalancer name or one of the IPs it's resolving to.
 #### Scale up and auto scaling
 You can scale up and scale down the solution vertically by increasing number of pods or horizontally by increasing number of nodes. For example;
 ```
 kubectl scale deployment app --replicas=3
 eksctl scale nodegroup --cluster=vf-eks-cluster --nodes=5 {NODE_GROUP_ID}
 ```
 You can also setup autoscaling based on CPU utilization for example;
 ```
 kubectl autoscale deployment app --min=2 --max=10 --cpu-percent=80
 ```
 #### Deploy Monitoring stack
 ```
 kubectl apply -k ./monitoring/
 ```
 This will run kustomization.yaml exists in the *monitoring* directory. kustomization.yaml will create kubernetes resources required to run monitoring system Prometheus. This will also create an AWS loadbalancer to access Prometheus.
 #### Testing Monitoring stack
 Once deployed successfully, Prometheus should be available as per below;
 ```
 http://{HOST}:9090/
 ```
 where HOST can be AWS Loadbalancer name or the IP(s) it's resolving to.
 #### Cleanup
 You can use these steps to cleanup Kubernetes resources 
 ```
 kubectl delete -k ./monitoring/
 kubectl delete -k ./
 ```
 Finally run below to delete AWS EKS cluster
 ```
 cd scripts/
 ./destroy.sh
 ```
 ## Why choose this solution?
 ## Explanation of the solution
 ## Things I wanted to do?
 ## Improvements
