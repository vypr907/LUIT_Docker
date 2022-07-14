FROM nginx

COPY . /app

WORKDIR /app

EXPOSE 80

HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:8080 || nc -zv localhost 8080 || exit 1

RUN apt-get update && apt-get -y install python3

CMD ["python3","./deployDate.py"]

COPY ./index.html /usr/share/nginx/html/index.html

COPY ./deployment.txt /usr/share/nginx/html/deployment.txt

CMD tail -f /dev/null