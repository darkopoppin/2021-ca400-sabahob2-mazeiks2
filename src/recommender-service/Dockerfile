FROM python:3.7

WORKDIR /reccommender-service
ADD ./ /reccommender-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py:app
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--no-debugger"]