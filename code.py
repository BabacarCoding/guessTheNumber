import random


print("This random number guesser has three dificulties: Easy, Medium, and Hard.")
difficulty = input("Type your desired difficulty: ")
difficulty = (difficulty.lower()).strip()


def guessFunction(upperBound):
    triesAvailable = 5
    number = random.randint(1, upperBound)
    guess = 0
    while triesAvailable > 0:
        triesAvailable -= 1
        guess = int(input(f"Guess a number between 1 and {upperBound}: "))
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        elif guess == number:
            print(f"You guessed the number in {5 - triesAvailable} tries!")
            triesAvailable = -1
    if triesAvailable == 0:
        print(
            f"You have ran out of guesses. The number was {number}. Better luck next time!")


if difficulty == "easy":

    guessFunction(10)

elif difficulty == "medium":

    guessFunction(20)

elif difficulty == "hard":

    guessFunction(30)
