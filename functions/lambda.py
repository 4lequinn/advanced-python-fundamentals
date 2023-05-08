# double value
# Anonym function

double_value = lambda num: num*2
#_(2,)

print(double_value(2))


caculate_square = lambda side: side**2
value = 2
print(f'Cuadrado de {value} es {caculate_square(value)}')


# Use cases
print('Lista original:')
number_list = [1,2,3,4,5,6,7,8,9,10]
print(number_list)

list_even_numbers = list(filter(lambda number: number%2 == 0,number_list))

print('Lista de números pares:')
print(list_even_numbers)


# Calculate square
print('Cuadrado de valores de la lista original:')
new_list = list(map(caculate_square,number_list))
print(new_list)