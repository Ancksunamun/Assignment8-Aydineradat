import random
print("welcome to Stone, scissor,cloth game. who reach score of 5 wins.best of luck"
      )

def choicee():
    print("""Please enter you choice as number:
    1.scissor
    2.stone
    3.cloth
    """)


gamechoice=('scissor','stone','cloth')

def randomchoice():
    randchoice=random.choice(gamechoice)
    return randchoice

def playerchoice(x):
    if x==1:
        return gamechoice[0]
    if x==2:
        return gamechoice[1]
    if x==3:
        return gamechoice[2]

def winning_condition():
    global playerscore
    global computerscore

    #draw condition
    if gamechoice.index(randcho)==gamechoice.index(playerchoice(num)):
        return print("draw")
    #player wining condition
    elif gamechoice.index(playerchoice(num))-gamechoice.index(randcho)==1 or gamechoice.index(playerchoice(num))-gamechoice.index(randcho)==-2:
        playerscore+=1
        return print("player wins")
    #computer wining condition
    elif gamechoice.index(randcho)-gamechoice.index(playerchoice(num))==1 or gamechoice.index(randcho)-gamechoice.index(playerchoice(num))==-2:
        computerscore+=1
        return print("computer wins")




playerscore=0
computerscore=0

while True:
    choicee()
    num = int(input("number:"))
    randcho = randomchoice()
    print(playerchoice(num) + " Vs " +randcho )
    winning_condition()
    print('player score:'+str(playerscore)+"computer score:"+str(computerscore))
    if playerscore==5 :
        print("congratulations you win")
        break
    elif computerscore==5:
        print("Opps you lost")
        break






