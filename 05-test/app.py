import csv
from faker import Faker
import random

def generateRow(fake):
    order_id = fake.uuid4()[:8].upper()  
    customer_id = fake.random_int(min=1000, max=9999)
    product_id = f"PROD{fake.random_int(min=1, max=100):03}"
    unit_price = round(random.uniform(10, 1000), 2)
    quantity = fake.random_int(min=1, max=10)
    order_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    category = fake.random_element(elements=('Electronics', 'Clothing', 'Books', 'Toys'))
    city = fake.city()

    return [order_id, customer_id, product_id, unit_price, quantity, order_date, category, city]

def generateOrders(outputFile,row_count):
    fake = Faker(['en_IN'])
    field = ["OrderId","CustomerId","ProductId","UnitPrice","Quantity","OrderDate","Category","City"]
    with open(outputFile,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(field)
        for i in range(row_count):
            new_row = generateRow(fake)
            writer.writerow(new_row)




if __name__ == '__main__':
    outputFile = "data.csv"
    row_count = 1000

    generateOrders(outputFile, row_count)
    print("Orderes data created successfully.")