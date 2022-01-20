
# write some code to build your image
FROM python:3.8-buster

COPY api.py api.py
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
