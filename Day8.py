# def greet(): # Without input
#     print("Hello Everyone")
#     print("Good Morning")
#     print("Welcome to the jungle")
# greet()

# def greet(name): # With input
#     print(f"Hello {name}")
#     print(f"Good Morning {name}")
#     print("Welcome to the jungle")
# user_name=input("enter your name")
# greet(user_name)


#exercise 1
# def life_in_weeks():
#     # Get the current age from the user
#     current_age = int(input("What is your current age? "))

#     # Calculate the remaining time
#     max_age = 90
#     years_left = max_age - current_age
#     weeks_left = years_left * 52  # 52 weeks in a year

#     # Print the result using f-strings
#     print(f"You have {weeks_left} weeks left.")
# life_in_weeks()

# exercise 2
# def greet_with(name,location): #multiple parameters and input
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
# greet_with("Naman","lucknow")
# greet_with("Sumit","Raibarilly")
# greet_with(name="Sahil",location="Ghazipur")

#exercise 3
# def calculate_love_score():
#     name1=input("Enter the name1: ")
#     name2=input("Enter the name2: ")
#     # Combine both names and convert them to lowercase
#     combined_names = (name1 + name2).lower()

#     # Count the occurrences of each letter in "TRUE"
#     true_score = 0
#     for letter in "true":
#         true_score += combined_names.count(letter)

#     # Count the occurrences of each letter in "LOVE"
#     love_score = 0
#     for letter in "love":
#         love_score += combined_names.count(letter)

#     # Combine the two scores to form the love score
#     love_score_total = int(str(true_score) + str(love_score))

#     # Print the result
#     print(f"Your love score is {love_score_total}.")
# calculate_love_score()