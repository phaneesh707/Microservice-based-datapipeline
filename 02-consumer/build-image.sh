docker build -t phaneesh707/consumer:2.2 .
docker push phaneesh707/consumer:2.2
kubectl apply -f consumer-deploy.yaml