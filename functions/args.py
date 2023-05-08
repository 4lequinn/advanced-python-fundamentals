# *args -> Tuple (n..n args)
def calculate_perimeter(*args):
    perimeter =  0
    for side in args: perimeter+=side
    return perimeter

perimeter = calculate_perimeter(1,2,3,4,5,6)
print(perimeter)