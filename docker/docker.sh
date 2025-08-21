#!/bin/sh
# Remove all the exited containers from your host

#List the containers with basic docker command and write output to text file.
docker ps -a >> docker.txt

#using awk command the get the exited containers into text file.
awk '/Exited/ {print}' docker.txt >> exited_container.txt

#Filter out the container id's from above generated output
container_id=$(awk '{print $1}' exited_container.txt)

#iterate all the container id's using for loop and remove the containers using docker command
for id in $container_id
do 
    docker rm $id
done

#Delete the text files created above
rm docker.txt
rm exited_container.txt
