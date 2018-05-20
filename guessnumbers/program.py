import random

number = random.randint(1, 100)

gamestart = input("do you want to play a game?: ")

if gamestart == "yes":
    print("good choice")
elif gamestart == "no":
    print("too bad, here we go")
else:
    print("ok well here we go anyway")

guess = 101

while guess != number:
        game = input("\ni'm thinking of a number between 1 and 100\nplease take a guess: ")
        guess = int(game)
        if guess > number:
            print("{} is too high".format(guess))
        if guess < number:
            print("{} is too low".format(guess))
else:
    print("wow, {} is right! you won, idiot.")

