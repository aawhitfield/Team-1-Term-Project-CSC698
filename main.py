from roulette import Roulette
from screen import Screen

# create instances of the necessary classes
roulette = Roulette()
screen = Screen()

# create a variable to keep track of the user's money
balance = 100

# display welcome message
screen.displayWelcome()

# display the user's options
screen.displayMenu()

# get the user's menu choice
choice = screen.getMenuChoice()

# loop until the user chooses to quit
while choice != "4":
    # display the user's current balance
    screen.displayBalance(balance)
    
    # get the user's bet amount
    bet = screen.getBetAmount()

    if choice == "1": # bet on a number
        # get the user's number bet
        number = screen.getNumberBet()

        # spin the wheel
        ball = roulette.spin()

        # display the ball pocket number to the user
        screen.displayBall(ball)
        print()

        # determine if the user has won
        if roulette.isWinnerByNumber(number):
            # calculate the user's winnings
            winnings = roulette.calculateWinnings(bet)

            # update the user's balance
            balance += bet # get the bet back
            balance += winnings

            # display the user's winnings
            screen.displayWinnings(bet, winnings)
            screen.displayBalance(balance)
        else:
            # display the user's loss
            screen.displayLoss(bet)
            screen.displayBalance(balance)

            # update the user's balance
            balance -= bet
    
    # display the user's options
    screen.displayMenu()
    
    # get the user's menu choice
    choice = screen.getMenuChoice()

