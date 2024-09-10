from random import randint
from art import logo
def clear():
    print("\033[H\033[J")

def menu():
    choice = int(input("Enter\n1 -> continue playing\n0 -> exit :\t"))
    match choice:
        case 0:
            clear()
            print("Thank you for playing 😉")
            exit()
        case 1:
            clear()
            print("CooL! Let's play again...! 😁")
            intro()


def easy():
    print("You get 10 attempts to guess the number")
    target = randint(1, 100)
    attempts = 10
    while attempts != 0:
        answer = int(input("Guess the number :\t"))
        attempts -= 1
        if answer == target:
            print(f"Woah!! You guessed it right!!\nThe number is  {target}")
            menu()
            break
        elif answer > target:
            print(f"Too high..! {attempts - 1} attempts remaining! ")
        else:
            print(f"Too low..! {attempts -1} attempts remaining! ")
        attempts -= 1
    if attempts == 0:
        print("Looks like you are out of attempts!!\nBetter luck next time!")
        print(f"The number was {target}")
        menu()

def hard():
    print("You get 5 attempts to guess the number")
    target = randint(1, 100)
    attempts = 5
    while attempts != 0:
        answer = int(input("Guess the number :"))

        if answer == target:
            print(f"Woah!! You guessed it right!!\nThe number is  {target}")
            menu()
            break
        elif answer > target:
            print(f"Too high..! {attempts - 1} attempts remaining! ")
        else:
            print(f"Too low..! {attempts - 1} attempts remaining! ")
        attempts -= 1
    if attempts == 0:
        print("Looks like you are out of attempts!!\nBetter luck next time!")
        print(f"The number was {target}")
        menu()

def start():
    user_choice = input("Choose your difficulty (easy/hard) :")
    if user_choice.lower() == "easy":
        easy()
    else:
        hard()


def intro() -> None:
    print(logo)
    print("Welcome to the number guessing game!! 😁")

    print("I'm thinking of a number between 1 to 100...")
    start()

intro()