### Setup the PostgreSQL for the application

1. open postgresql in terminal

`psql -U postgres`

2. create a database 

` CREATE DATABASE blog_db;`

3. create a user

`CREATE USER bloguser WITH PASSWORD 'secret@123';`

4. gave all the privileges on database

`GRANT ALL PRIVILEGES ON DATABASE blog_db TO bloguser;`

5. make the created uesr as owner of the new db

` ALTER DATABASE blog_db OWNER TO bloguser;`

6. GRANT Usage and Rights on Schima to the user

```
GRANT ALL ON SCHEMA public TO bloguser;

ALTER SCHEMA public OWNER TO bloguser;
```
5. quit the postgreSQL

`\q`

6. install the dependency in python help to connect the postgreSQL with our python code

`pip install psycopg2-binary`

7. update the db location from `database.sqlite` to `postgresql locationo`

`postgresql://bloguser:secret@123:5432/blog_db`

8. do the migration if needed or you can also crete from new db by `db.create_all()`

9. before creatign the docker image some configuration  with posgreSQL
- updte the pg_hba.conf file and add `sudo nano /etc/postgresql/<version>/main/pg_hba.conf`

    `host    all    all    172.17.0.0/16    md5`

- update the allowed  host in postgresql.conf `sudo nano /etc/postgresql/<version>/main/postgresql.conf`

    `listen_addresses = '*'`

10. once restart the postgreSQL or restart the server or computer.