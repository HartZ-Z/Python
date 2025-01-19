import random

def game():
    print("You are playing a game..")
    score=random.randint(1,100)

    with open ("Highscore.txt") as f:
        highscore=f.read()

        if (highscore!=""):
            highscore = int (highscore)
        else:
            highscore = 0

    print(f"Your score = {score}")

    if ( score > highscore ):
        with open ("Highscore.txt" , "w") as f:
            f.write(str(score))

    if (score > highscore):
        print(f"You just beat the highscore which was {highscore}")
        print(f"New highscore: {score}")
    elif ( score == 100 ):
        print("Well done you just beat the game with your score ")
    else:
        print(f"Better luck next time\nHighscore:{highscore}")
    return score
game()