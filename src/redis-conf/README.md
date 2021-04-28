## Run redis locally
Install redis by following the instructions:
- `wget https://download.redis.io/releases/redis-6.2.2.tar.gz`
- `tar xvzf redis-6.2.2.tar.gz`
- `cd redis-6.2.2`
- `make`
- `make test`
- `make install`

Then to run the server:
- `redis-server [path]/src/redis-conf/redis.conf`

To access the server from *redis-cli*:
- `redis-cli --pass '[password from redis.conf]'`

## Run redis with Docker
Expose port 5005 in the Docker file, then:
- `docker build t [yourusername]/redis .`
- `docker run -p 5005:6379 [yourusername]/redis`
