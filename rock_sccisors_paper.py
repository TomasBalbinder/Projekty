
from random import randint


# This is a simple game Rock-scissors-paper

print("Welcome my game\n")

computer = ["rock", "paper", "scissors"]

score = 2

player_score = 0
computer_score = 0

while player_score <= score  and computer_score <= score:

    comp = computer[randint(0,2)]
    player = input("Player: ").lower()
    if player == "quit":
        break
    for word in computer:
        if player in computer:


            print(f"Computer: {comp}")

            if player == comp:
                print("Split!")
                player_score += 1
                computer_score += 1

            elif player == "rock":
                if comp == "scissors":
                    print("Player Win!")
                    player_score += 1
                else:
                    print("Computer Win!")
                    computer_score += 1

            elif player == "paper":
                if comp == "rock":
                    print("Player Win!")
                    player_score += 1
                else:
                    print("Computer Win!")
                    computer_score += 1

            elif player == "scissors":
                if comp == "paper":
                    print("Player Win!")
                    player_score += 1
                else:
                    print("Computer Win!")
                    computer_score += 1
            print(f"\nYour score is: {player_score} \nComputer score is: {computer_score}\n")
            print("-------------------------")
            break
    else:
        print("Wrong words, try again.")


if player_score > computer_score:
    print("End game, you Win!.")

elif player_score == computer_score:
    print("End game, Split!")
else:
    print("End game, computer Win!.")








