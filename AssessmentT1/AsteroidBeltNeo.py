# Asteroid Belt Neo v2 pt.2 the sequel the prequel the second coming
## By Ahseley de Weerdt
import pygame as pg
import random as rd
import time as tm
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

explosion = pg.image.load("AssessmentT1\\Assets\\explosion.png")
largeExplosion = pg.transform.smoothscale(explosion, (1000,1000))
medExplosion = pg.transform.smoothscale(explosion, (250,250))
smallExplosion = pg.transform.smoothscale(explosion, (125, 125))

spaceShipY = 800
missileY = 650
missileFired = False
score = 0
counter = 0
tempCounter = 0

# Game Setup
FPS = 60
fpsClock = pg.time.Clock()
WINDOW_WIDTH = 360
WINDOW_HEIGHT = 780
 
WINDOWX_CENTRE = WINDOW_WIDTH / 2
WINDOWY_CENTRE = WINDOW_HEIGHT / 2

WINDOW = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Asteroid Belt Neo Ultra X Super + The Sequel The Prequel The Second Coming 2')

# rotatedImage, rotatedImageRect = rotate(image, angle, (coordsx, coordsy))

def fireMissile(size: int):
  global missileY, missile, missileFired, missile_fire_time, asteroidSize
  scaleFactor = size / 5
  neoMissile = pg.transform.smoothscale(missile, (missile.get_width() * scaleFactor, missile.get_height() * scaleFactor))
  if missileY >= 75:
    missileY -= 10
    WINDOW.blit(neoMissile, (WINDOWX_CENTRE - neoMissile.get_width() / 2, missileY))
  else: 
    missileY = 650
    missileFired = False
    end()

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
      WINDOW.blit(medAsteroid, (WINDOWX_CENTRE - 100, 75))
    case "large":
      rotate(largeAsteroid, 180, (500, 500))
      WINDOW.blit(largeAsteroid, (WINDOWX_CENTRE - 500, -600))
    case _:
      print("That's not an asteroid size stupid!!")
  pass

def drawExplosion(size: str):
  match size:
    case "small":
      WINDOW.blit(smallExplosion, (WINDOWX_CENTRE - 66, 75))

    case "med":
      WINDOW.blit(medExplosion, (WINDOWX_CENTRE - 125, 50))

    case "large":
      WINDOW.blit(largeExplosion, (WINDOWX_CENTRE - 500, -300))

  if event.type == pg.QUIT :
    pg.quit()
    sys.exit()
  pg.display.update()
  tm.sleep(2)

# my hear it s astero it beats for you
def stero():
  print("my heats a stero")
  print("it beats for you so listen close")
  print("woah/n"*100)

def end():
  global tempCounter, asteroidSize
  if tempCounter < 7:
    drawExplosion("small")
  elif tempCounter > 6 and tempCounter < 14:
    if tempCounter == asteroidSize:
      drawExplosion("med")
    elif tempCounter < asteroidSize:
      drawExplosion("small")
    elif tempCounter > asteroidSize:
      drawExplosion("med")
  elif tempCounter > 13:
    if tempCounter == asteroidSize:
      drawExplosion("large")
    if tempCounter != asteroidSize:
      drawExplosion("med")

# Initialising random number
asteroidSize = rd.randint(1, 21)

# Main Game Loop
while True :        
  # Render elements of the game
  WINDOW.fill(BACKGROUND)

  # Spaceship animation
  if spaceShipY >= 650:
    spaceShipY -= 1
  WINDOW.blit(spaceShip, (WINDOWX_CENTRE - 50, spaceShipY))

  # Gametime mwahahahaha
  # Generating random number
  if asteroidSize < 7:
    drawAsteroid("small")
  elif asteroidSize < 14:
    drawAsteroid("med")
  else:
    drawAsteroid("large")

  if missileFired:
    fireMissile(tempCounter)

  # New section: wait for spacebar press
  for event in pg.event.get():
    if event.type == pg.QUIT :
      pg.quit()
      sys.exit()
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_w:
        counter += 1
        print(f"Counter: {counter}")
      if event.key == pg.K_SPACE:
        tempCounter = counter
        missileFired = True
        fireMissile(tempCounter)
        if counter == 0:
          print(f"{counter} is literally 0.")
          counter = 0
          break
        elif counter < asteroidSize:
          print(f"{counter} isn't enough!!! Try Again!!!!")
          counter = 0
          break
        elif counter == asteroidSize:
          print(f"{counter} is just right! We did it!!!!!!!! Asteroid Destroyed!!!!!!!!!!!")
          counter = 0
          break
        elif counter > 0:
          print(f"{counter} is too much!! AAAAAAHHHHHH!!!!!")
          counter = 0
          break
  pg.display.update()
  fpsClock.tick(FPS)
main()