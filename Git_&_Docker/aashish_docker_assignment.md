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


