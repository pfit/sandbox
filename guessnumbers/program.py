import random


def start():
    answer = input("do you want to play a game?: ")
    if answer == "yes":
        print("good choice")
    elif answer == "no":
        print("too bad, here we go")
    else:
        print("ok well here we go anyway")


def game():
    number = random.randint(1, 100)
    guess = 101
    while guess != number:
        game = input("\ni'm thinking of a number between 1 and 100\nplease take a guess: ")
        guess = int(game)
        if guess > number:
            print("{} is too high".format(guess))
        if guess < number:
            print("{} is too low".format(guess))
    else:
        print("wow, {} is right! you won, idiot.".format(guess))


def main():
    start()
    game()

main()
