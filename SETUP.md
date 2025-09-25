### Containerization Process

1. Create the Docker File

2. Create the .dockerignore file which containes 

3. build the docker image

`docker build -t blog-app .`

4. run the docker file by connection the external database file from the computer not inside the docker container

### run the docker container in normal mode
`docker run -p 80:5000 -v ${PWD}/database.sqlite:/app/database.sqlite blog-app`

- here `docker` means initiate the docker
- `run` command to run the image
- here `-p` is for the port 
- `80:5000` it means port 80 of the maching and 5000 of the docker
- here `-v` for the flag to use the volume
- `${PWD}/database.sqlite:/app/database.sqlite` means use the database file from the main maching not the docker database file
- `blog-app` is the name of the image or the conatainer which we want to run

### run the docker in detached mode, means we can leave the terminal, it will run in background of the host

`docker run -d -p 80:5000 -v ${PWD}/database.sqlite:/app/database.sqlite blog-app`

- here `-d` means detached mode