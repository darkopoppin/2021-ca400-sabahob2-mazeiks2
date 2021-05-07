FROM python:3.7

WORKDIR /planning-service
ADD ./ /planning-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5003
ENV GRAPHH=f44fbd4f-5b89-4d99-838e-c4e48c2c3861
ENV YELP_API=-qkQqVfTLb3hsK477izbVvwnUqyQHwxu79M5TAt0TwGfV819k97Gjvn1IXQWjVzsRBswfhT9ZD6yeDz-rLK8AHFarhf4JKeTLVRJrvTv5hFscCbrskKMTeZ10yeVYHYx

RUN pip install --no-cache-dir -r requirements.txt
CMD ["flask", "run", "--no-debugger"]