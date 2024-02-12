import time

# Variables
S=0



### Random Int Tester
#print(AsteroidPosX)
#print(AsteroidPosY)
#print(AsteroidStars)

# Game Start
print('Asteroid Belt')
for G in range(1,11):
    ## Getting Time for Random Int
    Time = time.time()
    Time = int(Time*1000000)
    AsteroidPosX = Time % 18+1
    AsteroidPosY = Time % 12+1
    AsteroidStars = Time % 9+1
    
    print(G)