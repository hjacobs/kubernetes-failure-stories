FROM python:3.7-alpine3.9

RUN pip install requests markdown

COPY update.py /
COPY template.html /

WORKDIR /workdir

ENTRYPOINT ["python", "/update.py"]

