# Introduction
This project will deploy a simple Python based API. It has couple of POST methods. You can use one method to insert date-time stamp into your database while one method to see existing data from the database. The application is scaleable and have persistent data in case of application failure or unexpected crash of database.

## Logical design and Architecture diagram
![Logical Design](images/logical_design.png)
![Architecture Diagram](images/architecture.png)

## How to test if solution is working?
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
* [Amazon CLI](https://aws.amazon.com/cli/)
* [Amazon EKS CLI](https://eksctl.io/)
* [Kubernetes CLI](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* [Docker](https://docs.docker.com/get-docker/)
 #### Get source code
 ```
  git clone git@github.com:abubakar-malik/vf.git
 ```
 #### Create Docker image
 ```
 cd docker/
 sudo docker build --tag vf .
 sudo docker login --username=abual
 sudo docker images
 sudo docker tag 3c537760ae99 abual/vf:latest
 sudo docker images
 sudo docker push abual/vf:latest
 ```
 ## Monitoring

 ## Improvements
