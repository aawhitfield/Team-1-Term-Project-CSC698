from roulette import Roulette
from screen import Screen

# create instances of the necessary classes
roulette = Roulette()
screen = Screen()

# display welcome message
screen.displayWelcome()

# display the user's options
screen.displayMenu()

# get the user's menu choice
choice = screen.getMenuChoice()

# loop until the user chooses to quit
while choice != "4":
    # display the user's current balance
    screen.displayBalance(100)
    
    # display the user's current bet
    screen.displayBet(0)
    print() # blank line
    
    # display the user's options
    screen.displayMenu()
    
    # get the user's menu choice
    choice = screen.getMenuChoice()

# spin the wheel and get the ball pocket number
pocket = roulette.spin()

# display the ball pocket number to the user
screen.displayBall(pocket)

