import random
options=["rock","paper","scissor"]
while True:
    player=input("enter rock,paper,scissor(or'exit',to quit): " ).lower()
    if player=="exit":
        print("thank you for playing")
        break
    if player not in options:
        print("entered invalued choice!try again")
        break
    computer=random.choice(options)
    print("enter choice:",computer)

    if computer==player:
        print("tie!")
    elif (player=="paper" and computer=="rock")or\
    (player=="scissor" and computer=="paper")or\
    (player=="rock" and computer=="scissor"):
        print("you won the game")
    else:
        print("computer won the game")
