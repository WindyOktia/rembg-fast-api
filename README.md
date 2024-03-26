---
title: Remove Background
emoji: 🏢
colorFrom: green
colorTo: pink
sdk: docker
pinned: false
---

![](https://img.shields.io/badge/docker-black?logo=docker)
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
