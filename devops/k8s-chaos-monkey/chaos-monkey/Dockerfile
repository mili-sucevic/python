FROM python:3.8-slim-buster

COPY chaos-monkey.py /app/chaos-monkey.py

RUN pip install kubernetes schedule

CMD [python, /app/chaos-monkey.py]
