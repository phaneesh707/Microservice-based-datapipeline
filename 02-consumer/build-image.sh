docker build -t phaneesh707/consumer:2.7 .
docker push phaneesh707/consumer:2.7
kubectl apply -f consumer-deploy.yaml