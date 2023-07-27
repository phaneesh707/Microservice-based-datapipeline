#  Build Python base image
FROM python:3.9-slim AS python-base

# Add JDK to Python base image
FROM python-base AS final

# Install JDK
RUN apt-get update && apt-get install -y default-jdk 

# Set JAVA_HOME environment variable
ENV JAVA_HOME="/usr/lib/jvm/default-java"


# FROM bitnami/spark:latest
# FROM bitnami/spark:latest

#create directory
RUN mkdir /home/app

# install depndencies
RUN pip install kafka-python pyspark kafka-utils psycopg2-binary


# copy files
COPY ./consumer.py /home/app/

# set working directory
WORKDIR /home/app

# run script
CMD ["submit-spark", "consumer.py"]