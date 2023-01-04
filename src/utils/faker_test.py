from faker import Faker

fake = Faker()
fake.random.seed(1234)


print(fake.date_time())
print(fake.name())
print(fake.text())


for _ in range(15):
    print(fake.name())