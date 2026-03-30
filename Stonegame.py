import random
print("Welcome to HAND GAME")
choices= ["rock","paper","scissor"]
user= input("enter rock, paper or scissors: ").lower()
computer =  random.choice(choices)
print("computer:",computer)

#tie case
if user == computer:
    print("it's a tie")

#if your winning cases
elif user == "rock" and computer == "scissors":
    print("you win")

elif user == "paper" and computer == "rock":
    print("you win")

elif user == "scissors" and computer == "paper":
    print("you win")

#computer winning cases
elif computer == "rock" and user == "scissors":
    print("computer wins")
elif computer == "paper" and user == "rock":
    print("computer wins")   
elif computer == "scissors" and user == "paper":
    print("computer wins")   

#invalid input
else:
    print("invalid input")