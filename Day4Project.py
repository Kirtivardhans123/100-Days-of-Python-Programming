import random
rock='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]

user_input=int(input("What do you choose?type 0 for Rock,1 for Paper or 2 for Scissors: "))
#user choice
if user_input>=0 and user_input<=2:
    print(game_images[user_input])
#compter choice
computer_choice=random.randint(a=0, b=2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if user_input>=3 or user_input<0:
    print("You type the invalid the number!")
elif user_input==0 and computer_choice==2:
    print("You Win!")
elif computer_choice > user_input:
    print("Computer Win!")
elif computer_choice==user_input:
    print("It's a draw")
elif computer_choice==0 and user_input==2:
    print("You Win!")
elif user_input > computer_choice:
    print("You Win!")
else:
    print("You typed an invalid number.You lose!")