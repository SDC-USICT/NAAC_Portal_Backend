FROM frolvlad/alpine-python3
WORKDIR /src
ADD . .
EXPOSE 80
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 manage.py runserver 0.0.0.0:80