import random,time,os; clear = lambda: os.system('cls')
from PIL import Image

#------------------------- variables ------------------------------------------------#

informationForUse = "\n\n-type 'info' to display this list of information\
\n-type 'redo' to reopen this exe\
\n-type 'gen1' to generate green land\
\n-type 'gen2' to generate sand\
\n-Type 'poof' to clear array\
\n-type 'image' to create and store image (replaced if program restarted)\
\n-type 'image2' to create and store image.v2 (replaced if program restarted)\
\n-type 'map' to display array\
\n-advanced command 'set' same coords example 'set.5', different coords example 'set.5,7'\
\n-type 'clean1' to clean world of one pixel holes\
\n-type 'clean2' to clean world of 2x2 to pixel holes\
\n-type 'clean3' to clean world of random 1 pixel wide spikes and stuff\
\n-type 'clean4' to use all clean commands in order [clean3,(clean1,clean2(looped)),clean3]\
\n-type 'save' to save copy as number e.g. 'save1' (current session only)\
\n-type 'load.(number)' to load a saved copy (current session only)\n\n\n"

#------------------------- start ------------------------------------------------#

while True:
    print("   -=:List of commands after you're done with the inputs:=-",informationForUse)
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

#------------------------- def///display arrray ------------------------------------------------#

world = [["." for i in range(x)]for j in range(y)]
assetCounter = 0;errorCounter = 0
def showMap():
    for i in world:print(" ".join(i))

#------------------------- def///generate land (grass) ------------------------------------------------#

def gen1():
    global errorCounter,delay1,toGen
    #x = random.randint(0,len(world[0])-1)
    #y = random.randint(0,len(world)-1)
    x = len(world)//2
    y = len(world[0])//2
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

#------------------------- def///generate beaches (sand) ------------------------------------------------#

def gen2(beachSize):
    for l in range(len(world)):
        for i in range(len(world[0])):
            try:
                if world[l][i] in "#s" and world[l+1][i] == ".":# up
                    for f in range(beachSize):
                        try:
                            if world[l-f][i] == ".":
                                break
                            else:
                                world[l-f][i] = "s"
                        except:
                            IndexError

                if world[l][i] in "#s" and world[l-1][i] == ".":# down
                    for f in range(beachSize):
                        try:
                            if world[l+f][i] == ".":
                                break
                            else:
                                world[l+f][i] = "s"
                        except:
                            IndexError

                if world[l][i] in "#s" and world[l][i+1] == ".":# left
                    for f in range(beachSize):
                        try:
                            if world[l][i-f] == ".":
                                break
                            else:
                                world[l][i-f] = "s"
                        except:
                            IndexError

                if world[l][i] in "#s" and world[l][i-1] == ".":# right
                    for f in range(beachSize):
                        try:
                            if world[l][i+f] == ".":
                                break
                            else:
                                world[l][i+f] = "s"
                        except:
                            IndexError
            except:
                IndexError
    for l in range(len(world)):
        for i in range(len(world[0])):
            try:
                if world[l][i] == "." and world[l-1][i] in ["#","s"] and world[l-2][i] in ["#","s"] and world[l-3][i] in ["#","s"] and world[l-4][i] in ["#","s"] and world[l-5][i] in ["#","s"]\
                    and world[l][i+1] in ["#","s"] and world[l][i+2] in ["#","s"] and world[l][i+3] in ["#","s"] and world[l][i+4] in ["#","s"] and world[l][i+5] in ["#","s"]:# up right
                    for x in range(4):
                        for n in range(4):
                            if world[l-1-x][i+1+n] != ".":
                                world[l-1-x][i+1+n] = "s"

                if world[l][i] == "." and world[l+1][i] in ["#","s"] and world[l+2][i] in ["#","s"] and world[l+3][i] in ["#","s"] and world[l+4][i] in ["#","s"] and world[l+5][i] in ["#","s"]\
                    and world[l][i+1] in ["#","s"] and world[l][i+2] in ["#","s"] and world[l][i+3] in ["#","s"] and world[l][i+4] in ["#","s"] and world[l][i+5] in ["#","s"]:# down right
                    for x in range(4):
                        for n in range(4):
                            if world[l+1+x][i+1+n] != ".":
                                world[l+1+x][i+1+n] = "s"

                if world[l][i] == "." and world[l+1][i] in ["#","s"] and world[l+2][i] in ["#","s"] and world[l+3][i] in ["#","s"] and world[l+4][i] in ["#","s"] and world[l+5][i] in ["#","s"]\
                    and world[l][i-1] in ["#","s"] and world[l][i-2] in ["#","s"] and world[l][i-3] in ["#","s"] and world[l][i-4] in ["#","s"] and world[l][i-5] in ["#","s"]:# down left
                    for x in range(4):
                        for n in range(4):
                            if world[l+1+x][i-1-n] != ".":
                                world[l+1+x][i-1-n] = "s"

                if world[l][i] == "." and world[l-1][i] in ["#","s"] and world[l-2][i] in ["#","s"] and world[l-3][i] in ["#","s"] and world[l-4][i] in ["#","s"] and world[l-5][i] in ["#","s"]\
                    and world[l][i-1] in ["#","s"] and world[l][i-2] in ["#","s"] and world[l][i-3] in ["#","s"] and world[l][i-4] in ["#","s"] and world[l][i-5] in ["#","s"]:# up right
                    for x in range(4):
                        for n in range(4):
                            if world[l-1-x][i-1-n] != ".":
                                world[l-1-x][i-1-n] = "s"
            except:
                IndexError
                        
