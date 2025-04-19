import random,time,os; clear = lambda: os.system('cls')
from PIL import Image

while True:
    print("   -=:List of commands after you're done with the inputs:=-\n\n-type 'redo' to reopen this exe\n-type 'gen1' to generate green land\n-Type 'poof' to clear array\n-type 'image' to create and store image (replaced if program restarted)\n-type 'map' to display array\n\n\n")
    try:delay1 = int(input("Delay for error checking, recomended 1000 minimum\n\n</: "));clear();break
    except:ValueError;clear()

while True:
    x = input("Width: ")
    if x[0] == ".":
        x = x.replace(x[0],"")
        try:x = y = int(x);break
        except:ValueError;clear()
    else:
        try:
            x = int(x)
            while True:
                try:y = int(input("Height: "));break
                except:ValueError;clear()
            break
        except:ValueError;clear()

world = [["." for i in range(x)]for j in range(y)]
assetCounter = 0;errorCounter = 0
def showMap():
    for i in world:print(" ".join(i))





def gen1():
    global errorCounter,delay1,toGen
    x = random.randint(0,len(world[0])-1)
    y = random.randint(0,len(world)-1)
    toGen = random.randint(0,len(world)*len(world[-1])//2)
    if world[y][x] == "#":
        while world[y][x] == "#":
            x = y = random.randint(0,len(world)-1)# anti infinite loop
    for i in range(toGen):
        if "." in world[y][x]:
            world[y][x] = "#"
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
                        if temp == 1 and world[y-z][x] != "#":# up
                            y -= z
                            world[y][x] = "#"
                            break
                        elif temp == 2 and world[y][x-z] != "#":# left
                            x -= z
                            world[y][x] = "#"
                            break
                        elif temp == 3 and world[y][x+z] != "#":# right
                            x += z
                            world[y][x] = "#"
                            break
                        elif temp == 4 and world[y+z][x] != "#":# down
                            y += z
                            world[y][x] = "#"
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
numericalOrder = 0
while True:
    global toGen
    inpt = input("</: ")
    if inpt == "redo":
        os.startfile('basic gen v2.py')
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
        #showMap()
        errorCounter = 0
    elif inpt == "poof":
        assetCounter = 0
        clear()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    world[i][l] = "."
        #showMap()
    elif inpt == "image":
        img = Image.new('RGB',(len(world[0]),len(world)),(25,25,140))
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    img.putpixel((i,l),(0,120,0))
        img.save("test{}.png".format(numericalOrder))
        img.show()
        numericalOrder += 1
    elif inpt == "map":
        showMap()
    else:
        clear()
        #showMap()
