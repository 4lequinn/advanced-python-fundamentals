import json

people = {
    'name' : 'Jorge',
    'age' : 22
} 

object_json = json.dumps(people,indent=2)

with open('people.json','w') as file:
    file.write(object_json)