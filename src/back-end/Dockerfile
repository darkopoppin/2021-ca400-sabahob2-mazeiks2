FROM python:3.6

WORKDIR /user-information
ADD ./ /user-information

ENV DOCKERIZE_VERSION v0.6.1

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV YELP_API=-qkQqVfTLb3hsK477izbVvwnUqyQHwxu79M5TAt0TwGfV819k97Gjvn1IXQWjVzsRBswfhT9ZD6yeDz-rLK8AHFarhf4JKeTLVRJrvTv5hFscCbrskKMTeZ10yeVYHYx
# the redis pass should be in single quotes because it contains bash syntax
ENV REDIS_PASS='K4Ws$$65?}z$e:p\qm7_ycu<Ak]k:}m$'

ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5144
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C ./ -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN python -m pip install -r requirements.txt