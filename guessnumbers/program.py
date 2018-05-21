import random


def main():
    start()
    game()


def start():
    answer = input("do you want to play a game?: ")
    if answer == "yes":
        print("good choice")
    elif answer == "no":
        print("too bad, here we go")
    else:
        print("ok whatever it's happening")


def game():
    number = random.randint(1, 10)
    guess = None
    while guess != number:
        user_input = input("\ni'm thinking of a number between 1 and 10\ntake a guess: ")
        guess = int(user_input)
        if guess > number:
            print("{} is too high".format(guess))
        elif guess < number:
            print("{} is too low".format(guess))
    else:
        print("wow, {} is right! you won, idiot.".format(guess))


main()
