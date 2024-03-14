import pygame, sys, time, keyboard
from pygame.locals import *
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 780
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Purple')

# Variables
yCounter=1

def increment_counter(e):
    global counter
    counter += 1

keyboard.on_press_key('w', increment_counter)

# Create a custom event for the timer
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 5000)  # 5000 milliseconds = 5 seconds

while True:
    print('Asteroid Belt')
    for G in range(1,11):
        ## Getting Time for Random Int
        Time = time.time()
        Time = int(Time*1000000)
        AsteroidPosY = Time % 12+1
        AsteroidStars = Time % 9+1
        counter = 0
        Score = 0
        # Round Start
        print('Round',G)
        for i in range(yCounter, AsteroidPosY):
             print("")
        for i in range(yCounter, AsteroidStars):
             if yCounter==1 and yCounter==4 and yCounter==7:
                print('*');
             else:
                print()
                print("".ljust(AsteroidStars))
                print('*');
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            elif event.type == TIMEREVENT:
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
    WINDOW.fill(BACKGROUND)
    pygame.display.update()
    fpsClock.tick(FPS)   
    # Game Start
    

    
    print(f'You Hit {Score} Out of 10')