<!-- to create kafka topic  -->
kubectl exec POD_NAME -- kafka-topics.sh --create --topic data-topic --bootstrap-server kafka-svc:9092 --partitions 3  --replication-factor 1


<!-- to check all the topics  -->
kubectl exec POD_NAME -- kafka-topics.sh --list --bootstrap-server kafka-svc:9092

<!-- keep listening to kafk-topic -->
kubectl exec POD_NAME -- kafka-console-consumer.sh --bootstrap-server kafka-svc --topic TOPIC --from-beginning


<!-- For building image and pushing to ECR -->
1. build a docker file for the app
2. build image 
3. push it to ECR
4. build a yaml file for app deployment 
5. pull the image from ECR
6. look at the ECR console on AWS for cmds 


<!-- when pods fail to start and gives crashloopbackoff -->
Jugaad - use commands and args in yaml


<!-- to run pyspark app -->
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 FILE-NAME
