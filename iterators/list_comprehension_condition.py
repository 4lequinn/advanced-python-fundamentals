def calculate_square(number): return number**2

def is_even_number(number): return number % 2 == 0

# Without conditions
list_numbers = [1,2,3,4,5,6,7,8,9]
print(list_numbers)

# 1 condition
list_comprehension = [calculate_square(number) for number in list_numbers if is_even_number(number)]
print(list_comprehension)

# 2 Conditions
results = [calculate_square(number) if is_even_number(number) else 0 for number in list_numbers]
print(results)