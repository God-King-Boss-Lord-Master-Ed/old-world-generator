import random,time,os; clear = lambda: os.system('cls')
from PIL import Image

#------------------------- variables ------------------------------------------------#

informationForUse = "\n\n-type 'info' to display this list of information\
\n-type 'redo' to reopen this exe\
\n-type 'gen1' to generate green land\
\n-type 'gen2' to generate sand\
\n-type 'gen2_alt' use after gen2, makes world smoother but deducts some land\
\n-Type 'poof' to clear array\
\n-type 'image' to create and store image (replaced if program restarted)\
\n-type 'image2' to create and store image.v2 (replaced if program restarted)\
\n-type 'map' to display array\
\n-advanced command 'set' same coords example 'set.5', different coords example 'set.5,7'\
\n-advanced command 'genRiver{.(amount)}'\
\n-type 'clean1' to use all clean commands in order [clean3,(clean1,clean2(looped)),clean3]\
\n-type 'clean2' to clean holes in land(ponds and stuff)\
\n-type 'clean3' to clean 2x2 or 1x2\
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

#------------------------- def///generate beaches (sand)(cleaner) ------------------------------------------------#

def gen2_cleaner(setAllAsset):
    for l in range(len(world)-1):
        for i in range(len(world[0])-1):
            if world[l][i] == "s":
                world[l][i] = "."

    for l in range(len(world)-1):
        for i in range(len(world[0])-1):
            if world[l][i] == "#" and world[l-1][i] == "." or\
               world[l][i] == "#" and world[l][i+1] == "." or\
               world[l][i] == "#" and world[l+1][i] == "." or\
               world[l][i] == "#" and world[l][i-1] == ".":
                world[l][i] = ","
    allAsset = [".",","]
    for l in range(len(world)-1):# make circles on ','
        for i in range(len(world[0])-1):
            
            if world[l][i] == ",":
                # top right
                for d in range(3):
                    for k in range(7):
                        k += 1
                        try:
                            if world[l-k][i+d] not in allAsset:
                                world[l-k][i+d] = setAllAsset
                        except:
                            IndexError

                for d in range(2):
                    d += 3
                    for k in range(6):
                        k += 1
                        try:
                            if world[l-k][i+d] not in allAsset:
                                world[l-k][i+d] = setAllAsset
                        except:
                            IndexError

                for k in range(5):
                    k += 1
                    try:
                        if world[l-k][i+5] not in allAsset:
                            world[l-k][i+5] = setAllAsset
                    except:
                        IndexError

                for k in range(4):
                    k += 1
                    try:
                        if world[l-k][i+6] not in allAsset:
                            world[l-k][i+6] = setAllAsset
                    except:
                        IndexError

                for k in range(2):
                    k += 1
                    try:
                        if world[l-k][i+7] not in allAsset:
                            world[l-k][i+7] = setAllAsset
                    except:
                        IndexError
                # bottom right
                for d in range(3):
                    for k in range(7):
                        k += 1
                        try:
                            if world[l+d][i+k] not in allAsset:
                                world[l+d][i+k] = setAllAsset
                        except:
                            IndexError

                for d in range(2):
                    d += 3
                    for k in range(6):
                        k += 1
                        try:
                            if world[l+d][i+k] not in allAsset:
                                world[l+d][i+k] = setAllAsset
                        except:
                            IndexError

                for k in range(5):
                    k += 1
                    try:
                        if world[l+5][i+k] not in allAsset:
                            world[l+5][i+k] = setAllAsset
                    except:
                        IndexError

                for k in range(4):
                    k += 1
                    try:
                        if world[l+6][i+k] not in allAsset:
                            world[l+6][i+k] = setAllAsset
                    except:
                        IndexError

                for k in range(2):
                    k += 1
                    try:
                        if world[l+7][i+k] not in allAsset:
                            world[l+7][i+k] = setAllAsset
                    except:
                        IndexError
                # bottom left
                for d in range(3):
                    for k in range(7):
                        k += 1
                        try:
                            if world[l+k][i-d] not in allAsset:
                                world[l+k][i-d] = setAllAsset
                        except:
                            IndexError

                for d in range(2):
                    d += 3
                    for k in range(6):
                        k += 1
                        try:
                            if world[l+k][i-d] not in allAsset:
                                world[l+k][i-d] = setAllAsset
                        except:
                            IndexError

                for k in range(5):
                    k += 1
                    try:
                        if world[l+k][i-5] not in allAsset:
                            world[l+k][i-5] = setAllAsset
                    except:
                        IndexError

                for k in range(4):
                    k += 1
                    try:
                        if world[l+k][i-6] not in allAsset:
                            world[l+k][i-6] = setAllAsset
                    except:
                        IndexError

                for k in range(2):
                    k += 1
                    try:
                        if world[l+k][i-7] not in allAsset:
                            world[l+k][i-7] = setAllAsset
                    except:
                        IndexError
                # top left
                for d in range(3):
                    for k in range(7):
                        k += 1
                        try:
                            if world[l-d][i-k] not in allAsset:
                                world[l-d][i-k] = setAllAsset
                        except:
                            IndexError

                for d in range(2):
                    d += 3
                    for k in range(6):
                        k += 1
                        try:
                            if world[l-d][i-k] not in allAsset:
                                world[l-d][i-k] = setAllAsset
                        except:
                            IndexError

                for k in range(5):
                    k += 1
                    try:
                        if world[l-5][i-k] not in allAsset:
                            world[l-5][i-k] = setAllAsset
                    except:
                        IndexError

                for k in range(4):
                    k += 1
                    try:
                        if world[l-6][i-k] not in allAsset:
                            world[l-6][i-k] = setAllAsset
                    except:
                        IndexError

                for k in range(2):
                    k += 1
                    try:
                        if world[l-7][i-k] not in allAsset:
                            world[l-7][i-k] = setAllAsset
                    except:
                        IndexError

    for l in range(len(world)-1):
        for i in range(len(world[0])-1):
            if world[l][i] == ",":
                world[l][i] = setAllAsset



                
                            
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

