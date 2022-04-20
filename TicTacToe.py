import random

# variable setup
win = 0
pls = []
ais = []
# a/b/c are the variables for the board
a = [" ", " ", " "]
b = [" ", " ", " "]
c = [" ", " ", " "]
# available spaces on the board
av = [0, 1, 2, 3, 4, 5, 6, 7, 8]
AISpecialCase = -1

# To rig who goes first:
# Literally anything BUT 1 or 2 - Random (default)
# 1 - You go first
# 2 - AI goes first
rig = 0

# randomly pick who goes first
if random.randint(0,1) == 1:
    pxo = "X"
    axo = "O"
else:
    pxo = "O"
    axo = "X"

# check if there is a rig
if rig == 1:
    pxo = "X"
    axo = "O"
elif rig == 2:
    pxo = "O"
    axo = "X"

# prints the board
def printBoard():
    global a, b, c
    print("  1   2   3")
    print("A " + a[0] + " | " + a[1] + " | " + a[2])
    print(" ---+---+---")
    print("B " + b[0] + " | " + b[1] + " | " + b[2])
    print(" ---+---+---")
    print("C " + c[0] + " | " + c[1] + " | " + c[2])
    print("")

# AI check script
def AICheck():
    global AICheckBlock, AICheckWin
    AICheckWin()
    if AISpecialCase == -1:
        AICheckBlock()

# checks if the AI can block the other player
def AICheckBlock():
    global av, pls, AISpecialCase
    if pls.count(0) == 1:
        if pls.count(1) == 1 and av.count(2) == 1:
            AISpecialCase = 2
        elif pls.count(2) == 1 and av.count(1) == 1:
            AISpecialCase = 1
        elif pls.count(3) == 1 and av.count(6) == 1:
            AISpecialCase = 6
        elif pls.count(6) == 1 and av.count(3) == 1:
            AISpecialCase = 3
        elif pls.count(4) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif pls.count(8) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif pls.count(1) == 1:
        if pls.count(2) == 1 and av.count(0) == 1:
            AISpecialCase = 0
        elif pls.count(4) == 1 and av.count(7) == 1:
            AISpecialCase = 7
        elif pls.count(7) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif pls.count(2) == 1:
        if pls.count(5) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif pls.count(8) == 1 and av.count(5) == 1:
            AISpecialCase = 5
        elif pls.count(4) == 1 and av.count(6) == 1:
            AISpecialCase = 6
        elif pls.count(6) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif pls.count(3) == 1:
        if pls.count(4) == 1 and av.count(5) == 1:
            AISpecialCase = 5
        elif pls.count(5) == 1 and av.count(4) == 1:
            AISpecialCase = 4
        elif pls.count(6) == 1 and av.count(0) == 1:
            AISpecialCase = 0
    elif pls.count(4) == 1:
        if pls.count(5) == 1 and av.count(3) == 1:
            AISpecialCase = 3
        elif pls.count(7) == 1 and av.count(1) == 1:
            AISpecialCase = 1
        elif pls.count(8) == 1 and av.count(0) == 1:
            AISpecialCase = 0
        elif pls.count(6) == 1 and av.count(2) == 1:
            AISpecialCase = 2
    elif pls.count(5) == 1 and pls.count(8) == 1 and av.count(2) == 1:
        AISpecialCase = 2
    elif pls.count(6) == 1:
        if pls.count(7) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif pls.count(8) == 1 and av.count(7) == 1:
            AISpecialCase = 7
    elif pls.count(7) == 1 and pls.count(8) == 1 and av.count(6) == 1:
        AISpecialCase = 1

# checks if the AI can win (favored over blocking)
def AICheckWin():
    global av, ais, AISpecialCase
    if ais.count(0) == 1:
        if ais.count(1) == 1 and av.count(2) == 1:
            AISpecialCase = 2
        elif ais.count(2) == 1 and av.count(1) == 1:
            AISpecialCase = 1
        elif ais.count(3) == 1 and av.count(6) == 1:
            AISpecialCase = 6
        elif ais.count(6) == 1 and av.count(3) == 1:
            AISpecialCase = 3
        elif ais.count(4) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif ais.count(8) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif ais.count(1) == 1:
        if ais.count(2) == 1 and av.count(0) == 1:
            AISpecialCase = 0
        elif ais.count(4) == 1 and av.count(7) == 1:
            AISpecialCase = 7
        elif ais.count(7) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif ais.count(2) == 1:
        if ais.count(5) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif ais.count(8) == 1 and av.count(5) == 1:
            AISpecialCase = 5
        elif ais.count(4) == 1 and av.count(6) == 1:
            AISpecialCase = 6
        elif ais.count(6) == 1 and av.count(4) == 1:
            AISpecialCase = 4
    elif ais.count(3) == 1:
        if ais.count(4) == 1 and av.count(5) == 1:
            AISpecialCase = 5
        elif ais.count(5) == 1 and av.count(4) == 1:
            AISpecialCase = 4
        elif ais.count(6) == 1 and av.count(0) == 1:
            AISpecialCase = 0
    elif ais.count(4) == 1:
        if ais.count(5) == 1 and av.count(3) == 1:
            AISpecialCase = 3
        elif ais.count(7) == 1 and av.count(1) == 1:
            AISpecialCase = 1
        elif ais.count(8) == 1 and av.count(0) == 1:
            AISpecialCase = 0
        elif ais.count(6) == 1 and av.count(2) == 1:
            AISpecialCase = 2
    elif ais.count(5) == 1 and ais.count(8) == 1 and av.count(2) == 1:
        AISpecialCase = 2
    elif ais.count(6) == 1:
        if ais.count(7) == 1 and av.count(8) == 1:
            AISpecialCase = 8
        elif ais.count(8) == 1 and av.count(7) == 1:
            AISpecialCase = 7
    elif ais.count(7) == 1 and ais.count(8) == 1 and av.count(6) == 1:
        AISpecialCase = 1

