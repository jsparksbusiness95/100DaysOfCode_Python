import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
pass_generated = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# print(random.choice(letters)

for num in range(nr_letters):
    letter_select = random.choice(letters)
    pass_generated.append(letter_select) # Appends to end of list
    num -= num

for num in range(nr_numbers):
    number_select = random.choice(numbers)
    pass_generated.append(number_select) # Appends to end of list
    num -= num

for num in range(nr_symbols):
    symbol_select = random.choice(symbols)
    pass_generated.append(symbol_select) # Appends to end of list
    num -= num

random.shuffle(pass_generated) # Shuffles the list retroactively after data has been inserted.
print("".join(pass_generated))