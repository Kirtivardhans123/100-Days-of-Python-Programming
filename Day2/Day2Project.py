# tip Calculator
print("Welcome to the tip Calculator!") # Greeting Message
total_bill=float(input("What is your total bill? $")) #total bill
tip_percentage=int(input("How much tip would you like to give? 10 12 or 15? ")) #tip amount in percent but not use percentage sign while enter the input 
no_of_person=int(input("How many people to split the bill? ")) #no. of person 
payable_amt_per_person=((total_bill*(tip_percentage/100)+total_bill)/no_of_person) 
print(f"Each person should pay: ${payable_amt_per_person}")