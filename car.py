N = 3
systemSize = 1
Cycles = 3

RedArr = [0, 1, 1, 1, 0 ,0, 1]
BlueArr = [1, 0, 1, 0, 0 ,0, 1]

def traffic (N, systemSize, Cycles, RedArr, BlueArr):
    for i in range(Cycles):
        RedArr = redCycle(RedArr, BlueArr)
        BlueArr = blueCycle(RedArr, BlueArr)


def redCycle (RedArr, BlueArr):
    return RedArr


def blueCycle (RedArr, BlueArr):
    return BlueArr

traffic()