# get image
FROM python

# code directory
RUN mkdir /app

# install depndencies
RUN pip install kafka-python 

# copy files
COPY ./producer.py /app/producer.py

# set working directory
WORKDIR /app

# run script
CMD ["python","producer.py"]