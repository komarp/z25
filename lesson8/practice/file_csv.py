import csv

file = open('../../data.csv')
reader = csv.DictReader(file)
print(list(reader))
file.close()

data = [
    {
        'first_name': 'Tima',
        'last_name': 'Akulich'
    },
    {
        'first_name': 'John',
        'last_name': 'Doe'
    }
]
file = open('../../data_new.csv', 'w')
writer = csv.DictWriter(file, ('first_name', 'last_name'))
writer.writeheader()
writer.writerows(data)
file.close()
