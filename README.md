# greppo-demo

A repository of demo apps built using Greppo.

---

## Quickstart

1. Install `greppo` using:

```shell
pip install greppo
```

Note: It is recommended to install `greppo` inside a python environment.

2. Go inside one of the demo apps folders in this repository and run the command:

```shell
greppo serve app.py
```

3. Follow the link for the webserver.

---

## Deployment Quickstart (Docker)

### Build Image

Configure the container's image using the example `Dockerfile` provided.

Change `line 6` in the `Dockerfile: COPY /{folder-name} .` with the `{folder-name}` to the source folder, or the demo folder of choice. In the example in the Dockerfile we use the `vectore-demo`.

```shell
## build image
docker build --tag greppo-vector-demo .
## list docker images
docker images
```

### Run docker image locally

```shell
## start docker image, use the --publish option to expose the port (one the app running within the container uses: 8080) to the outside (5000).
## Check the app locally at http://0.0.0.0:5000

docker run --publish 5000:8080 greppo-vector-demo
```

### Setup docker hub and push the image

```shell
docker login
## setup tag with repo, replace with username and image name
## you need to tag the image to be pushed, here we use the tag of greppo-vector-demo
docker tag greppo-vector-demo <docker_hub_username>/<image-name>
## push to repo, replace username and image name.
docker push <docker_hub_username>/<image-name>
```

### Deploying container

-   [GCP](https://cloud.google.com/run/docs/deploying)
-   [AWS](https://www.amazonaws.cn/en/getting-started/tutorials/deploy-docker-containers/)
