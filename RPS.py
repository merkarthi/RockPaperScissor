import random as ran
score=0
life=3


class Myasset:
    score=0


def intro():
    import time
    print("Welcome to")

    time.sleep(0.2)
    print("Rock")

    time.sleep(0.2)
    print("paper")

    time.sleep(0.2)
    print("Scissor")




def game():
    life=3
    sr=ran.randrange(1,3)
    print(sr)
    print("life:",life)
    print("score:",Myasset.score)
    print("1.Rock \n2.Paper \n3.Scissor")
    ui=int(input("Enter your option"))
    if(ui==1 and sr==2):
        Myasset.score+=1
        print("life:",life)
        print("score:",score)
    else:
        life-=1
        print("life:",life)
        print("score:",Myasset.score)





intro()
game()

print("game Score",game.score)