### Containerization Process

**Here the app is converted into the docker container but the database access from the machine not inside the container**

1. Create the Docker File

2. Create the .dockerignore file which containes 

3. build the docker image

`docker build -t blog-app .`

4. run the docker file by connection the external database server from the computer not inside the docker container and location of db is already in the `.env` file

### here we run just
`docker run -p 80:5000 blog-app`

- here `docker` means initiate the docker
- `run` command to run the image
- here `-p` is for the port 
- `80:5000` it means port 80 of the maching and 5000 of the docker
- `blog-app` is the name of the image or the conatainer which we want to run
