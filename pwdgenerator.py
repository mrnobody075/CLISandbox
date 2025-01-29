import random
import string  


letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = string.digits         # '0123456789'
symbols = "!#$%&()*+"

print("Welcome to the PyPassword Generator!")

# Input validation
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Enter a valid number.")

nr_letters = get_positive_int("How many letters would you like in your password?\n")
nr_symbols = get_positive_int("How many symbols would you like?\n")
nr_numbers = get_positive_int("How many numbers would you like?\n")

# Generate random characters
password_list = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)

# Shuffle password list
random.shuffle(password_list)

# Convert list to string
password = "".join(password_list)

print(f"\nYour secure password is: {password}")
