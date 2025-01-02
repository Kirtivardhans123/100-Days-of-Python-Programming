import random

print("Welcome to Hangman Game")

list_of_words=["cat","apple","dog","grandfather",""]
# Randomly choose a word from the list_of_words and assign it in the variable called choosen_word
lives=6

chosen_word=random.choice(list_of_words)

# Create a placeholder with the same no. of blanks as the chosen_word
placeholder= ""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over= False
correct_letter=[]

while not game_over:
    # Check the user guess a letter and assign their answer to a variable.
    guess=input("Guess the letter: ").lower()
    # Check if the letter the user guessed is one of the letters in the chosen_word
    display=""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You Win!")
    
    print(f"Lives available: {lives}")