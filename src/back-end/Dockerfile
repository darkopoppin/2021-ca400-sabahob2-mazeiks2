FROM python:3.6

WORKDIR /user-information
ADD ./ /user-information

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py:app
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
RUN python -m pip install -r requirements.txt
CMD ["flask", "run", "--no-debugger"]