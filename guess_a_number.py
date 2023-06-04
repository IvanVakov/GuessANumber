import random


def play_game():
    computer_number = random.randint(1, 10)
    count = 0
    tries_count = 5

    while True:
        player_input = input("Guess the number (1-10): ")
        print(f"You will have {tries_count} tries to guess it")

        count += 1
        tries_count -= 1

        if not player_input.isdigit():
            print("Invalid input. Try again...")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            print("You guessed it!")
            break
        elif player_number > computer_number:
            print("Too High!")
        else:
            print("Too Low!")

        if count > 5:
            print("Sorry, you ran out of tries.")
            break


def play_again():
    while True:
        restart = input("Do you want to play again? (yes/no): ")
        if restart.lower() == "yes":
            play_game()
        elif restart.lower() == "no":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def start():
    print("Welcome to the Number Guessing Game!")
    play_game()
    play_again()


start()
