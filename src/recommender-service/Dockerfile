FROM python:3.7

WORKDIR /reccommender-service
ADD ./ /reccommender-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV YELP_API=-qkQqVfTLb3hsK477izbVvwnUqyQHwxu79M5TAt0TwGfV819k97Gjvn1IXQWjVzsRBswfhT9ZD6yeDz-rLK8AHFarhf4JKeTLVRJrvTv5hFscCbrskKMTeZ10yeVYHYx

RUN pip install -r requirements.txt

CMD ["flask", "run", "--no-debugger"]