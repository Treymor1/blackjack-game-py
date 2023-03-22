import random
def user():
    user_choices=input("Rock,Paper or Scisors: ").lower()
    return user_choices

def computer():
    computer_choices=random.choice(["rock","paper","scissors"])
    return computer_choices

def game():
    print("Welcome to the game ROCK, PAPER OR SCISSORS!")
    user_choice = user()
    computer_choice = computer()
    print(computer_choice)
    if user_choice == "rock" and computer_choice == "scissors":
        print("You win!, rock beats scissors ")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! paper beats rock")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! scissors beats paper")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("You Lose! rock beats scissors")
    elif computer_choice == "paper" and user_choice == "rock":
        print("You Lose! paper beats rock")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("You Lose! scissors beats paper")
    else:
        print("Tie!")

game()
