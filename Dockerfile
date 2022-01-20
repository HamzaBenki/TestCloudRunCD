
# write some code to build your image
FROM python:3.8-buster

RUN pip install -U pip
RUN pip install fastapi uvicorn

COPY api.py api.py

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
