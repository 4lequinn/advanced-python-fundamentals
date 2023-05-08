import json



with open('people.json','r') as file:
    data = json.loads(file)

print(type(data))
print(data)