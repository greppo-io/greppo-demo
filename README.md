# greppo-demo

A repository of demo apps built using Greppo. 

----
## Quickstart

1. Install `greppo` using:

```shell
$ pip install greppo
```
Note: It is recommended to install `greppo` inside a python environment.

2. Go inside one of the demo apps folders in this repository and run the command:

```shell
$ greppo serve app.py
```

3. Follow the link for the webserver.

----
## Docker Quickstart
### Build Image
docker build -t greppo-demo .  ## build image
docker images  ## list docker images

### Run docker image locally
docker run --publish 8080:8080 greppo-demo  ## start docker image


### Setup docker hub
docker login
docker tag greppo-demo <docker_hub_username>/<image-name>  ## setup tag with repo, replace with username and image name
docker push <docker_hub_username>/<image-name>  ## push to repo, replace username and image name.
