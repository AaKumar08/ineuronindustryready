## Assignment 1
### 15 basic docker commands

#### 1. docker --version 
#### Explaination - It shows the version of docker installed in your local
!['docker version command '](./images/docker_1.PNG)

#### 2. docker run -d -p 80:80 docker/getting-started
#### -d - run the container in detached mode (in the background)
#### -p 80:80 - map port 80 of the host to port 80 in the container
#### docker/getting-started - the image to use
!['docker run command'](./images/docker_2.PNG)

#### 3. docker pull docker/getting-started
#### To pull (aka download) the docker image from docker hub to your local machine.
!['pull command'](./images/pull.PNG)

#### 4. docker images
#### To list all the docker images present in your local machine.
!['List images'](images/list_all_images.PNG)

## Yeah buddy!! We have implemented 4 commands. Let's keep up the good work.
!['Work is fun'](images/kungu_panda_1st.jpg)

#### 5. docker ps
#### To list all the docker containers which are in running state in your local machine.
!['List of running containers'](images/list_all_running_containers.PNG)

#### 6. docker ps --all
#### To list all the docker containers which are in running state as well as those are in stopped state in your local machine.
!['List all containers including the stopped containers'](images/list_all_conatiners.PNG)

#### 7. docker stop
#### To stop a running container
!['To stop a running container'](images/stop.PNG)

#### Wow!! this is awesome. Like it is easy to start, run, stop and see the containers....
!['Wow'](images/panda_2.jpg)

#### 8. docker stop
#### To restart a stopped container
!['Stop'](images/stop.PNG)

#### 9. docker rename
#### To rename a container
![](images/rename.PNG)

#### 10. docker logs
#### To fetch the logs from a specified container
![](images/logs.PNG)

#### 11. docker rm
#### To remove container, first stop it and then remove it.
![](images/remove_container.PNG)

#### 12. docker rmi
#### Remove a image
![](images/remove_image.PNG)

#### 13. docker command --help 
#### To get help
![](images/to_get_help.PNG)

#### 14. To run commands inside the container
![](images/exec.png)

#### 15. docker kill container_id
#### To kill the container immediately
![](images/kill.PNG)

#### Yayy!!!! Assignment 1 Done...
![](images/thanku.jpg)

## Assignment 2
#### Hello World Docker Image Run Hello World Docker Image Locally.
![](images/hello_world.PNG)

## Assignment 3
#### Create a hello world flask application. Create a Dockerfile for your flask hello world application. Build Docker image using Docker file. Run docker image build in previous step. Push your Docker image to Docker Hub.
![](images/docker_file_1.PNG)
![](images/docker_push.PNG)

## Assignment 4
#### Automate Assignment below task using github action.
####
#### 1. Build Docker Image
#### 2. Push Docker Image to Docker hub.

