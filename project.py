#In this project you have to enter a range [A, B] and system will randomly pick any number from
#your given range and check the status of that given number.
#The properties to be checked are:
#1. Is that number is odd or even
#2. Is that number is positive or negative number
#3. Is that number is prime number or composite number.
#After checking the status, you have to display all the properties followed by the randomly picked
#number.
#For example
#Range is (1,12) and randomly picked number is 10
#Then the properties followed by this number are:
#10 is a positive number
#10 is an even number
#10 is a composite number

import random
a = int(input("The lower range: "))
b = int(input("The upper range: "))
r = random.randint(a,b)
print("The generated random number is",r)
if r%2==0:
    print(f"The number {r} is even")
else :
    print(f"The number {r} is odd")
if r>0 :
    print(f"The number {r} is positive")
else :
    print(f"The number {r} is negative")
for i in range(2,r):
    s = False
    if r%i==0:
        s = True
if s==True:
    print(f"The number {r} is composite")
else:
    print(f"The number {r} is prime")
    
