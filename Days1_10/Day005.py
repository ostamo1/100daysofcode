#!/bin/python
from os import name, system
system("cls")
####################################
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# numletters = int(input("how many letters"))
# numnumbers = int(input("how many numbers"))
# numsymbols = int(input("how many symbols"))
numletters = 6
numnumbers = 2
numsymbols = 2
password=""
passwordlength = numletters+numnumbers+numsymbols
for x in range(0,numletters):
  rnum=random.randint(0,len(letters)-1)
  password+=letters[rnum]
for x in range(0,numnumbers):
  rnum=random.randint(0,len(numbers)-1)
  password+=numbers[rnum]    
for x in range(0,numsymbols):
  rnum=random.randint(0,len(symbols)-1)
  password+=symbols[rnum]

print(password)
password =''.join(random.sample(password,len(password)))
# newpass=""
# for x in range(0,len(password)):
#   rnum=random.randint(0,len(password)-1)
#   newpass+=password[rnum]
#   password=password.replace(password[rnum],"",1)

# password=newpass
print(password)
####################################
