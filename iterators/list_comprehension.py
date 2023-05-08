def calculate_square(number): return number**2

list_numbers = [1,2,3,4,5,6,7,8,9]
list_comprehension = [number**2 for number in list_numbers]
list_comprehension = [calculate_square(number) for number in list_numbers]
print(list_comprehension)