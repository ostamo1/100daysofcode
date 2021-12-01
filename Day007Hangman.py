#!/bin/python
from os import system
system("cls")
from modules.hangmanwords import word_list
from modules.hangmanart import *
####################################

print(logo)
lives=6
import random
chosenword = random.choice(word_list)
chosenword =list(chosenword)
display = list(chosenword)
guessedletters=[]
for x in range(len(chosenword)):
  display[x]='_'
print(f"{' '.join(display)}")
end_of_game = False
while not end_of_game:
    guess=input("Guess a letter : ").lower()
    if guess in guessedletters:
            lives-=1
            print(f"you have already guess letter {guess}")
    elif guess in display:
        print(f"you have already guess letter {guess}")
    elif guess not in chosenword:
            lives-=1
            guessedletters.append(guess)
    else:
        for x in range(len(chosenword)):
            if guess == chosenword[x]:
                display[x]=guess    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    if lives == 0:
        end_of_game =True
        print("you lose")
    print(stages[lives])