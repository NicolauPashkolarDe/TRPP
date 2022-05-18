FROM ubuntu:20.04
COPY . /app
RUN apt update \
	&& apt install -y python3 fortune \
     	&& cd /usr/bin \
	&& ln -s python3 python
ENTRYPOINT ["python", "./app/main.py"]
