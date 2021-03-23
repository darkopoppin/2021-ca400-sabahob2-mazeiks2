FROM python:3.6-slim-buster
WORKDIR /user-information
ADD ./ /user-information
RUN python -m pip install -r requirements.txt
CMD ["python","app.py"]