import random

random_integer= random.randint(1,50)
print(random_integer)

random_number_0to1=random.random()*10
print(random_number_0to1)

random_float=random.uniform(a=1,b=10)
print(random_float)

# Exercise1 
friends=["Naman","Sumit","Saurabh","Sahil","Arish"]
random_friends=random.choice(friends)
print(random_friends)