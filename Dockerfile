
# write some code to build your image
FROM python:3.8-buster

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api.py api.py

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
