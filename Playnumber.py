import random

print("Welcome to Number Guessing Game!")

name = input("Enter your name: ")

while True:

    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 5
    won = False

    print("\nHello", name)
    print("I have selected a number between 1 and 100.")
    print("You have 5 chances to guess the number.")

    while attempts < max_attempts:

        print("\n-------------------------")

        print("Attempt:", attempts + 1, "of", max_attempts)
        print("Remaining chances:", max_attempts - attempts)

        try:
            guess = int(input("Enter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess == secret_number:

            won = True

            print("\nCongratulations! You won!")
            print("The secret number was:", secret_number)

            if attempts == 1:
                print("Rank: Excellent!")

            elif attempts == 2:
                print("Rank: Very Good!")

            elif attempts == 3:
                print("Rank: Good!")

            elif attempts == 4:
                print("Rank: Accepted!")

            elif attempts == 5:
                print("Rank: Lucky!")

            break

        else:

            difference = abs(guess - secret_number)

            if guess > secret_number:
                print("Smaller! Enter a smaller number.")

            else:
                print("Bigger! Enter a bigger number.")

            if difference <= 5:
                print("Very close!")

            elif difference <= 15:
                print("You are close, but still have some distance!")

            else:
                print("You are far away!")

    if not won:

        print("\nGame Over! You lost.")
        print("The correct number was:", secret_number)

    print("\nDo you want to play again?")

    while True:

        answer = input("Enter yes or no: ").lower()

        if answer == "yes":
            break

        elif answer == "no":
            print("Thank you for playing!")
            exit()

        else:
            print("Please enter yes or no.")