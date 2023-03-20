FROM alpine

WORKDIR /home/isifoo/Portflio/Docker

COPY requirements.txt /home/isifoo/Portflio/Docker
COPY ProjectManager /home/isifoo/Portflio/Docker

RUN apk update && apk add python3 py3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python3 manage.py runserver

EXPOSE 8000
