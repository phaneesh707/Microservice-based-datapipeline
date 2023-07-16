# Stage 1: Build Python base image
FROM python:3.9-slim AS python-base

# Stage 2: Add JDK to Python base image
FROM python-base AS final

# Install JDK
RUN apt-get update && apt-get install -y default-jdk

# Set JAVA_HOME environment variable
ENV JAVA_HOME="/usr/lib/jvm/default-java"

#create directory
RUN mkdir /app

# install depndencies
RUN pip install kafka-python pyspark kafka-utils


# copy files
COPY ./consumer.py /app/

# set working directory
WORKDIR /app

# run script
CMD ["python", "consumer.py"]