# string='artificial intelligence'
# print(len(string))
# print(string.upper())
# print(string.lower())
# print(string.index('i'))


# source = input("Type your text:\n")

# if len(source) > 5: 
#     print("It's more than 5")
# elif len(source) < 5: 
#     print("It's less than 5")
# else:
#     print("It's exactly 5")

# string = input("Enter a string: ").lower() 
# letter = input("Enter a letter to detect: ").lower()

# if letter in string:
#     print(f"The letter '{letter}' is present in the string.")
# else:
#     print(f"The letter '{letter}' is not present in the string.")


# string='artificial intelligence'
# name=input('type ur name:\n')
# print(f'{name} loves {string}')




# number = float(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")



# text = input("Enter ur text: ")
# print(text[::-1])

# name=input('type ur name:\n').upper()
# last_name=input('type ur last name:\n').upper()
# print(f'{name[0]} {last_name[0]}')




# side_length = float(input("Enter the side length of the square: "))

# if side_length > 0:
#     perimeter = 4 * side_length 
#     surface_area = side_length ** 2  
#     print(f"The perimeter is: {perimeter}")
#     print(f"The surface area is: {surface_area}")
# else:
#     print("Please enter a valid positive number for the side length.")

string='Artificial Intelligence'
new_string=string.replace('A', 'a').replace('I', 'i')
print(new_string)