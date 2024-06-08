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
        print()

    # display the user's loss
    def displayLoss(self, loss):
        print("You have lost $" + str(loss) + ".")
        print() # blank line

    # display welcome message
    def displayWelcome(self):
        print("Welcome to Roulette!")
        print("You have $100 to start with.")
        print("Good luck!")
        print() # blank line

    # display the user's options
    def displayMenu(self):
        print("1. Bet on a number")
        print("2. Bet on a color")
        print("3. Bet on odd or even")
        print("4. Quit")
        print() # blank line

    # get the user's menu choice
    def getMenuChoice(self):
        choice = input("Enter your choice: ")
        return choice
    
    # get the user's bet amount
    def getBetAmount(self):
        bet = int(input("Enter your bet amount: "))
        return bet

    # get the user's number bet
    def getNumberBet(self):
        number = input("Enter your number bet (0-36, 00): ")
        return number
    
    # tell the user if they have won or lost
    def displayOutcome(self, outcome):
        if outcome == True:
            print("Congratulations! You have won!")
        else:
            print("Sorry, you have lost.")
        print() # blank line
