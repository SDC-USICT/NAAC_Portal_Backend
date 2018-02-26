FROM frolvlad/alpine-python3
RUN apk add --no-cache sqlite
RUN apk add --no-cache libmagic
WORKDIR /src
ADD . .
EXPOSE 80
RUN pip3 install -r requirements.txt
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD python3 manage.py runserver 0.0.0.0:$PORT
