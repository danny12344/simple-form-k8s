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

#### Deploy to GKE:

Create cluster:
```bash
gcloud container clusters create-auto backend --region=europe-west2
```

Deploy app
```bash
kubectl create deployment api-app -- image=europe-west2-docker.pkg.dev/k8s-learning-390219/cloud-run-source-deploy/backend:latest
```

Expose app to the internet
```bash
kubectl expose deployment api-app --type LoadBalancer --port 8080 --target-port 8080
```

Deploy to GCR:

```bash
gcloud run deploy
```