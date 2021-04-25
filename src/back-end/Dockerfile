FROM python:3.6

WORKDIR /user-information
ADD ./ /user-information

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV YELP_API=f-625oQS3C7MH4ksSS2Bz30c5vtkbg669c4DHqzqrrmMStzihXNwEClzXZ6vrya_38Ol2aw0Inf6z90IePHjjAG7UZGCDhXbP3hhskIGaiyygD15bhvUtqsb6swjYHYx
# the redis pass should be in single quotes because it contains bash syntax
ENV REDIS_PASS='K4Ws$$65?}z$e:p\qm7_ycu<Ak]k:}m$'

EXPOSE 5000
RUN python -m pip install -r requirements.txt
CMD ["flask", "run", "--no-debugger"]