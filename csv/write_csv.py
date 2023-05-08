import csv

columns = ['name','age']

data = ['Jorge',22]

with open('data.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(columns)
    writer.writerow(data)


data_list = [
    ['Jorge',22],
    ['Mati',17],
    ['Krishna',20],
]


with open('data.csv','w',newline='') as file:
    writer = csv.writer(file,delimiter=',')
    writer.writerow(columns)
    writer.writerows(data_list)


# Dictionaries
data_dict = [
    {'name':'Jorge','age':22},
    {'name':'Krishna','age':20},
]

with open('data.csv','w',newline='') as file:
    writer = csv.DictWriter(file,fieldnames=columns)
    writer.writeheader()
    writer.writerows(data_dict)

