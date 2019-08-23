# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.

FROM sanicframework/sanic:LTS

LABEL Name=my_sanic_app Version=0.0.1
EXPOSE 8010

ENV PYTHONUNBUFFERED 1

RUN apk add git
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

CMD ["tail", "-f", "/dev/null"]
# CMD ["python", "start_app.py"]

