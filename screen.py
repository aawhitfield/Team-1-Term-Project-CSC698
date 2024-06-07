# contains the methods to display information to the user via the command line "screen"

class Screen:
    def __init__(self):
        pass

    # display the ball pocket number to the user
    def displayBall(self, ball):
        print("The ball landed in pocket " + ball + ".")

    # display the user's current balance
    def displayBalance(self, balance):
        print("Your current balance is $" + str(balance) + ".")

    # display the user's current bet
    def displayBet(self, bet):
        print("You have bet $" + str(bet) + ".")

    # display the user's winnings
    def displayWinnings(self, winnings):
        print("You have won $" + str(winnings) + ".")

    # display the user's loss
    def displayLoss(self, loss):
        print("You have lost $" + str(loss) + ".")
