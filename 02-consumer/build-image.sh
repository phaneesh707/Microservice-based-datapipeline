docker build -t phaneesh707/consumer:2.0 .
docker push phaneesh707/consumer:2.0
kubectl apply -f consumer-deploy.yaml