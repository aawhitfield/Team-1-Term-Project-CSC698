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
    
    # get the user's bet amount
    bet = screen.getBetAmount()

    if choice == "1":
        # get the user's number bet
        number = screen.getNumberBet()

        # spin the wheel
        ball = roulette.spin()

        # display the ball pocket number to the user
        screen.displayBall(ball)
        print()

        # determine if the user has won
        if roulette.isWinnerByNumber(number):
            # display the user's winnings
            screen.displayWinnings(bet)
        else:
            # display the user's loss
            screen.displayLoss(bet)
    
    # display the user's options
    screen.displayMenu()
    
    # get the user's menu choice
    choice = screen.getMenuChoice()

