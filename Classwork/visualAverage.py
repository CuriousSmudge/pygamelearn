import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
BARCOLOUR = (50, 50 , 200)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

def getNewValue () :
            print ('') # Just to space things out
            newValue = int(input('Please enter the next number : '))
            return newValue 

# Render the values as bars on the screen
def renderValues (valuesArray) :
    barWidth = int(WINDOW_WIDTH / len(valuesArray))
    newArray = valuesArray.copy()
    newArray.sort()
    largestValue = newArray[-1]
    
    heightUnit = int(WINDOW_HEIGHT / largestValue)
    
    counter = 0
    
    while counter < len(valuesArray) :
        barX = counter * barWidth
        barHeight = heightUnit * valuesArray[counter]
        barY = WINDOW_HEIGHT - barHeight
        bar = pygame.Rect(barX, barY, barWidth, barHeight)
        pygame.draw.rect(WINDOW, BARCOLOUR, bar)
        counter = counter + 1
    return

 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

# The main function that controls the game
def main () :
    looping = True
    values = [] # initialise a blank array
 
    # The main game loop
    while looping :
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
    
        # Processing
        # This section will be built out later
        nextValue = getNewValue()
        values.append(nextValue)
        print (values)
 
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        renderValues(values)
        pygame.display.update()
        fpsClock.tick(FPS)
        
main()

