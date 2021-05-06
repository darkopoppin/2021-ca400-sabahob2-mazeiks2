FROM python:3.7

WORKDIR /planning-service
ADD ./ /planning-service

ENV GOOGLE_APPLICATION_CREDENTIALS=credentials/citycydev-firebase.json
ENV FLASK_APP=run.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5003
ENV GRAPHH=f44fbd4f-5b89-4d99-838e-c4e48c2c3861
ENV YELP_API=b7wSeZeFykMFbPx-n7VpQD9gwi8EZWYYjaPEoa3ExSZv5c4LlGpANEhKR-sUW51218X6M3RO6t90tQGvbBAcX7pP9A3KnEo8FRfYZ1t1efZ_SXvj7POdAmmyqptTXnYx

RUN pip install --no-cache-dir -r requirements.txt
CMD ["flask", "run", "--no-debugger"]