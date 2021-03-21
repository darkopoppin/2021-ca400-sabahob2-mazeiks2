FROM python:3.6-slim-buster
WORKDIR /Docker
ADD ./ /Docker
RUN python -m pip install -r requirements.txt
CMD ["python","app.py"]