import random

def main():
    print("Welcome to Number Guessing Game!")

    while True:
        tries = choose_level()
        number = random.randint(1, 100)
        print("Please enter a number between 1 and 100.")
        success = play_game(tries, number)

        if not ask_play_again():
            break

def choose_level():
    difficulty = ["Easy", "Normal", "Hard"]

    print("Choose difficulty level:")
    for i in difficulty:
        print(f"{difficulty.index(i) + 1}. {i}")
    
    flag = True
    while flag:
        try:
            level = int(input("Enter the number of the choosen level: "))
            if level in [1, 2, 3]:
                flag = False
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")
    
    tries = 0

    if level == 1:
        print("You have 10 tries. \n")
        tries = 10
    elif level == 2:
        print("You have 7 tries. \n")
        tries = 7
    elif level == 3:
        print("You have 5 tries. \n")
        tries = 5
    return tries

def get_guess():
    print("Try to guess the number between 1 and 100!")
    guess = int(input("Enter your guess: "))
    
    return guess

def play_game(tries, number):
    attempts = 0
    while tries > 0:
        guess = get_guess()
        attempts += 1
        if guess < 1 or guess > 100:
            tries -= 1
            print(f"You have {tries} left.")
            continue
        
        if guess == number:
            print(f"Congratulations! You guessed the number {number} in {attempts} tries. \n")
            return True
        elif guess < number:
            print("Too low!")
            tries -= 1
            print(f"You have {tries} left.")
        elif guess > number:
            print("Too high!")
            tries -= 1
            print(f"You have {tries} left.")
    return False

def ask_play_again():
    repeat = input("Do you want to play again? (yes/no): ").strip().lower()
    if repeat == 'yes':
        return True
    else:
        print("Ty for playing!")
        return False

main()