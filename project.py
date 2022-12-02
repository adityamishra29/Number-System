

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
    
