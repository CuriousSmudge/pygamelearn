# Variables
N = 3
systemSize = 1
Cycles = 3
RedArr = [".", "R", "R", "R", "." ,".", "R"]
BlueArr = ["B", ".", "B", ".", ".", ".", "B"]

# Cycle Loop
def traffic (N, systemSize, Cycles, RedArr, BlueArr):
    for i in range(Cycles):
        RedArr = Cycle(RedArr, BlueArr, "R")
        BlueArr = Cycle(BlueArr, RedArr, "B")

# Doing (ur mom doin doin ur mom) Simulation
def Cycle (Arr1, Arr2, Type):
    for x in range(0, len(Arr1), 1):
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
                print("Went to intersection")
                Arr1[x] = "."
                Arr1[x + 1] = Type
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
            x = x + 3 #Dont iterate over same car twice
            print(x)
            continue

        print(Arr1)
        print("WAH")

    return Arr1



#print(len(RedArr))

print(Cycle(RedArr, BlueArr, "R"))