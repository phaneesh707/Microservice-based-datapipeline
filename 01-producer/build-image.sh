docker build -t phaneesh707/producer:2.3 .
docker push phaneesh707/producer:2.3
kubectl apply -f producer-deploy.yaml