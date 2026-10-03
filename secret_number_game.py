import random

play_again = "yes"

while play_again.lower() == "yes":

    secret_number = random.randint(1, 10)
    winner = False

    while winner == False:

        number = int(input("Say a number between 1 and 10 "))

        if number == secret_number:
            print(f"The secret number is {secret_number}, you win!")
            winner = True

        elif number > secret_number:
            print("Too high! Try a smaller number.")

        else:
            print("Too low! Try a bigger number.")

    play_again = input("Do you want to play again? Yes/No: ")