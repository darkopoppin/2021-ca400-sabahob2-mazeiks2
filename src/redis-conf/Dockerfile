FROM redis:6.2.2
COPY redis.conf /usr/local/etc/redis/redis.conf
# Uncomment if you running the container with Docker run
# EXPOSE 5005
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]