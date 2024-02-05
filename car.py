# Variables
N = 3
systemSize = 1
Cycles = 3
RedArr = [".", "R", "R", "R", "." ,".", "R"]
BlueArr = ["B", ".", "B", ".", ".", ".", "B"]

# Cycle Loop
def traffic (N, systemSize, Cycles, RedArr, BlueArr):
    for i in range(Cycles):
        RedArr = Cycle(RedArr, BlueArr)
        BlueArr = Cycle(BlueArr, RedArr)

# Doing (ur mom doin doin ur mom) Simulation
def Cycle (Arr1, Arr2):
    return Arr1



traffic()