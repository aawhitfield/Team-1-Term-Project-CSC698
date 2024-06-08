from roulette import Roulette
from screen import Screen
from color import Color # an enum class for color (red or black)

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

# loop until the user chooses to quit or runs out of money
while choice != "4" and balance > 0:
    # display the user's current balance
    screen.displayBalance(balance)
    
    # get the user's bet amount
    bet = screen.getBetAmount()

# ~~~~~~~~~~~~~~~~ CHOICE  1 ~~~~~~~~~~~~~~~~~~~~~~~ Bet on a number
    if choice == "1": # bet on a number
        # get the user's number bet
        number = screen.getNumberBet()

        # spin the wheel
        ball, color = roulette.spin()

        # display the ball pocket number to the user
        screen.displayBall(ball, color)
        print()

        # determine if the user has won
        if roulette.isWinnerByNumber(number):
            # calculate the user's winnings
            # the payout ratio for betting on a number is 35:1
            payout_ratio = 35
            winnings = roulette.calculateWinnings(bet, payout_ratio)

            # update the user's balance
            balance += bet  # get the bet back
            balance += winnings

            # display the user's winnings
            screen.displayWinnings(winnings, bet)
            screen.displayBalance(balance)
        else:
            # display the user's loss
            screen.displayLoss(bet)
            balance -= bet
            screen.displayBalance(balance)

# ~~~~~~~~~~~~~~~~ CHOICE  2 ~~~~~~~~~~~~~~~~~~~~~~~ Bet on a color
    elif choice == "2": # bet on a color
        # get the user's color bet
        color = screen.getColorBet()

        # spin the wheel
        ball, result_color = roulette.spin()

        # display the ball pocket number to the user
        screen.displayBall(ball, result_color)
        print()

        # determine if the user has won
        if roulette.isWinnerByColor(color):
            # because there are so few green pockets, the payout ratio for betting on green is 35:1
            if color == Color.GREEN:
                payout_ratio = 35
            # but because there are an equal number of red and black pockets, the payout 1ratio for betting on red or black is 1:1
            else:
                payout_ratio = 1
            # calculate the user's winnings
            winnings = roulette.calculateWinnings(bet, payout_ratio)

            # update the user's balance
            balance += bet  # get the bet back
            balance += winnings

            # display the user's winnings
            screen.displayWinnings(winnings, bet)
            screen.displayBalance(balance)
        else:
            # display the user's loss
            screen.displayLoss(bet)
            balance -= bet
            screen.displayBalance(balance)

# ~~~~~~~~~~~~~~~~ CHOICE  3 ~~~~~~~~~~~~~~~~~~~~~~~ Bet on odd or even
    elif choice == "3":
        # get the user's odd or even bet
        odd_or_even = screen.getOddEvenBet()

        # spin the wheel
        ball, color = roulette.spin()

        # display the ball pocket number to the user
        screen.displayBall(ball, color)
        print()

        # determine if the user has won
        if roulette.isWinnerByOddEven(odd_or_even):
            # the payout ratio for betting on odd or even is 1:1
            payout_ratio = 1
            # calculate the user's winnings
            winnings = roulette.calculateWinnings(bet, payout_ratio)

            # update the user's balance
            balance += bet
            balance += winnings

            # display the user's winnings
            screen.displayWinnings(winnings, bet)
            screen.displayBalance(balance)

        else:
            # display the user's loss
            screen.displayLoss(bet)
            balance -= bet
            screen.displayBalance(balance)

    # display the user's options
    screen.displayMenu()
    
    # get the user's menu choice
    choice = screen.getMenuChoice()