#------------------------- def///clean up 1 pixel holes ------------------------------------------------#

clear()
numericalOrder = 0
def mapCleaner():
    for l in range(len(world)):
        for i in range(len(world[0])):
            if world[l][i] == ".":
                try:
                    if world[l][i-1] == "#" and world[l][i+1] == "#"\
                       or world[l-1][i] == "#" and world[l+1][i] == "#":# left & right or up & down
                        world[l][i] = "#"
                except:
                    IndexError

#------------------------- def///clean up 2x2 pixel holes ------------------------------------------------#

def mapCleaner2():
    for l in range(len(world)):
        for i in range(len(world[0])):
            try:
                if world[l][i] == "." and world[l][i-1] == "." and world[l+1][i] == "." and world[l+1][i-1] == ".":
                    try:
                        if world[l][i-2] == "#" and world[l][i+1] == "#" and world[l+1][i-2] == "#" and world[l+1][i+1] == "#"\
                           or world[l-1][i] == "#" and world[l-1][i-1] == "#" and world[l+2][i] == "#" and world[l+2][i-1] == "#":# left & right or up and & down
                            world[l][i] = "#"
                            world[l][i-1] = "#"
                            world[l+1][i] = "#"
                            world[l+1][i-1] = "#"
                    except:
                        IndexError
            except:
                IndexError

#------------------------- def///clean up 1x wide pixel spikes (improved) ------------------------------------------------#

def mapCleaner3():
    for l in range(len(world)):
        for i in range(len(world[0])):
            if world[l][i] == "#":
                try:
                    if world[l][i] == "#" and world[l][i-1] == "." and world[l][i+1] == "."\
                       or world[l][i] == "#" and world[l-1][i] == "." and world[l+1][i] == ".":
                           world[l][i] = "."
                except:
                    IndexError                    

#------------------------- MAIN LOOP ------------------------------------------------#                      
    
while True:
    global toGen
    inpt = input("</: ")

#------------------------- info ------------------------------------------------#

    if inpt == "info":
        print(informationForUse)

#------------------------- redo ------------------------------------------------#
       
    elif inpt == "redo":
        os.startfile('basic gen v4.py')
        sys.exit()

#------------------------- gen1 ------------------------------------------------#

    elif inpt == "gen1":
        clear()
        gen1()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    assetCounter += 1
        print("\nAssets generated this runtime:",toGen,"\nCurrent asset count:",assetCounter)
        assetCounter = 0
        errorCounter = 0

#------------------------- gen1 ------------------------------------------------#

    elif inpt[:4] == "gen2":
        beachSize = 5
        if inpt.count(".") == 1:
            inpt = inpt.split(".")[1]
            try:
                int(inpt)
                beachSize = int(inpt)
            except:
                ValueError
                pass
        clear()
        gen2(beachSize)
        print("Beach generation complete!")

#------------------------- poof ------------------------------------------------#

    elif inpt == "poof":
        assetCounter = 0
        clear()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] != ".":
                    world[i][l] = "."

#------------------------- image ------------------------------------------------#

    elif inpt == "image":
        img = Image.new('RGB',(len(world[0]),len(world)),(25,25,140))# water
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    img.putpixel((i,l),(0,120,0))
                elif world[l][i] == "s":
                    img.putpixel((i,l),(255,255,0))
        img.save("v1-test{}.png".format(numericalOrder))
        numericalOrder += 1

#------------------------- image2 ------------------------------------------------#

    elif inpt == "image2":
        greenland_asset = Image.open('testing3.png')
        sand_asset = Image.open('testing4.png')
        img = Image.new('RGB',(len(world[0])*15,len(world)*15),(25,25,140))# water
        y = 0
        for l in range(len(world)):
            x = 0
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    img.paste(greenland_asset,(i+x,l+y))
                elif world[l][i] == "s":
                    img.paste(sand_asset,(i+x,l+y))
                x += 14
            y += 14
        img.save("v2-test{}.png".format(numericalOrder))
        numericalOrder += 1

