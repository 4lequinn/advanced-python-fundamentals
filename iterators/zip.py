names = ['Jorge','Matías']
last_names = ['Quintui','Quintui']

fullname = list(zip(names,last_names))

print(fullname)


names_unzip, last_names_unzip = zip(*fullname)
print(names_unzip)
print(last_names_unzip)

for name, lastname in zip(names,last_names):
    print(name,lastname)