# Variables
N = 3
systemSize = 1
Cycles = 3
RedArr = [0, 1, 1, 1, 0, 0, 1]
BlueArr = [1, 0, 1, 0, 0 ,0, 1]

# Cycle Loop
def traffic (N, systemSize, Cycles, RedArr, BlueArr):
    for i in range(Cycles):
        RedArr = Cycle(RedArr, BlueArr)
        BlueArr = Cycle(BlueArr, RedArr)

# Doing (ur mom doin doin ur mom) Simulation
def Cycle (Arr1, Arr2):
    return Arr1



traffic()