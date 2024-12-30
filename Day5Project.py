import random 
import string

print("Welecome to the PyPassword Generator: ")

letters=string.ascii_letters
digits=string.digits
symbols=string.punctuation

letter_choice=int(input("how many letter would you like in your password? "))
print(letter_choice)
symbols_choice=int(input("how many symbols would you like? "))
print(symbols_choice)
number_choice=int(input("how many number would you like? "))
print(number_choice)

password=""
for char in range(1,letter_choice+1):
    password+=random.choice(letters)
for char in range(1,symbols_choice+1):
    password+=random.choice(symbols)
for char in range(1,number_choice+1):
    password+=random.choice(digits)

print(f"your password is:{password}")