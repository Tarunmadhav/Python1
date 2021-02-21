import random

number=random.randint(1,9)
chances=0
print("Guess A Number Between 1-9")
while chances<5:
    guess=int(input("Guess A Number 1-9"))
    if(guess==number):
        print("Congratulations")
        break
    elif(guess<number):
        print("Guess Higher Number")
    else:
        print("Guess Lesser Number")
    chances+=1
if(chances>5):
    print("You Loose and The Number is",number)