import random


print("This random number guesser has three dificulties: Easy, Medium, and Hard.")
difficulty = input("Type your desired difficulty: ")
difficulty = (difficulty.lower()).strip()

if difficulty == "easy":
    triesAvailable = 5
    number = random.randint(1, 10)
    guess = 0
    while triesAvailable > 0:
        triesAvailable -= 1
        guess = int(input("Guess a number between 1 and 10: "))
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

elif difficulty == "medium":
    triesAvailable = 5
    number = random.randint(1, 20)
    guess = 0
    while triesAvailable > 0:
        triesAvailable -= 1
        guess = int(input("Guess a number between 1 and 20: "))
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
elif difficulty == "hard":
    triesAvailable = 5
    number = random.randint(1, 30)
    guess = 0
    while triesAvailable > 0:
        triesAvailable -= 1
        guess = int(input("Guess a number between 1 and 30: "))
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
