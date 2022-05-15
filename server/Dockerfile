FROM python:3

ADD simpleServer.py /

COPY server_config.config ./

RUN pip install fastapi

RUN pip install uvicorn

RUN pip install requests

CMD [ "python", "./simpleServer.py" ]
