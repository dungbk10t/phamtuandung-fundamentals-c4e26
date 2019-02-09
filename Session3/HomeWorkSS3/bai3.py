#The Word Jumble Game

import random

WORDS = ["python","jumble","game","word",

]
word = random.choice(WORDS)

correct = word
jumble = ""
while(word):
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

#Start game
print(
    """
            WECOME TO WORD JUMBLE
            =====================
    Unscramble the letters to make a word\n
    """         
    )
print("The jumble is: ",jumble)

guess = input("\nYour quess: ")
while(guess!=correct and guess!=""):
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if(guess == correct):
    print("That's it! You guessed it!\n")

print("Thanks for playing")
input("\n\nPress the enter key to exit")
