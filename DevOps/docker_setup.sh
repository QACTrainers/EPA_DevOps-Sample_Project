docker build -t epa_frontend .
docker build -t epa_backend .

docker run -d --network new_network -p 80:80 --name frontend epa_frontend
docker run -d --network new_network -p 5000:5000 --name backend epa_backend


# Removes all stopped containers
docker rm $(docker ps --filter status=exited -q)

# Removes all images
docker rmi -f $(docker images -a -q)