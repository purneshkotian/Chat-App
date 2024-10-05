# Chat-App

Real-Time Chat Application with Django Channels

### You can run redis server using below command in docker

`docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest`

### Running Chat application

Use `daphne -b 0.0.0.0 -p 8000 chat_app.asgi:application` to run server locally
_`python manage.py runserver` works for normal WSGI connection i.e http connection_
_for using websocket connection we need to use daphne_

### Use two separate tabs to verify if the ws connection is working and chat is visible
