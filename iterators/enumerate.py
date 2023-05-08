names = ['Jorge','Matías','krishna']
enumerate_names = list(enumerate(names,start=5))
print(enumerate_names)

for index, element in enumerate(names):
    print(index,element)