# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.

FROM sanicframework/sanic:LTS

LABEL Name=my_sanic_app Version=0.0.1
EXPOSE 8010

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
# WORKDIR /app
# COPY ./app /app

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["tail", "-f", "/dev/null"]

