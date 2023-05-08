## Walrus operator
print('Ingrese un valor o escriba salir:')
while (line := input()) !=  'salir': print(line)

def calculate_square(number): return number**2
list_numbers = [1,2,3,4,5,6,7,8,9]
list_comprehension = [square for number in list_numbers if (square:=calculate_square(number)) %2 == 0 ]
print(list_comprehension)