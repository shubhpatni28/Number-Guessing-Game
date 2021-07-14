  
import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number between 1 and 9")
while chances <5:
    guess=int(input("Enter Your Guess"))
    if guess==number:
        print("Merlin's Beard !!You Defeated Me")
        break
    elif guess<number:
        print("Your Guess Was Too Low,Guess A Number Higher Than",guess)
    else:
        print("Your Guess Was Too High,Guess A Number Lower Than",guess)
    chances+=1

if not chances<5:
    print("lol...You Lose!! The Number Is ",number)