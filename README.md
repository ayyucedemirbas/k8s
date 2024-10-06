# k8s


```sudo docker build -t my-flask-app . ```

```sudo docker run -p 8000:8080 my-flask-app```

```docker login```

```docker tag my-flask-app yourusername/my-flask-app:latest```

```docker push yourusername/my-flask-app:latest```

```kubectl apply -f deployment.yaml```

```kubectl get pods```

```minikube service flask-app-service```
