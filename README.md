# simple echo server

Useful web app for debugging Docker or Kubernetes

Run in docker:
```
docker build . -t test-web-server:v0.1.0
docker run --rm -p 8080:8080 test-web-server:v0.1.0
```
