#!/bin/python
from os import system
system("cls")
####################################

import random

print("Lets play rock paper scissors:")
choice=int(input("Rock =0,Paper =1 , or Scissors =2?"))

#choice = 0
choices=["rock","paper","scissors"]
if choice >= 3 or choice < 0:
    print("not a choice")
else:
    print(f"you chose {choices[choice]}")

    pcchoice= random.randint(0,2)
    print(f"the computer chose {choices[pcchoice]}")
    if pcchoice == choice :
        print ("draw")
    elif pcchoice == 0 and choice== 2:
        print("you lose")
    elif pcchoice == 2 and choice== 1:
        print("you lose")
    elif pcchoice == 1 and choice== 0:
        print("you lose")
    else:
        print("you win")

####################################
#print("\n\n")