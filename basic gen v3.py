import random,time,os; clear = lambda: os.system('cls')
from PIL import Image

informationForUse = "   -=:List of commands after you're done with the inputs:=-\
\n\ntype 'info' to display this list of information\
\n-type 'redo' to reopen this exe\
\n-type 'gen1' to generate green land\
\n-Type 'poof' to clear array\
\n-type 'image' to create and store image (replaced if program restarted)\
\n-type 'image2' to create and store image.v2 (replaced if program restarted)\
\n-type 'map' to display array\
\n-type 'clean1' to clean world of one pixel holes\
\n-type 'clean2' to clean world of 2x2 to pixel holes\
\n-type 'clean3' to clean world of random 1 pixel wide spikes (advised to be used after 'clean1')\
\n-type 'save' to save copy as number e.g. 'save1' (current session only)\
\n-type 'load.(number)' to load a saved copy (current session only)\n\n\n"

while True:
    print(informationForUse)
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

def mapCleaner3():
    for l in range(len(world)):
        for i in range(len(world[0])):
            if world[l][i] == "#":
                try:
                    if world[l][i] == "#" and world[l-1][i] == "#" and world[l+1][i] != "#" and world[l][i-1] == "." and world[l-1][i-1] == "." and world[l][i+1] == "." and world[l-1][i+1] == "."\
                       or world[l][i] == "#" and world[l][i+1] == "#" and world[l][i-1] != "#" and world[l-1][i] == "." and world[l-1][i+1] == "." and world[l+1][i] == "." and world[l+1][i+1] == "."\
                       or world[l][i] == "#" and world[l+1][i] == "#" and world[l-1][i] != "#" and world[l][i-1] == "." and world[l+1][i-1] == "." and world[l][i+1] == "." and world[l+1][i+1] == "."\
                       or world[l][i] == "#" and world[l][i-1] == "#" and world[l][i+1] != "#" and world[l-1][i] == "." and world[l-1][i-1] == "." and world[l+1][i] == "." and world[l+1][i-1] == ".":# up,right,down,left
                           world[l][i] = "."
                except:
                    IndexError
                      





            
while True:
    global toGen
    inpt = input("</: ")
    if inpt == "info":
        print(informationForUse)
    elif inpt == "redo":# redo
        os.startfile('basic gen v3.py')
        sys.exit()

    elif inpt == "gen1":# gen1
        clear()
        gen1()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    assetCounter += 1
        print("\nAssets generated this runtime:",toGen,"\nCurrent asset count:",assetCounter)
        assetCounter = 0
        errorCounter = 0

    elif inpt == "poof":# poof
        assetCounter = 0
        clear()
        for i in range(len(world)):
            for l in range(len(world[0])):
                if world[i][l] == "#":
                    world[i][l] = "."

    elif inpt == "image":# image
        img = Image.new('RGB',(len(world[0]),len(world)),(25,25,140))
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    img.putpixel((i,l),(0,120,0))
        img.save("test{}.png".format(numericalOrder))
        img.show()
        numericalOrder += 1

    elif inpt == "image2":# using assets for image
        img = Image.new('RGB',(len(world[0])*2,len(world)*2),(25,25,140))
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    img.putpixel((i+1,l),(0,120,0))# top left - green
                    img.putpixel((i,l+1),(0,60,0))# top right - red
                    img.putpixel((i,l+1),(0,60,0))# bottom left - red
                    img.putpixel((i+1,l+1),(0,120,0))# bottom right - green
                
        img.save("test{}.png".format(numericalOrder))
        img.show()
        numericalOrder += 1
        

    elif inpt == "map":# map
        showMap()
    elif inpt[:3] == "set":# sets object at location
        print("test")
        

###########################################################################################################################################################################

    elif inpt == "clean1":# clean1
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

    elif inpt == "clean3":
        for l in range(len(world)):
            for i in range(len(world[0])):
                if world[l][i] == "#":
                    try:
                        if world[l][i] == "#" and world[l-1][i] == "#" and world[l+1][i] != "#" and world[l][i-1] == "." and world[l-1][i-1] == "." and world[l][i+1] == "." and world[l-1][i+1] == "."\
                           or world[l][i] == "#" and world[l][i+1] == "#" and world[l][i-1] != "#" and world[l-1][i] == "." and world[l-1][i+1] == "." and world[l+1][i] == "." and world[l+1][i+1] == "."\
                           or world[l][i] == "#" and world[l+1][i] == "#" and world[l-1][i] != "#" and world[l][i-1] == "." and world[l+1][i-1] == "." and world[l][i+1] == "." and world[l+1][i+1] == "."\
                           or world[l][i] == "#" and world[l][i-1] == "#" and world[l][i+1] != "#" and world[l-1][i] == "." and world[l-1][i-1] == "." and world[l+1][i] == "." and world[l+1][i-1] == ".":# up,right,down,left
                               print("cleaning...")
                               mapCleaner3()
                               break
                    except:
                        IndexError



###########################################################################################################################################################################



    elif inpt == "save":# save
        i = 0
        while True:
            if f'save{i}' not in globals():
                break
            else:
                i += 1
        exec(f'save{i} = list(map(list,world))',globals())

    elif inpt[:4] == "load":# load
        try:
            int(inpt.split(".")[1])
            if f'save{int(inpt.split(".")[1])}' in globals():
                exec(f'world = list(map(list,save{int(inpt.split(".")[1])}))')
        except:
            ValueError
            pass        
    else:
        clear()
        #showMap()
