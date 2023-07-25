# get image
FROM python

# code directory
RUN mkdir /app

# install depndencies
RUN pip install kafka-python Faker


# copy files
COPY ./producer.py /app/producer.py
COPY ./data.csv /app/data.csv

# set working directory
WORKDIR /app

# run script
CMD ["python","producer.py"]