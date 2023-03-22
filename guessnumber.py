import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input("Guess the number"))
        if guess<random_number:
            print("Too low")
        elif guess>random_number:
            print("Too high")
    print("You Win!")

guess(20)

