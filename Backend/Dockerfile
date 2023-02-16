FROM python:3.7

WORKDIR /epa_backend

COPY . . 

RUN pip install flask flask_cors

EXPOSE 5000

ENTRYPOINT python controller.py