list_numbers = [1,2,3,4,2,3,5,5,6,7,4,3]

set_even_number = {number for number in list_numbers if number % 2 == 0}
print(set_even_number)

vowels = "aeio"
dictionary = {vowel.lower(): vowel.upper() for vowel in vowels}
print(dictionary)