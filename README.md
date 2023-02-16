# EPA-Sample_Project

## Summary 

This repo is a Sample Case Study Project for the EPA for DevOps Level 4 course. 

It contains the files and resources to complete the assessment with all KSBs being hit with pieces of code, documentation or examples of best practice condicted as part of the assessment. This project does not include all of the auxilliary documentation and proof it does meet all expectations as that will be a specific requirement for the domain you are creating for. 

The domain and brief for this example project is to create a CRUD Multi tiered architecture project utilising an API powered backend (Python using Flask), a static HTML being served with nginx and an embedded SQL database within the backend application. 

Further than just the software side it has be containerised using Docker (and docker compose), deployed with Kubernetes, on a provisioned AWS environment using Terraform. In order to control this process, it is managed by a GitHub CI CD Actions workflow file. All required code and information is stored within the DevOps directory of this repo.

## Example Brief

You have been hired as a Software & DevOps Engineer for a popular high street music shop QA Records that sell albums. They require a method of storing and updating orders that are made in the record shop. They require a Graphical User Interface to allow customers to create and view orders as well as an admin page allowing the store owner to edit the list of albums and edit the orders. 

In order for the order management system to be effective they need to do the following: 
- Create a Record
- Real all records
- Read record by ID
- Update record by ID
- Delete record by ID
- Delete all Records
- Query records by search term
- Read an order by ID
- Read all orders
- Update an order by ID
- Delete an order by ID
- Delete all orders

The owners of QA Records are requesting the data for orders be stored within some form of SQL database and are open to more functionalities being added. 
The shop is also looking into the benefit of adopting a DevOps mindset throughout this project and would like to explore the possibility of utilising a CI/CD pipeline for their releases. This pipeline would need to automate, containerise, and release versions of the order management system.


# Running

## Prerequisites

In order to run this application as a cloud hosted project you will need the following:

- AWS environment with access to VPC, EC2, IAM, Roles, EKS
- EC2 of atleast t2.small within the AWS Environment
- IAM Access and Secret Access Key saved
- SSH access to Setup EC2

## Running 

You should start with forking this repo to your own personal profile so you can push changes. 

Within the forked repo you have to add GitHub Actions secrets for DockerHub, add your username under `DOCKER_USERNAME` and your password under `DOCKER_PASSWORD`

Within your setup EC2 git clone the forked repo down and navigate to the DevOps directory `cd /DevOps`

Run the `./setup.sh`file to install terraform, awscli and kubectl. 

Navigate to the `/terraform` directory and create a file called `terraform.tfvars` and add the following (entering your own AWS keys) 

```
access_key = "Your access key"
secret_key = "Your Secret Key"
```

Ensure the `.gitignore` is working correctly and the `.tfvars` file is not being pushed up to github, this can be checked with a `git status` and seeing if the file is not being tracked.

Within the `/terraform` directory run the `tf_deploy.sh` file to prepare, plan and run the terraform IaC. This process is automated and should take approx 25 minutes to provision all of the necessary infrastructure. 

Once everything has been installed and created navigate to the `k8s` directory with `cd ../k8s`.
Modify the `backend.yaml` and `frontend.yaml` image attributes so they connect to your personal DockerHub account `image: reeceqa/epa_frontend` to use your image rather than the default image. This could be improved with using `secrets` to pass in Env Vars for the DockerHub account.

Run the `./deploy.sh` to setup the K8s cluster, apply the k8s manifest files and print the services. 

Once the manifests have been applied wait approx 2 minutes and run the command `kubectl get svc` to print the services and make note of the external IP on the `load balancer` service. This URL is how you access the application, in order for the application to fully work you must edit the .js files of the /Frontend/WebApp and replace the existing URL with the external IP you have copied.  

Push these changes to your repo with the following: 
```
git add . 
git commit -m "Modified .js files" 
git push
```

By pushing new code to GitHub it forces the workflow file to run which will lint, test, build and pushing the image to DockerHub. 

Once the GitHub workflow has run and passed the checks your images will be pushed up to your personal DockerHub and can be accessed by <dockerHub username>/epa_frontend and epa_backend we can force the K8s deployment to update with the command `kubectl rollout frontend` and `kubectl rollout backend`
  
To access the application go to your web browser and access the Load Balancer external IP, it should open up the web page and will contain all necessary functionality. 
  
## Project Structure
  
The Cloud structure with the Setup EC2 will look like below: 
  <br>
  <br>
![Cloud Environment](/Project_Planning/images/Cloud_Environment.png) 
  <br>
  <br>
Kubernetes structure with routes and networking looks like: 
  <br>
  <br>
![Cloud Environment](/Project_Planning/images/K8s_routes.png) 
  <br>
  <br>
GitHub Actions stages and process: 
  <br>
  <br>
![Cloud Environment](/Project_Planning/images/GitHub_CI CD.png) 
  <br>
  <br>
Routes of the backend and the simplified Backend <-> Frontend connection: 
  <br>
  <br>
![Cloud Environment](/Project_Planning/images/Frontend and Backend.drawio.png) 
  
  
## Documentation
  
Further documentation about the project can be found in the `/project_planning` directory with Risk Assessment, KSB assigning and the brief of this project 

