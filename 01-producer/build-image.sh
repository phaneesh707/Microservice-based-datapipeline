docker build -t phaneesh707/producer:2.1 .
docker push phaneesh707/producer:2.1
kubectl apply -f producer-deploy.yaml