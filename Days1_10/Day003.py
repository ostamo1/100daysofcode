#!/bin/python
from os import system
system("cls")
####################################
#basic setup fo the final project, it works logically just not as pretty
print("welcome to treasure island")
status=input("left or right").lower()
if(status == 'left'):
    status=input("swim or wait").lower()
    if(status == 'wait'):
        status=input("which door?, red,yellow or blue").lower()
        if(status == 'red'):
            print("burned by fire/n game over")
        elif(status == 'blue'):
            print("eaten by beasts/n game over")
        elif (status == 'yellow'):
            print("you win")
        else:
            print("/n game over")
    else:
        print("attacked by a trout/n game over")
else:
    print("you fall into a hole/n game over")
####################################
print("\n\n")