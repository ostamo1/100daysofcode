#this is a file that has random projects 
#that are commented out
#!/bin/python
from os import system
system("cls")
####################################

#!/bin/python3
#11-23-2021 Learning about Variable types in python being mutable or immutable
#also learning about precicion and fractions and Booleans and floats and ints

#tuples
# t=()
# type(t)
# one_element_tuple = (42,)
# three_element_tuple = (1,2,3)
# a,b,c = 4,5,6
# print(a)
# print(b)
# print(c)
# print(one_element_tuple)
# print(three_element_tuple)
# print(3 in three_element_tuple)

# num=int(input("how many numbers "))
# x=0
# for x in range(1,num+1):
#     print(x)
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")

# height=float(input("height"))
# weight=float (input("weight"))
# bmi = weight/(height**2)
# print(int(bmi))
# height=int(input("input height\n"))
##########
# age=int(input("input age\n"))
# other = 90 - age
# days = other *365
# weeks = other *52
# months = other * 12
# print(f"you have {days} days , {weeks} weeks , and {months} months left.")
##########
# ticket=0
# if(height >= 120):
#     if(age >=12 and age <=18):
#         ticket=7
#     elif(age < 12):
#         ticket = 5
#     else:
#         ticket =12
# else:
#     print("you cannot ride")
# print(ticket)
##########
# textprint=''
# bmi=36
# if(bmi <=18.5):
#     textprint = "underweight"
# elif(bmi > 18.5 and bmi<= 25):
#     textprint = "normal weight"
# elif(bmi > 25 and bmi<= 30):
#     textprint = "overweight"
# elif(bmi > 30 and bmi<= 35):
#     textprint = "obese"
# else:
#     textprint = "clinically obese"

# print(textprint)
##########
# #year=int(input("Enter Year:"))
# for x in range(1995,2025):
#     print(x)
#     if((x%4 )==0): #good
#         if ((x % 100)==0):
#             if ((x % 400)==0):
#                 print("leap year")
#             else:
#                 print("not leap year")
#         else:
#             print("leap year")
#     else:
#         print("not leap year")
# #x+=10
##########
# name1="Angela yu"
# name2 ="Jack bauer"
# names=name1+name2
# score1 = 0
# score1+=names.lower().count("t")
# score1+=names.lower().count("r")
# score1+=names.lower().count("u")
# score1+=names.lower().count("e")

# score2=0
# score2+=names.lower().count("l")
# score2+=names.lower().count("o")
# score2+=names.lower().count("v")
# score2+=names.lower().count("e")

# score =int(str(score1)+str(score2))
# print(score)
# if score < 10 and score > 90:
#     print(f"you score is {score} coke and Mentos")
# elif score >=40 and score <= 50 :
#     print(f"you score is {score} you are okay together")
# else:
#     print(f"you score is {score} ")
##########
# print("flip a coin")
# for x in range(1,4):
#     y=random.randint(1,2)
#     if y % 2 == 0:
#         print(f"heads {y}")
#     else:
#         print(f"tails {y}")
##########
# import random
# names=["cris","pam","emma"]
# #names=input("insert names here ").split(", ")
# for x in range(1,11):
#     whopays=random.randint(0,len(names)-1)
#     print(names[whopays])
##########
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position= input("where to put treasure?\n")
# column=int(position[0])
# row=int(position[1])
# map[row-1][column-1]="💲"
# print(f"{row1}\n{row2}\n{row3}")
##########
# mylist="180, 124, 165, 173, 189, 169, 146"
# heights=mylist.split(", ")
# avgheight=0
# for x in heights:
#     avgheight+=int(x)

# print(round(avgheight/len(heights)))
##########
# mylist="100, 65, 89, 86, 55, 91, 64, 89, 99"
# heights=mylist.split(", ")
# score=0
# for x in heights:
#     if score <=int(x):
#         score=int(x)
    

# print(score)
##########
# import random
# s = 'abcde'
# sr = ''.join(random.sample(s, len(s)))
# print(sr)
##########
# chosenword="aardvark"
# triesleft=len(chosenword)
# shownword = list(chosenword)
# for x in range(0, triesleft):
#   shownword[x]='_'

# print(''.join(shownword))
##########
# import math
# height= int(input("height"))
# width= int(input("width"))
# coverage=5

# def calc(h,w,c):
#   area=math.ceil((h*w)/c)
#   print(f" {area} cans")

# calc(height,width,coverage)

##########
# def prime_checker(number):
#   isprime=True
#   #listofnums=[]
#   for x in range(2,number):
#     if (number % x == 0):
#       isprime = False

#   if isprime == True:
#     print(f"{number} is a prime number")


# #n = int(input("Check this number: "))
# for x in range(2,121):
#   prime_checker(number=x)

##########
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#     shift_amount *= -1
#   for char in start_text:
#     #TODO-3: What happens if the user enters a number/symbol/space?
#     #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#     #e.g. start_text = "meet me at 3"
#     #end_text = "•••• •• •• 3"
#     if char in alphabet:
#       position = alphabet.index(char)
#       new_position = position + shift_amount
#       end_text += alphabet[new_position]
#     else:
#       end_text += char
#   print(f"Here's the {cipher_direction}d result: {end_text}")

# #TODO-1: Import and print the logo from art.py when the program starts.
# from art import logo
# print(logo)

# #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_end = False
# while not should_end:

#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#   #Try running the program and entering a shift number of 45.
#   #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#   #Hint: Think about how you can use the modulus (%).
#   shift = shift % 26

#   caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#   restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#   if restart == "no":
#     should_end = True
#     print("Goodbye")
    

##########
##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

##########

####################################
print("\n\n")