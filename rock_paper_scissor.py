#[Rock Paper Scissor game -by Aakash mohole] rock broke scissor, paper wrap rock, scissor cut paper
import random

lst = ['rock','paper','scissor']

chance = 5
no_of_chance = 0
computer_point = 0
human_point = 0
print("------------------------------------\n")
print("_ Rock, Paper, Scissor Game _ Aakash Mohole _ \n")
print("------------------------------------\n")

while no_of_chance < chance:
    _input = input('Enter your choice (Rock, Paper, Scissor): ').lower()
    _random = random.choice(lst)

    if _input == _random:
        print("\n------------------------------------")
        print("\nTie...! 0 points to each player")
        print("------------------------------------")


    elif _input == "rock" and _random == "paper":
        computer_point = computer_point + 1
        print("\n------------------------------------")
        print(f"You chose {_input} and computer chose {_random}")
        print("Computer wins by 1 point")
        print(f"Computer's point is {computer_point} and your point is {human_point} ")
        print("------------------------------------")

    elif _input == "paper" and _random == "rock":
        human_point = human_point + 1
        print("\n------------------------------------")
        print(f"You chose {_input} and computer chose {_random} ")
        print("You wins by 1 point ")
        print(f"Computer's point is {computer_point} and your point is {human_point}")
        print("------------------------------------")

    elif _input == "scissor" and _random == "rock":
        computer_point = computer_point + 1
        print("\n------------------------------------")
        print(f"You chose {_input} and computer chose {_random} ")
        print("Computer wins by 1 point ")
        print(f"Computer's point is {computer_point} and your point is {human_point}  ")
        print("------------------------------------")

    elif _input == "rock" and _random == "scissor":
        human_point = human_point + 1
        print("\n------------------------------------")
        print(f"You chose {_input} and computer chose {_random}")
        print("You wins by 1 point")
        print(f"Computer's point is {computer_point} and your point is {human_point}")
        print("------------------------------------")

    elif _input == "scissor" and _random == "paper":
        human_point = human_point + 1
        print("\n------------------------------------")
        print(f"\nYou chose {_input} and computer chose {_random}")
        print("You wins by 1 point ")
        print(f"Computer's point is {computer_point} and your point is {human_point}")
        print("------------------------------------")


    elif _input == "paper" and _random == "scissor":
        computer_point = computer_point + 1
        print("\n------------------------------------")
        print(f"You chose {_input} and computer chose {_random} ")
        print("Computer wins by 1 point ")
        print(f"Computer's point is {computer_point} and your point is {human_point} ")
        print("------------------------------------")

    else:
        print("you have input wrong !\n")

    no_of_chance = no_of_chance + 1
    print(f"[ {chance - no_of_chance} is left out of {chance} chance.!] \n")

print("*********************************************")
print("Game over...!")

if computer_point==human_point:
    print("Tie...!")

elif computer_point > human_point:
    print("Computer wins and you loose :()")

else:
    print("Congo..! You win and computer loose :)")

print(f"Your point is {human_point} and computer point is {computer_point}")
print("*********************************************")


