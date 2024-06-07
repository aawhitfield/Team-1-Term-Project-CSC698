from roulette import Roulette
from screen import Screen

# create instances of the necessary classes
roulette = Roulette()
screen = Screen()

# spin the wheel and get the ball pocket number
pocket = roulette.spin()

# display the ball pocket number to the user
screen.displayBall(pocket)

