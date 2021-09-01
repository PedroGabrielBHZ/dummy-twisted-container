# twisted-docker
A basic example to deploy a Twisted application as a Docker container.

# Requirements
- Python 3.x
- Docker (just get the latest, I guess)
- Docker Compose (idem)

# Dockerfile

The Dockerfile installs all necessary requirements to properly run twisted in a *nix environment.

## Server Config

### Port
Just set an environment variable called **ECHO_SERVER_PORT** and define a value.

By default, the server will run at the 8000 port. 

# Running on Docker

```
git clone `this repo's link`
export ECHO_SERVER_PORT=5000
cd twisted-docker/server
docker-compose up
```

After the image, the container will be started. Check with:

```
docker ps
```

When the container starts, just access:

[http://192.168.99.100:5000](http://192.168.99.100:5000) and you should see the responder from the echo server.

* Your docker IP may vary.

# Running locally

You also can run the app locally (not the same fun!)
Follow this steps:

```
git clone `this repo's link`
cd `into it`
pip3 install -r requirements.txt
export ECHO_SERVER_PORT=5000
twistd --nodaemon --python run_server.py
```

Access: [http://localhost:5000](http://localhost:5000) and you should see the responder from the echo server.

