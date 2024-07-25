---
title: Remove Background
emoji: 🏢
colorFrom: green
colorTo: pink
sdk: docker
pinned: false
---

[![](https://img.shields.io/badge/docker-black?logo=docker)](https://hub.docker.com/repository/docker/c2pcmd/remove_background_api)
![](https://img.shields.io/badge/FastAPI-black?logo=fastapi)

## This is a dockerized FastAPI app to remove background from images using [rembg](https://github.com/danielgatis/rembg)

### How to run
```shell
git clone https://github.com/c2p-cmd/rembg-fast-api/
cd rembg-fast-api
docker build -t rembgapi .
docker run --rm -p 0.0.0.0:7860:7860 rembgapi
```
Then open `http:localhost:7860/` in your browser and done!

### Run with docker image directly
```shell
docker pull c2pcmd/remove_background_api
docker run --rm -p 0.0.0.0:7860:7860 c2pcmd/remove_background_api
```

### Live Demo on [🤗 Spaces](https://huggingface.co/spaces/c2p-cmd/remove-background-ai)
<iframe
	src="https://c2p-cmd-remove-background-ai.hf.space"
	frameborder="0"
	width="850"
	height="450"
></iframe>
