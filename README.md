# Simple Containerised form webapp

Contains containerised frontend & seperately containerised backend

## What it does:

- takes input from username & password fields
- stores them in python variables in fastapi backend

## Dockerfile for deploying to Google Cloud Run

### <u>Instructions to run locally</u>

Build docker images:

```bash
docker build -t formapi .
docker build -t frontend .
```

Run docker images:

```bash
docker run -it -p 8080:8080 formapi
docker run -it -p 8000:80 frontend
```

### <u>Instructions to deploy</u>


Initialise Google Cloud CLI:
```bash
gcloud init
```

Deploy to GCR:

```bash
gcloud run deploy
```