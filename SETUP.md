### Containerization Process With docker-compose.yml file

**Here the app is converted into the docker container but the database access from the machine not inside the container**

1. Create the docker-compose file with name `docker-compose.yml`

2. update the `.env` file with `localhost` to `db` or the database container name which we setup in the docker-compose.yml file

3. Build the Container and start it with connection all the dockers Containers

`docker-compose up --build`

- here `docker-compose` command tell about the docker create the new docker image from the current directory
- start the image of container of this directory
- Build the new image from this directory