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

    for x in Arr1:
        if x == N: # just before intersection
            if Arr2[x + 1] != ".": # Check if empty


        elif Arr1[x + 1] == Type:
            Arr1[x] == "."
            Arr1[x + 1] == Type
    return Arr1




print(Cycle(RedArr, BlueArr, "R"))