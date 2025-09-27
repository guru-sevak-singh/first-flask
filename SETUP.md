### Containerization Process With docker-compose.yml file

**Here the app is converted into the docker container but the database access from the machine not inside the container**

1. Create the docker-compose file with name `docker-compose.yml`

2. update the `.env` file with `localhost` to `db` or the database container name which we setup in the docker-compose.yml file

3. Build the Container and start it with connection all the dockers Containers

`docker-compose up --build`

- here `docker-compose` command tell about the docker create the new docker image from the current directory
- start the image of container of this directory
- Build the new image from this directory

4. Add `nginx` with our application so it is able for production ready and use nginx as a loadbalancer

- create `nginx.conf` file and write the contet from `nginx.conf` file

- add `nginx` service in the `docer-compose.yml` file

    ```
    nginx:
        image: nginx:latest
        container_name: nginx-loadbalancer
        ports:
        - "80:80"
        volumes:
            - ./nginx.conf:/etc/nginx/nginx.conf:ro
        depends_on:
            - web
    ```

- once up the app by command `docker-compose up --build`

- once your service is started then use command `docker-compose up --scale web=3` or `docker-compose up --scale web=3 --build`