#------------------------- def///clean up ponds and stuff in land ------------------------------------------------#

def mapCleaner4(locationToStart):
    if locationToStart in [1,2,3,4]:
        if locationToStart == 1:
            world[0][0] = ","# top left
        elif locationToStart == 2:
            world[len(world)-1][0] = ","# bottom left
            
        elif locationToStart == 3:
            world[len(world)-1][len(world[0])-1] = ","# bottom right
            
        elif locationToStart == 4:
            world[0][len(world[0])-1] = ","# top right
        for f in range(2):
            for l in range(len(world)-1):
                for i in range(len(world[0])-1):
                    try:
                        if world[l][i-1] == "," and world[l][i] != "#" or\
                           world[l-1][i] == "," and world[l][i] != "#" or\
                           world[l][i+1] == "," and world[l][i] != "#" or\
                           world[l+1][i] == "," and world[l][i] != "#":# top left to bottom right
                            world[l][i] = ","
                        else:
                            pass
                    except:
                        IndexError
    
            for l in range(len(world)-1):
                t = len(world)-1-l
                for i in range(len(world[0])-1):
                    z = len(world[0])-1-i
                    try:
                        if world[t][z-1] == "," and world[t][z] != "#" or\
                           world[t-1][z] == "," and world[t][z] != "#" or\
                           world[t][z+1] == "," and world[t][z] != "#" or\
                           world[t+1][z] == "," and world[t][z] != "#":# bottom right to top left
                            world[t][z] = ","
                        else:
                            pass
                    except:
                        IndexError
                    
            for l in range(len(world)-1):
                for i in range(len(world[0])-1):
                    z = len(world[0])-1-i
                    try:
                        if world[l][z-1] == "," and world[l][z] != "#" or\
                           world[l-1][z] == "," and world[l][z] != "#" or\
                           world[l][z+1] == "," and world[l][z] != "#" or\
                           world[l+1][z] == "," and world[l][z] != "#":# top right to bottom left
                            world[l][z] = ","
                        else:
                            pass
                    except:
                        IndexError
                    
            for l in range(len(world)-1):
                t = len(world)-1-l
                for i in range(len(world[0])-1):
                    try:
                        if world[t][i-1] == "," and world[t][i] != "#" or\
                           world[t-1][i] == "," and world[t][i] != "#" or\
                           world[t][i+1] == "," and world[t][i] != "#" or\
                           world[t+1][i] == "," and world[t][i] != "#":# bottom left to top right
                            world[t][i] = ","
                        else:
                            pass
                    except:
                        IndexError
                        
        for l in range(len(world)-1):
            for i in range(len(world[0])-1):
                if world[l][i] == ".":
                    world[l][i] = "#"

        for l in range(len(world)):
            for i in range(len(world[0])):
                try:
                    if world[l][i] == ",":
                        world[l][i] = "."
                except:
                    IndexError
    else:
        pass


