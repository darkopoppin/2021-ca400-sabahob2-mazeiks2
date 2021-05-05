FROM python:3.7

WORKDIR /reccommender-service
ADD ./ /reccommender-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV YELP_API=XcU9cdJYOY3QyrKgbsomrMpf79P27i5SfFztzGUBANte6K6t3V7yqa0uewbcxBfhkvEwoMgRwZv3--s4g7h2a6LliVwH2ZuoeCedToofpC1xDjm24tKrlybmjrmSYHYx

RUN pip install -r requirements.txt

CMD ["flask", "run", "--no-debugger"]