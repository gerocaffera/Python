import random
guessed = False
number = random.randint(1,20)

print("I am thinking of a number between 1 and 20. Take a guess")

while not guessed:
    guess = input()
    guess = int(guess)

    if guess > number:
        print("Guess is too high")
    if guess < number:
        print("Guess is too low")
    if guess == number:
        print("You guessed right")
        guessed = True
