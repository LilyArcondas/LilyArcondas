print("\rExcercise 8:")
import random
n= random.randint(1,99)
guess=int(input("Choose a random number, 1 through 99: "))
while n != guess:
    if guess > n:
        guess = int(input("Your guess is too high. Try again: "))
    elif guess < n:
        guess = int(input("Your guess is too low. Try again: "))
    else:
        print("You guessed it!")
print("You guessed it!")