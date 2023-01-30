import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passw_arr = []

for nr_l in range(0, nr_letters):
    passw_arr.append(random.choice(letters))
for nr_n in range(0, nr_numbers):
    passw_arr.append(random.choice(symbols))
for nr_s in range(0, nr_symbols):
    passw_arr.append(random.choice(numbers))

print(f"your password is : {passw_arr}")
random.shuffle(passw_arr)
print(f"your password is : {passw_arr}")
passw = ""
for letter in passw_arr:
    passw += letter

print(f"your password is : {passw}")
