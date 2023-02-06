# import random

# # options
# options = ["rock", "paper", "scissors"]

# # user input
# user_choice = input("Please choose rock, paper, or scissors: ").lower()


# if user_choice not in options:
#     print("Invalid input. Please choose rock, paper, or scissors.")
#     exit()


# computer_choice = random.choice(options)


# if user_choice == computer_choice:
#     print("It's a tie!")
# elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
#     print("You win! The computer loose " + computer_choice + ".")
# else:
#     print("You lose! The computer won " + computer_choice + ".")
import random
option=["scissor","stone","paper"]
user=input("Enter your choice: ").lower()
computer=random.choice(option)
if user not in option:
    print("Invalid input")
if user==computer:
    print("Tie")
elif (user=="paper" and computer=="stone") or (user=="scissor" and computer=="paper") or (user=="stone" and computer=="scissor"):
    print("You won and computer choose "+computer)
else:
    print("You loose and computer chosses "+computer)