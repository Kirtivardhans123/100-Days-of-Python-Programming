print("Hello World") 
# Hello World is written in the string datatype ("")

# Exercise 1 
# Method1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Method2
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl. \n2. Knead the dough for 10 minutes. \n3. Add 3g of Salt. \n4. Leave to rise for 2 hours.\n5. Bake at 200 degrees C for 30 minutes.")

# Exercise 2
input("What is your name?")
print("Hello " + input("What is your name?"))

# Variables
name = input("What is your name?")
name= "Naman"
print(len(name)) #length of the name


#Question- We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"
glass2 = "juice"
glass3=glass1
print("The Glass 3 contain " + glass3)
glass1=glass2
print("The Glass 1 contain " + glass1)
glass2=glass3
print("The Glass 2 contain " + glass2)