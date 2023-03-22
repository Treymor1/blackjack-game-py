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

def computer_guess(x):
    myguess = int(input("Insert your number and computer try to guess"))
    comp_guess = 0
    while myguess != comp_guess:
        comp_guess = random.randint(1,x)
        if myguess>comp_guess:
            print("To High")
        elif myguess<comp_guess:
            print("Too Low")
    print("You Win!")

computer_guess(20)



