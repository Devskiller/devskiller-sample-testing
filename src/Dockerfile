FROM python:3.8-alpine3.10

ENV FLASK_APP=main.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY start.sh /start.sh
COPY main.py /main.py
COPY templates /templates

ENTRYPOINT ["/start.sh"]
EXPOSE 5000