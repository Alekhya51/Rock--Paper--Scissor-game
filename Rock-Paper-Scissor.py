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
    elif (player=="rock" and computer=="paper")or\
    (player=="paper" and computer=="scissor")or\
    (player=="scissor" and computer=="rock"):
        print("you won the game")
    else:
        print("computer won the game")