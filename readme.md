<!-- to create kafka topic  -->
kubectl exec POD_NAME -- kafka-topics.sh --create --topic data-topic --bootstrap-server localhost:9092 --partitions 3  --replication-factor 1


<!-- to check all the topics  -->
kubectl exec POD_NAME -- kafka-topics.sh --list --bootstrap-server localhost:9092

<!-- keep listening to kafk-topic -->
kubectl exec POD_NAME -- kafka-console-consumer.sh --bootstrap-server kafka-svc --topic TOPIC --from-beginning


<!-- For building image and pushing to ECR -->
1. build a docker file for the app
2. build image 
3. push it to ECR
4. build a yaml file for app deployment 
5. pull the image from ECR
6. look at the ECR console on AWS for cmds 







