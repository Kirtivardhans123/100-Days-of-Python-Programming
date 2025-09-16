# Write a program to sort a list in python...

numbers=list(map(int,input("Enter any number: \n").split()))

#Ascending Order
sorting_list_ascending=sorted(numbers)
print("The Ascending Order list is: ", sorting_list_ascending)

#Descending Order
sorting_list_descending=sorted(numbers,reverse=True)
print("The Descending Order list is: ", sorting_list_descending)