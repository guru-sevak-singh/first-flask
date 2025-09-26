**Additionals with docker-compose**

1. Just to stop the docker use the command 

`docker-compose down`

2. If need to delete the volume also with the container user command

`docker-compose down -v`

3. If need to backup the database regulerly use the command

`docker exec -t postgres_db pg_dump -U bloguser blog_db > backup.sql`

- `docker` command will start the program docker for us
- `exec` command means we want to execute something inside the docker
- `postgres_db` -> conatainer name of our db
- `pg_dump -U` command to dump the selected database
- `blog_db` name of the database
- `> backp.sql` will create a backup file in the folder