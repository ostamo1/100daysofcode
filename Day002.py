#!/bin/python
from os import system
system("cls")
####################################
print("Welcome to the Tip Calculator.")
billtotal=float(input("What was the total bill?"))
percentage=float(input("What percentage tip would you like to give? 10,12 or 15?"))
numpeople=int(input("How many people to split the bill?"))

totalbill=round((billtotal * (1+percentage/100))/numpeople,2)
totalbill= "{:.2f}".format(totalbill)
print(f"each person should pay ${totalbill}")

####################################
print("\n\n")