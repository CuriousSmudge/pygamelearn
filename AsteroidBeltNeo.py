# Asteroid Belt Neo v2 pt.2 the sequel the prequel the second coming
## By Ahseley de Weerdt

import pygame, time, keyboard

# Variables
S=0
I=1
Q=0

### Random Int Tester
#print(AsteroidPosX)
#print(AsteroidPosY)
#print(AsteroidStars)

def increment_counter(e):
    global counter
    counter += 1

keyboard.on_press_key('w', increment_counter)

# Game Start
print('Asteroid Belt')
for G in range(1,11):
    ## Getting Time for Random Int
    Time = time.time()
    Time = int(Time*1000000)
    AsteroidPosX = Time % 18+1
    AsteroidPosY = Time % 12+1
    AsteroidStars = Time % 9+1
    counter = 0
    Score = 0

    # Round Start
    print('Round',G)
    for i in range(I, AsteroidPosY):
        print("")
    for i in range(I, AsteroidStars):
        if I==1 and I==4 and I==7:
            print('*');
        else:
            print()
            print("".ljust(AsteroidStars))
            print('*');
        ## Keyboard Input - Destroying the Asteroid
        start_time = time.time()
        while time.time() - start_time < 5:
            pass
        print(counter)
        if counter == 0:
            print('Crashed Into Asteroid')
            counter = 0
            break
        elif counter == AsteroidStars:
            print('You Destroyed It!')
            Score=Score+1
            counter = 0
            break
        elif counter < AsteroidStars and counter != 0:
            print('Not Strong Enough')
            counter = 0
        elif counter > AsteroidStars:
            print('Too Strong!')
            counter = 0
print('You Hit' + S + 'Out of 10')