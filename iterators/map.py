def calculate_square(number):
    return number**2

number_list = [1,2,3,4,5,6,7,8,9]

"""
square_list = list()

for number in number_list:
    square = calculate_square(number)
    square_list.append(square)

print(square_list)    
"""

square_map = map(calculate_square,number_list)
print(list(square_map)) 