#------------------------- map ------------------------------------------------#

    elif inpt == "map":
        showMap()

#------------------------- set ------------------------------------------------#

    elif inpt[:3] == "set":
        try:
            inpt = inpt.split(".")[1]
            if "," in inpt and inpt.count(",") == 1:
                inpt = inpt.split(",")
                world[int(inpt[0])][int(inpt[1])] = "#"
            else:
                world[int(inpt)][int(inpt)] = "#"
        except:
            IndexError
            pass
        

#------------------------- clean1 ------------------------------------------------#

    elif inpt == "clean1":
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == ".":
                    try:
                        if world[l][i-1] == "#" and world[l][i+1] == "#"\
                           or world[l-1][i] == "#" and world[l+1][i] == "#":
                            print("cleaning...")
                            mapCleaner()
                            break
                    except:
                        IndexError

#------------------------- clean2 ------------------------------------------------#

    elif inpt == "clean2":
        for l in range(len(world)):
            for i in range(len(world[0])):
                try:
                    if world[l][i] == "." and world[l][i-1] == "." and world[l+1][i] == "." and world[l+1][i-1] == ".":
                        try:
                            if world[l][i-2] == "#" and world[l][i+1] == "#" and world[l+1][i-2] == "#" and world[l+1][i+1] == "#"\
                               or world[l-1][i] == "#" and world[l-1][i-1] == "#" and world[l+2][i] == "#" and world[l+2][i-1] == "#":
                                print("cleaning...")
                                mapCleaner2()
                                break
                        except:
                            IndexError
                except:
                    IndexError

#------------------------- clean3 ------------------------------------------------#

    elif inpt == "clean3":
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    try:
                        if world[l][i] == "#" and world[l][i-1] == "." and world[l][i+1] == "."\
                           or world[l][i] == "#" and world[l-1][i] == "." and world[l+1][i] == ".":
                               print("cleaning...")
                               mapCleaner3()
                               break
                    except:
                        IndexError

#------------------------- clean4 ------------------------------------------------#

    elif inpt == "clean4":
        # clean3
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    try:
                        if world[l][i] == "#" and world[l][i-1] == "." and world[l][i+1] == "."\
                           or world[l][i] == "#" and world[l-1][i] == "." and world[l+1][i] == ".":
                               print("cleaning...")
                               mapCleaner3()
                               break
                    except:
                        IndexError
        tempCounter1 = 2
        while tempCounter1 > 0:
            tempCounter1 = 0
            # clean1
            for l in range(len(world)):
                for i in range(len(world[0])):
                    if world[l][i] == ".":
                        try:
                            if world[l][i-1] == "#" and world[l][i+1] == "#"\
                               or world[l-1][i] == "#" and world[l+1][i] == "#":
                                print("cleaning...")
                                mapCleaner()
                                tempCounter1 += 1
                                break
                        except:
                            IndexError
            # clean2
            for l in range(len(world)):
                        for i in range(len(world[0])):
                            try:
                                if world[l][i] == "." and world[l][i-1] == "." and world[l+1][i] == "." and world[l+1][i-1] == ".":
                                    try:
                                        if world[l][i-2] == "#" and world[l][i+1] == "#" and world[l+1][i-2] == "#" and world[l+1][i+1] == "#"\
                                           or world[l-1][i] == "#" and world[l-1][i-1] == "#" and world[l+2][i] == "#" and world[l+2][i-1] == "#":
                                            print("cleaning...")
                                            mapCleaner2()
                                            tempCounter1 += 1
                                            break
                                    except:
                                        IndexError
                            except:
                                IndexError
        # clean3
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    try:
                        if world[l][i] == "#" and world[l][i-1] == "." and world[l][i+1] == "."\
                           or world[l][i] == "#" and world[l-1][i] == "." and world[l+1][i] == ".":
                               print("cleaning...")
                               mapCleaner3()
                               break
                    except:
                        IndexError


#------------------------- save ------------------------------------------------#

    elif inpt == "save":
        i = 0
        while True:
            if f'save{i}' not in globals():
                print(f"saved as 'save{i}'")
                break
            else:
                i += 1
        exec(f'save{i} = list(map(list,world))',globals())

#------------------------- load ------------------------------------------------#

    elif inpt[:4] == "load":
        try:
            int(inpt.split(".")[1])
            if f'save{int(inpt.split(".")[1])}' in globals():
                exec(f'world = list(map(list,save{int(inpt.split(".")[1])}))')
                print("Loading...")
        except:
            ValueError
            pass

#------------------------- unknown input ------------------------------------------------#

    else:
        clear()
