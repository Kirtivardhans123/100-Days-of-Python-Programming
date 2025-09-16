# Write a program that verifies whether a line segment is a Horizontal, Vartical, and oblique

x1=int(input("Enter the value of X1: "))
y1=int(input("Enter the value of Y1: "))
x2=int(input("Enter the value of X2: "))
y2=int(input("Enter the value of Y2: "))
if x1==x2:
    print("Vertical")
elif y1==y2:
    print("Horizontal")
else :
    print("Oblique")
