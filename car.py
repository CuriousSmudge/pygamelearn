import copy
# Variables
N = 3
systemSize = 3
Cycles = 5
RedArr = [".", "R", "R", "R", "." ,".", "R"]
BlueArr = ["B", ".", "B", ".", ".", ".", "B"]
altRedArr = ['R', 'R', 'R', '.', 'R', '.', '.']

# Cycle Loop
def traffic (N, systemSize, Cycles, RedArr, BlueArr):
    for i in range(Cycles):
        RedArr = Cycle(RedArr, BlueArr, "R")
        BlueArr = Cycle(BlueArr, RedArr, "B")
    print("FINISHED!!!")
    print(RedArr)
    print(BlueArr)


def Cycle (Arr1, Arr2, Type):
    x = -1
    startArr1 = copy.copy(Arr1)
    print("This should not appear twice")
    while x < (len(Arr1) - 1):
        x = x + 1
        print("Loop num: " + str(x))
        print("Start Arr: " + str(startArr1))
        #print(Arr1)

        if Arr1[x] != Type: # I.e traffix empty in that spot
            print("empty")
            continue
        elif x >= len(Arr1) - 1: # At end of road gonna wrap round
            print("gonna wrap")
            if startArr1[0] == ".":
                print("Start Arr: " + str(startArr1))
                Arr1[x] = "."
                Arr1[0] = Type
                continue
            else: ## spot occupoed
                print("Wrap around occupied")
                continue

         # This is the standard case
        if x == N - 1: # just before intersection
            print("standard case Before intersection")
            if Arr2[x+1] == "." and startArr1[x+1] == ".": # Check if empty
                print("Went to inter section")
                Arr1[x] = "."
                Arr1[x + 1] = Type
                x = x + 1
                continue
            print("Did not intersection")
        if startArr1[x + 1] == Type: # if occupied
            print("Occupied")
            #Arr1[x] = "."
            #xPlus = x + 1
            #Arr1[xPlus] = Type
            continue
        elif startArr1[x + 1] == ".":
            print("standard march")
            print(startArr1)
            Arr1[x] = "."
            Arr1[x + 1] = Type
            print("about to add")
            #print(x)
            x = x + 1 #Dont iterate over same car twice
            #print(x)
            continue

        print(Arr1)
        print("WAH NOTHING WORKED IF YOU SEE THIS")

    return Arr1


# Doing (ur mom doin doin ur mom) Simulation

def Cycle2 (Arr1, Arr2, Type):
    x = -1
    while x < (len(Arr1) - 1):
        x = x + 1
    #for x in range(0, len(Arr1), 1):
        print(x)
        print(Arr1)
        if Arr1[x] != Type: # I.e traffix empty in that spot
            print("empty")
            continue
        elif x >= len(Arr1) - 1: # At end of road gonna wrap round
            print("gonna wrap")
            if Arr1[0] == ".":
                Arr1[x] = "."
                Arr1[0] = Type
                continue
            else: ## spot occupoed
                continue

        # This is the standard case
        if x == N - 1: # just before intersection
            print("standard case Before intersection")
            if Arr2[x+1] == "." and Arr1[x+1] == ".": # Check if empty
                print("Went to inter section")
                Arr1[x] = "."
                Arr1[x + 1] = Type
                x = x + 1
                continue
            print("Did not intersection")
        if Arr1[x + 1] == Type: # if occupied
            print("Occupied")
            #Arr1[x] = "."
            #xPlus = x + 1
            #Arr1[xPlus] = Type
            continue
        elif Arr1[x + 1] == ".":
            print("standard march")
            Arr1[x] = "."
            Arr1[x + 1] = Type
            print("about to add")
            print(x)
            x = x + 1 #Dont iterate over same car twice
            print(x)
            continue

        print(Arr1)
        print("WAH")

    return Arr1



#print(len(RedArr))

#print(Cycle(RedArr, BlueArr, "R"))
#print(Cycle(BlueArr, altRedArr, "B"))

print(traffic(N, systemSize, Cycles, RedArr, BlueArr))