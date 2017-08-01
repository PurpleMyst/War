from random import randint

playerA = []
playerB = []
cards = ["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"]
hierarchy = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

def dealCards():
    while len(cards) > 0:
        x = randint(0,len(cards)-1)
        playerA.append(cards[x])
        del.cards[x]
        x = randint(0,len(cards)-1)
        playerB.append(cards[x])
        del.cards[x]                #cards are dealt in a random order, thus they are shuffled during dealing

def compare(a, b):
    if hierarchy.index(a) > hierarchy.index(b):
        return 0
    elif hierarchy.index(a) < hierarchy.index(b)
        return 1
    

def war():
    winnings= []
    while playerA[0] == playerB[0]:
        print ("War!")
        print ("Player A plays a" + playerA[0] + "!")
        print ("Player B plays a" + playerB[0] + "!")
        winnings.append(playerA[0:4])
        winnings.append(playerB[0:4])
        del.playerA[0:4]
        del.playerB[0:4]
        if hierarchy.index(playerA[0]) > hierarchy.index(playerB[0]):
            print "Player A wins the war!"
            playerA.append(winnings)
            playerA.append(playerA[0])
            playerA.append(playerB[0])
        elif hierarchy.index(playerA[0]) < hierarchy.index(playerB[0]):
            print "Player B wins the war!"
            playerB.append(winnings)
            playerB.append(playerA[0])
            playerB.append(playerB[0])

dealCards()
while ((len(playerA) > 0) and (len(playerB) > 0))
    print ("Player A plays a" + playerA[0] + "!")
    print ("Player B plays a" + playerB[0] + "!")
    if playerA[0] == playerB[0]:
        war()
    elif hierarchy.index(playerA[0]) > hierarchy.index(playerB[0]):
        print "Player A wins the card!"
        playerA.append(playerB[0])
        playerA.append(playerA[0])
    else:
        print "Player B wins the card!"
        playerB.append(playerB[0])
        playerB.append(playerA[0])
    del.playerA[0]
    del.playerB[0]
    print ("Player A has " + str(len(playerA)) + " cards!")
    print ("Player B has " + str(len(playerB)) + " cards!") 
if len(playerA) == 0
    print "Player B wins!"
elif len(playerB) == 0
    print "Player A wins!"