#------------------------- def//clean up 2x1 wide bits ------------------------------------------------#

def mapCleaner5():
    for l in range(len(world)):
        for i in range(len(world[0])):
            if world[l][i] == "#":
                try:
                    if world[l][i] == "#" and world[l][i+1] == "#" and world[l][i-1] == "." and world[l][i+2] == ".":
                        world[l][i] = world[l][i+1] = "."
                    if world[l][i] == "#" and world[l+1][i] == "#" and world[l-1][i] == "." and world[l+2][i] == ".":
                        world[l][i] = world[l+1][i] = "."
                except:
                    IndexError

#------------------------- def//clean up 3x1 wide bits ------------------------------------------------#

def mapCleaner6():
    for l in range(len(world)):
        for i in range(len(world[0])):
            if world[l][i] == "#":
                try:
                    if world[l][i] == "#" and world[l][i+1] == "#" and world[l][i+2] == "#" and world[l][i-1] == "." and world[l][i+3] == ".":
                        world[l][i] = world[l][i+1] = world[l][i+2] ="."
                    if world[l][i] == "#" and world[l+1][i] == "#" and world[l+2][i] == "#" and world[l-1][i] == "." and world[l+3][i] == ".":
                        world[l][i] = world[l+1][i] = world[l+2][i] = "."
                except:
                    IndexError

#------------------------- def//generate rivers ------------------------------------------------#

def genRiv(amount):
    a = b = x = y = 0# 1,2,1,2
    for k in range(amount):
        while True:
            a = random.randint(0,len(world)-1)
            b = random.randint(0,len(world[0])-1)
            if world[a][b] in "#s":
                break
        while True:
            x = random.randint(0,len(world)-1)
            y = random.randint(0,len(world[0])-1)
            if world[x][y] == ".":
                break
        while True:
            if a < x:
                a += random.randint(0,1)
                world[a][b] = "."
            if a > x:
                a -= random.randint(0,1)
                world[a][b] = "."
            if b < y:
                b += random.randint(0,1)
                world[a][b] = "."
            if b > y:
                b -= random.randint(0,1)
                world[a][b] = "."
            if a == x and b == y:
                world[a][b] = "."
                break

#------------------------- def//clean combined ------------------------------------------------#    

def clean1():
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


#------------------------- MAIN LOOP ------------------------------------------------#                      
    
while True:
    global toGen
    inpt = input("</: ")

#------------------------- info ------------------------------------------------#

    if inpt == "info":
        print(informationForUse)

#------------------------- redo ------------------------------------------------#
       
    elif inpt == "redo":
        os.startfile('basic gen v5.py')
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

