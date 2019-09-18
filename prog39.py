print("Hello , What is Your name : \n")
name  =  input()
import random
num = random.randrange(1,21,1)
print("Well "+name+" I am thinking of a number between 1 and 20 \n Take a guess")

c_guess = 1
guessed = int(input())
while( guessed  != num   ):
    if(guessed < num ):
	print("Your guess is too low")
    else:
	print("Your guess is too high")
    print("Take a Guess ")
    guessed = int(input())
    c_guess+=1

print("Good Job, "+name+"! You guessed my number in "+str(c_guess)+" guesses!")

	
