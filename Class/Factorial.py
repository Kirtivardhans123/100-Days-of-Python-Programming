# Write a program for two factorial definition...

n=int(input("Enter the number: "))

# Method 01
result=1
for i in range(1,n+1):
    result*=i
print(" By Method 01: ", result)

# Method 02
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(" By Method 02: ", fact(n))

# Method 03
import math
print(" By Method 03: ", math.factorial(n))
