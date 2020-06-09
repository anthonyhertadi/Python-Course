import random
comp = random.randint(1,4)

for x in range(1,4):
    if comp == 1:
        bot = 'ROCK'
    elif comp == 2:
        bot = 'PAPER'
    else:
        bot = 'SCISSORS'

    orang = input("ROCK/PAPER/SCISSORS?")
    orang.lower()
    if comp == 1:
        if orang=="rock":
            print("DRAW!!!")
        elif orang==("paper"):
            print("YOU WIN!!!")
        else:
            print("YOU LOSE!!!")
            break
    if comp == 2:
        if orang=="rock":
            print("YOU LOSE!!!")
            break
        elif orang=="paper":
            print("DRAW!!!")
        else:
            print("YOU WIN!!!")
    if comp == 3:
        if orang == ("rock"):
            print("YOU WIN!!!")
        elif orang ==("paper"):
            print("YOU LOSE!!!")
            break
        else:
            print("DRAW!!!")