# what happens during the AI's turn
def AITurn(xo):
    global a, b, c, AISpecialCase, av, ais
    if AISpecialCase != -1:
        which = AISpecialCase
        AISpecialCase = -1
    else:
        which = av[random.randint(0, len(av) - 1)]
    av.remove(which)
    ais.append(which)
    if which <= 2:
        a[which] = xo
    elif which <= 5:
        which += -3
        b[which] = xo
    else:
        which += -6
        c[which] = xo

# what happens during the player's turn
def PlayerTurn(xo):
    global a, b, c, av, pls
    goodInput = 0
    while goodInput == 0:
        inp = input("What space would you like to play: ").lower()
        if inp == "a1" and av.count(0) == 1:
            goodInput = 1
            which = 0
        elif inp == "a2" and av.count(1) == 1:
            goodInput = 1
            which = 1
        elif inp == "a3" and av.count(2) == 1:
            goodInput = 1
            which = 2
        elif inp == "b1" and av.count(3) == 1:
            goodInput = 1
            which = 3
        elif inp == "b2" and av.count(4) == 1:
            goodInput = 1
            which = 4
        elif inp == "b3" and av.count(5) == 1:
            goodInput = 1
            which = 5
        elif inp == "c1" and av.count(6) == 1:
            goodInput = 1
            which = 6
        elif inp == "c2" and av.count(7) == 1:
            goodInput = 1
            which = 7
        elif inp == "c3" and av.count(8) == 1:
            goodInput = 1
            which = 8
    av.remove(which)
    pls.append(which)
    if which <= 2:
        a[which] = xo
    elif which <= 5:
        which += -3
        b[which] = xo
    else:
        which += -6
        c[which] = xo

# checks if either side has won
def checkIfWin():
    global win, av
    if len(av) == 0:
        win = 3
    
    if pls.count(0) == 1 and pls.count(1) == 1 and pls.count(2) == 1:
        win = 1
    elif pls.count(3) == 1 and pls.count(4) == 1 and pls.count(5) == 1:
        win = 1
    elif pls.count(6) == 1 and pls.count(7) == 1 and pls.count(8) == 1:
        win = 1
    elif pls.count(0) == 1 and pls.count(3) == 1 and pls.count(6) == 1:
        win = 1
    elif pls.count(1) == 1 and pls.count(4) == 1 and pls.count(7) == 1:
        win = 1
    elif pls.count(2) == 1 and pls.count(5) == 1 and pls.count(8) == 1:
        win = 1
    elif pls.count(0) == 1 and pls.count(4) == 1 and pls.count(8) == 1:
        win = 1
    elif pls.count(2) == 1 and pls.count(4) == 1 and pls.count(6) == 1:
        win = 1
    
    if ais.count(0) == 1 and ais.count(1) == 1 and ais.count(2) == 1:
        win = 2
    elif ais.count(3) == 1 and ais.count(4) == 1 and ais.count(5) == 1:
        win = 2
    elif ais.count(6) == 1 and ais.count(7) == 1 and ais.count(8) == 1:
        win = 2
    elif ais.count(0) == 1 and ais.count(3) == 1 and ais.count(6) == 1:
        win = 2
    elif ais.count(1) == 1 and ais.count(4) == 1 and ais.count(7) == 1:
        win = 2
    elif ais.count(2) == 1 and ais.count(5) == 1 and ais.count(8) == 1:
        win = 2
    elif ais.count(0) == 1 and ais.count(4) == 1 and ais.count(8) == 1:
        win = 2
    elif ais.count(2) == 1 and ais.count(4) == 1 and ais.count(6) == 1:
        win = 2

    if win == 1:
        print("You win! Congradulations! :D")
    elif win == 2:
        print("YOU LOST!!! HOW COULD YOU!???!? D:")
    elif win == 3:
        print("You tied? 😳")

# for loop because it is impossible to do 5 turns each or more
for i in range(5):
    # X always goes first, so this just checks to make sure X is going first
    if axo == "X":
        AICheck()
        AITurn(axo)
        checkIfWin()
        if win == 2 or win == 3:
            break
        printBoard()
        PlayerTurn(pxo)
        checkIfWin()
        if win == 1 or win == 3:
            break
    else:
        printBoard()
        PlayerTurn(pxo)
        checkIfWin()
        if win == 1 or win == 3:
            break
        AICheck()
        AITurn(axo)
        checkIfWin()
        if win == 2 or win == 3:
            break
printBoard()
print("Press enter to close this window.")
input()
