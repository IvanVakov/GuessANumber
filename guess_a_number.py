import random

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
        print("You guess it!")
        break
    elif player_number > computer_number:
        print("Too High!")
    else:
        print("Too Low!")
        
    if count > 5:
        if player_number != computer_number:
            print("Sorry you run out of tries. Try again in the next game.")
            break
        else:
             print("You guess it!")
             break
            
