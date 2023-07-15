FROM python:3.9

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