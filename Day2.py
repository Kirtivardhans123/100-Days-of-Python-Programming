# print("hello"[0])

# # String
# print("123" + "456")

# integer
# n1= 345
# n2= 234
# print(n1 + n2)

# # float
# f1= 23.65
# f2= 456.7
# print(f1 + f2)

# # boolean 
# b1= True


# # Checking Datatype
# print(type(n1)) 
# print(type(f1))
# print(type(b1)) 

# # Type Conversion
# print(int("123") + int("456"))
# print(float("123") + float("456"))
# print(bool("123") + bool("456"))

# # Exercise 1

# # print("Number of letters in your name :" + len(input("enter your name"))) #Wrong format...

# name_of_user = input("Enter the name :")
# length_of_name = len(name_of_user)

# # convert into the string datatype then perform the operation
# print("Number of letters in your name :" + str(length_of_name))

# # Other mathematical Operation 

# print(n1 + n2) #Additon
# print(n1 - n2) #Substraction
# print(n1 * n2) #Multiply
# print(n1 / n2) #Division
# print(n1 // n2) #It is also a Division but used when we don't want the decimal places... 
# print(2 ** 2)
# print(2 ** 3)

# # Its always uses the PEMDAS to perform the mathematical operation
# print(3 * 3 + 3 / 3 - 3) #Output 7
# print(3 * ( 3 + 3 ) / 3 - 3) #Output 3


# Exercise 2
height = 1.65 
weight = 84
# bmi = weight / (height*height)
bmi = weight / (height**2)
print(bmi)

# print(round(bmi)) #Round of any output
# print(round(bmi,4)) #Round of any output by the desired digit of round off.

# n1+=n2
# print(n1)

# Exercise 3 If we want to insert multiple variable in a Single String, we use F-strings

print(f"If the Weight is a person is : {weight}, the height is : {height}, then BMI of the person is : {bmi}")