#------------------------- gen2 ------------------------------------------------#

    elif inpt[:4] == "gen2":
        if inpt == "gen2_alt":
            #setAllAsset = "#"
            gen2_cleaner("#")
            print("Smoothened out land")
            beachSize = 5
            if inpt.count(".") == 1:
                inpt = inpt.split(".")[1]
                try:
                    int(inpt)
                    beachSize = int(inpt)
                except:
                    ValueError
                    pass
            gen2(beachSize)
            print("Beach generation complete!")

        elif inpt == "gen2_alt.og":
            gen2_cleaner("s")
            print("Smoothened out land")

        elif inpt == "gen2_alt2.og":
            gen2_cleaner("#")
            print("Smoothened out land")
            
        else:
            beachSize = 5
            if inpt.count(".") == 1:
                inpt = inpt.split(".")[1]
                try:
                    int(inpt)
                    beachSize = int(inpt)
                except:
                    ValueError
                    pass
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
        
#------------------------- clean ------------------------------------------------#

    elif inpt == "clean":
        clean1()

#------------------------- generate river ------------------------------------------------#

    elif inpt[:8] == "genRiver":
        try:
            inpt = inpt.split(".")[1]
            genRiv(int(inpt))
        except:
            IndexError
            pass

#------------------------- clean2 ------------------------------------------------#

    elif inpt == "clean2":
        locationToStart = 0
        while True:
            # top left
            check1 = False
            try:
                for l in range(0,len(world)//10):
                    for i in range(0,len(world[0])//10):
                        if world[l][i] in ["s","#",","]:
                            check1 = True
                            break
                        else:
                            pass
                    if check1 == True:
                        break
            except:
                IndexError
            if check1 == False:
                locationToStart = 1
                break
            

            # bottom left
            check1 = False
            try:
                for l in range(len(world)//10*9,len(world)):
                    for i in range(0,len(world[0])//10):
                        if world[l][i] in ["s","#",","]:
                            check1 = True
                            break
                        else:
                            pass
                    if check1 == True:
                        break
            except:
                IndexError
            if check1 == False:
                locationToStart = 2
                break 

            # bottom right
            check1 = False
            try:
                for l in range(len(world)//10*9,len(world)):
                    for i in range(len(world[0])//10*9,len(world[0])):
                        if world[l][i] in ["s","#",","]:
                            check1 = True
                            break
                        else:
                            pass
                    if check1 == True:
                        break
            except:
                IndexError
            if check1 == False:
                locationToStart = 3
                break

            # top right
            check1 = False
            try:
                for l in range(0,len(world)//10):
                    for i in range(len(world[0])//10*9,len(world[0])):
                        if world[l][i] in ["s","#",","]:
                            check1 = True
                            break
                        else:
                            pass
                    if check1 == True:
                        break
            except:
                IndexError
            if check1 == False:
                locationToStart = 4
                break

            print("Island is too big or has generated wrong, current code limitation cannot fix this (temporary)")
            break
        if locationToStart == 0:
            pass
        elif locationToStart in [1,2,3,4]:
            mapCleaner4(locationToStart)
            print("Cleaned up holes in island(s)!")
        else:
            pass
        
#------------------------- clean3 ------------------------------------------------#

    elif inpt == "clean3":
        tempCounter1 = 2
        while tempCounter1 > 0:
            tempCounter1 = 0
            for l in range(len(world)):
                for i in range(len(world[0])):
                    try:
                        if world[l][i] == "#" and world[l][i+1] == "#" and world[l][i-1] == "." and world[l][i+2] == "." or world[l][i] == "#" and world[l+1][i] == "#" and world[l-1][i] == "." and world[l+2][i] == ".":
                            print("cleaning...")
                            mapCleaner5()
                            tempCounter += 1
                            break
                    except:
                        IndexError

            for l in range(len(world)):
                for i in range(len(world[0])):
                    try:
                        if world[l][i] == "#" and world[l][i+1] == "#" and world[l][i+2] == "#" and world[l][i-1] == "." and world[l][i+3] == "." or world[l][i] == "#" and world[l+1][i] == "#" and world[l+2][i] == "#" and world[l-1][i] == "." and world[l+3][i] == ".":
                            print("cleaning...")
                            mapCleaner5()
                            tempCounter += 1
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
