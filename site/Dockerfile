FROM python:3.8-slim

RUN pip install requests markdown

COPY update.py /
COPY template.html /

WORKDIR /workdir

ENTRYPOINT ["python", "/update.py"]

