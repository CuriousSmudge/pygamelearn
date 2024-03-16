# Notes
## Ignore CLS, no command exists
## Setup -> Gameplay Loop -> Result
## Do Setup First, Dummy Gameplay and Result Second, Gameplay Loop Final
## Test as you go!!!!
## Utilise descriptive names

# Starship Take-off
## Settup
import random

print('Starship Take-Off')

### Defining and Testing Variables
Gravity=random.randint(1,20)
Weight=random.randint(1,40)
#print(f"Gravity: {Gravity} , Weight: {Weight}")

RequiredForce=Gravity*Weight
#print(f"RequiredForce: {RequiredForce}")

print(f"Gravity: {Gravity}")

## Gameplay
Guesses=0

Guess=int(input('Enter Force: '))
while Guesses < 10 and Guess != RequiredForce:
    if Guess < RequiredForce:
        print('Too low')
    elif Guess > RequiredForce:
        print('Too high')
    print('Try Again')
    Guess=int(input('Enter Force: '))
    Guesses = Guesses+1

## Result
if Guess == RequiredForce :
    print('Good Take-Off')
else :
    print("You Failed")
    print('The Aliens Got You')