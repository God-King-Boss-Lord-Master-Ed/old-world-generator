import random,time,os; clear = lambda: os.system('cls')
print("   -=:List of commands after you're done with the inputs:=-\n\n-type 'redo' to reopen this exe\n-type 'gen1' to generate\n-Type 'poof' to clear array\n\n\n")
delay1 = int(input("Delay for error checking, recomended 1000 minimum\n\n</: "))
clear()
x = y = int(input("Coords(x,y): "))
world = [["." for i in range(x)]for j in range(y)]
assetCounter = 0

errorCounter = 0
def showMap():
    for i in world:
        print(" ".join(i))


def gen1():
    global errorCounter,delay1,toGen
    x = y = random.randint(0,len(world)-1)
    toGen = random.randint(0,len(world)*len(world[-1])//2)
    if world[x][y] == "#":
        while world[x][y] == "#":
            x = y = random.randint(0,len(world)-1)# anti infinite loop
    for i in range(toGen):
        if "." in world[x][y]:
            world[x][y] = "#"
        else:
            temp = random.randint(1,4)
            z = 1
            while True:
                errorCounter += 1
                if errorCounter >= delay1:
                    break
                else:
                    print(errorCounter)
                    try:
                        if temp == 1 and world[x-z][y] != "#":# up
                            x -= z
                            world[x][y] = "#"
                            break
                        elif temp == 2 and world[x][y-z] != "#":# left
                            y -= z
                            world[x][y] = "#"
                            break
                        elif temp == 3 and world[x][y+z] != "#":# right
                            y += z
                            world[x][y] = "#"
                            break
                        elif temp == 4 and world[x+z][y] != "#":# down
                            x += z
                            world[x][y] = "#"
                            break
                        else:
                            z += 1
                    except:
                        IndexError
                        if temp >= 4:
                            temp = 1
                        else:
                            temp += 1
clear()
showMap()
while True:
    global toGen
    inpt = input("</: ")
    if inpt == "redo":
        os.startfile('basic gen v1.py')
        sys.exit()
    elif inpt == "gen1":
        clear()
        gen1()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    assetCounter += 1
        print("\nAssets generated this runtime:",toGen,"\nCurrent asset count:",assetCounter)
        assetCounter = 0
        showMap()
        errorCounter = 0
    elif inpt == "poof":
        assetCounter = 0
        clear()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    world[i][l] = "."
        showMap()
    else:
        clear()
        showMap()
