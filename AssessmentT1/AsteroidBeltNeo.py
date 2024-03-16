# Asteroid Belt Neo v2 pt.2 the sequel the prequel the second coming
## By Ahseley de Weerdt
import pygame as pg
import random as rd
import time as tm
import keyboard
import sys
pg.init()
 
# Variables
BACKGROUND = (0, 0, 0)

spaceShip = pg.image.load("AssessmentT1\\Assets\\Spaceship.png")
spaceShip = pg.transform.smoothscale(spaceShip, (100, 100))
missile = pg.image.load("AssessmentT1\\Assets\\missile.png")
missile = pg.transform.smoothscale(missile, (100, 100))

asteroid = pg.image.load("AssessmentT1\\Assets\\Asteroid.png")
largeAsteroid = pg.transform.smoothscale(asteroid, (1000, 1000))
medAsteroid = pg.transform.smoothscale(asteroid, (200, 200))
smallAsteroid = pg.transform.smoothscale(asteroid, (100, 100))

spaceShipY = 800
missileY = 650
missileFired = False
score = 0

# Game Setup
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 780
 
WINDOWX_CENTRE = WINDOW_WIDTH / 2
WINDOWY_CENTRE = WINDOW_HEIGHT / 2

WINDOW = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Asteroid Belt Neo Ultra X Super +')

# rotatedImage, rotatedImageRect = rotate(image, angle, (coordsx, coordsy))

def rotate(img: pg.Surface, angle: float, centerCords: tuple) -> pg.Surface:
  topleft = centerCords
  rotatedImg = pg.transform.rotate(img, -angle)
  newRect = rotatedImg.get_rect(center = img.get_rect(topleft=topleft).center)
  return rotatedImg, newRect

def drawAsteroid(size: str):
  match size:
    case "small":
      rotate(smallAsteroid, 180, (50, 50))
      WINDOW.blit(smallAsteroid, (WINDOWX_CENTRE - 50, 75))
    case "med":
      rotate(medAsteroid, 180, (100, 100))
      WINDOW.blit(medAsteroid, (WINDOWX_CENTRE - 100, 125))
    case "large":
      rotate(largeAsteroid, 180, (500, 500))
      WINDOW.blit(largeAsteroid, (WINDOWX_CENTRE - 500, -600))
    case _:
      print("That's not an asteroid size stupid!!")
  pass

# Main Game Loop
while True :
    # Get inputs
    for event in pg.event.get() :
      if event.type == pg.QUIT :
        pg.quit()
        sys.exit()
      #if event.type == pg.KEYDOWN :
        #if event.key == pg.K_w:
          #missileFired = True

    # Render elements of the game
    WINDOW.fill(BACKGROUND)

    # Spaceship animation
    if spaceShipY >= 650:
      spaceShipY -= 1
    WINDOW.blit(spaceShip, (WINDOWX_CENTRE - 50, spaceShipY))

    # Missile animation
    if missileFired:
      if missileY >= 75:
        missileY -= 10
      else:
        missileFired = False
        missileY = 650
      WINDOW.blit(missile, (WINDOWX_CENTRE - 50, missileY))

    # Gametime mwahahahaha
    for G in range (1,11):
      # Variable reset
      counter = 0
      # Generating random number
      asteroidSize = rd.randint(0, 21)
      
      if asteroidSize < 7:
        drawAsteroid("small")
      elif asteroidSize < 14:
        drawAsteroid("med")
      else:
        drawAsteroid("large")

        # New section: wait for spacebar press
      spacebar_pressed = False
      w_key_pressed = False
      while not spacebar_pressed:
        events = pg.event.get()
        for event in events:
          if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
              counter += 1
              print(f"Counter: {counter}")
            elif event.key == pg.K_SPACE:
              spacebar_pressed = True
              counter = 0  # Reset the counter

    pg.display.update()
    fpsClock.tick(FPS)

main()