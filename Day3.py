# print("Welcome to Day3: Conditional Statement")

# #Let a COnditional Statement of a Rollercoaster Ride , where we use if-else Condition

height=int(input("What is your height"))
if height >= 120:
# if height <= 120:
# if height == 120:
# if height != 120:
# if height < 120:
# if height > 120:
    print("You can ride the Rollercoaster")
else:
    print("Sorry you can't ride the Rollercoaster ")

# Exersice 1 To find a no. is even or odd

num=int(input("Enter the number you want to check that is it even or odd"))
if num % 2==0:
    print("This is a Even number")
else :
    print("This is a Odd number")

#Exersie 2 BMI Calculator with Interpretations, Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.If the bmi is under 18.5 (not including), print out "underweight". If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight". If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal Weight")
else:
    print("Overweight")   

#Exercise 3 

print("Welcome to Domino's Pizza")
size=str(input("What size do you want? S , M, L: "))
pepperoni=str(input("Do you want pepperoni on your pizza? Y or N: "))
extra_cheese=str(input("Do you want extra cheese? Y or N: "))
bill=0

if size=="S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
else:
    print("You enter the wrong size")

if pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3

if extra_cheese=="Y":
        bill+=1

print(f"The Final bill is ${bill}")