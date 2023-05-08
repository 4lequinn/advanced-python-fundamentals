import csv

# With indexs
with open('csv/countries.csv','r',encoding='UTF-8') as file:
    reader = csv.reader(file)
    columns = next(reader)
    print(f'Columnas {columns}')
    for row in reader: 
        print(row)
        print(row[0])

# With column name
with open('csv/countries.csv','r',encoding='UTF-8') as file:
    reader = csv.DictReader(file)
    for row in reader: 
        print(row['name'])
