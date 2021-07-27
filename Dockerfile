FROM python:3.7.9
# INSTALLING FFMPEG
RUN apt-get update
RUN apt-get install zsh -y

ADD requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /workspace
ADD entrypoint.sh /workspace
EXPOSE 8000

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]