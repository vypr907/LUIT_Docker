FROM nginx

COPY ./app/ .
COPY ./app/web/index.html /usr/share/nginx/html/index.html

WORKDIR /app

EXPOSE 8080

ENTRYPOINT ["/bin/sh"]

HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:8080 || nc -zv localhost 8080 || exit 1

CMD ["deployDate.py"]