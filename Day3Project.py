print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
road=str(input("You're at a cross road. Where do you want to go? \n Type 'left' or 'right': "))
if road=="right":
    print("Game over,You choose the road of lions.")
elif road=="left":
    print("You've come to the Lake.There is an island in the middle of the lake.")
    s_or_w=str(input("type 'wait' to wait for a boat.Type 'swim' to swim across. :"))
    if s_or_w=="swim":
        print("Game over,you are killed by the crocodiles.")  
    elif s_or_w=="wait":
        print("")  
        door=str(input("Which door do you want to choose? Red, Blue and Yellow"))
        if door=="red":
            print("Game Over.You Lost the match")
        elif door=="blue":
            print("Game Over.You Lost the match")
        else:
            print("Congratulation,You Win!")
else:
    print("You choose the invalid path.")