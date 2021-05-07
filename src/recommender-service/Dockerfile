FROM python:3.7

WORKDIR /reccommender-service
ADD ./ /reccommender-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5001
ENV YELP_API=TcqBLne8S_-RzVwebu7ozPWddmjVmoq2vNJn9Ma0ScMV6_0OkRnsejiF3eC5BphraKVna5BJgsf9nrPn-3wrn1-2De0RSg88M1FysrTRavrVSeADQV0_3YZmAD6UYHYx

RUN pip install -r requirements.txt

CMD ["flask", "run", "--no-debugger"]