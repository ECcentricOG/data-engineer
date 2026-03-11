from faker import Faker
import csv

file = open("data/data.csv", mode='w')
writer = csv.writer(file)
header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']

writer.writerow(header)

fake = Faker()

for i in range(1000):
    writer.writerow([fake.name(), fake.random_int(min=18, max=80 ,step=1),
                    fake.street_name(), fake.city(), fake.state(), fake.zipcode(),
                    fake.longitude(), fake.latitude()
                     ])
file.close()
