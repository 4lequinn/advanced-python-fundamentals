names = ['Jorge','Matías','Krishna']
for element in names:
    if element == 'Matías': break
    print(f'Break - {element}')

for element in names:
    if element == 'Matías': continue
    print(f'Continue - {element}')