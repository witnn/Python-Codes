#Tas Kagıt Makas
#Author : barış kıvanç #
import random as rd

tmlist = ["Rock", "Paper", "Scissors"]

print("-"*40+"\n#Welcome to the game..\n"+"-"*40)
isim = str(input("Set an username = "))

class computer:
    def __init__(self, Name):
        self.name = Name
    def oyna(self):
        self.secenek = rd.choice(tmlist)
        return self.secenek


aı = computer("V216")

def game():
    puan = 0
    while True:
        print("\n" + "-" * 20)
        print("1 - Rock \n2 - Paper \n3 - Scissors")
        print("-" * 20)

        try: a = int(input("which option you will choice? (1,2,3) = "))
        except:
            print("Wrong choice!")
            game()
        finally:
            if a == 1 or a == 2 or a == 3:
                secim = tmlist[a - 1]
                b_secim = aı.oyna()

                print("\n"+aı.name,"played with", b_secim)
                print(isim,"played with", secim)

                if secim == "Rock":
                    if b_secim == "Scissors":
                        puan += 1
                        print("You win! you have {} point.".format(puan))
                    elif b_secim == "Paper":
                        puan -= 1
                        print("You lose. you have {} point.".format(puan))
                    else:
                        print("Draw")
                if secim == "Paper":
                    if b_secim == "Scissors":
                        puan -= 1
                        print("You lose. you have {} point.".format(puan))
                    elif b_secim == "Rock":
                        puan += 1
                        print("You win! you have {} point.".format(puan))
                    else:
                        print("Draw")
                if secim == "Scissors":
                    if b_secim == "Rock":
                        puan -= 1
                        print("You lose. you have {} point.".format(puan))
                    elif b_secim == "Paper":
                        puan += 1
                        print("You win! you have {} point.".format(puan))
                    else:
                        print("Draw")
            else:
                print("Wrong choice!")
                game()
game()
