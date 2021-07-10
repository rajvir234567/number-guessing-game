#number guessing game
import random

print("number guessing game from 1 to 9")

number = random.randint(1,9)

chances = 0
print("guess a number between one and nine")

while(chances<5):
    guess = int(input("enter your guess "))
    if(guess == number):
        print("you won")
        break
    elif(guess < number):
        print("guess was too low, guess a bigger number than",guess)
    else:
        print("guess was too high, guess a smaller number than",guess)
    
    chances +=1

if not chances<5: 
    print("you lose the number was",number)