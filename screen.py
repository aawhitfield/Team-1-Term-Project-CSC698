from color import Color # an enum class for color (red or black)

# contains the methods to display information to the user via the command line "screen"

class Screen:
    def __init__(self):
        pass

    # display the ball pocket number to the user
    def displayBall(self, ball, color):
        print(f"The ball landed in pocket {ball} ({color.name.lower()}).")

    # display the user's current balance
    def displayBalance(self, balance):
        print(f"Your current balance is ${balance}.")

    # display the user's current bet
    def displayBet(self, bet):
        print(f"You have bet ${bet}.")

    # display the user's winnings
    def displayWinnings(self, winnings, bet):
        print(f"You have won ${winnings}. (Plus your bet of ${bet}.)")
        print()

    # display the user's loss
    def displayLoss(self, loss):
        print(f"You have lost ${loss}.")
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
        while True: # loop in case the user continues to enter invalid input
            try:
                bet = int(input("Enter your bet amount: ")) # convert the input to an integer so we can do math with it
                if bet > 0: # you can't bet a negative amount of money -- would be nice if you could in real life though 😜
                    return bet
                else:
                    print("Bet amount must be a positive number. Please try again.")
            except ValueError: 
                print("Invalid input. Please enter a number.")

    # get the user's number bet
    def getNumberBet(self):
        number = input("Enter your number bet (0-36, 00): ")
        if number == "00":
            return 37
        return int(number)
    
    # get the user's color bet
    def getColorBet(self):
        color_string = input("Enter your color bet (red, black, green): ").lower().strip() # convert to lowercase and remove leading/trailing whitespace
        
        # validate the color input
        while color_string not in ["red", "black", "green"]:
            color_string = input("Invalid color. Please enter red, black, or green: ").lower().strip()
        
        # convert the color string to a Color enum
        if color_string == "red":
            color = Color.RED
        elif color_string == "black":
            color = Color.BLACK
        else:
            color = Color.GREEN
        return color
    
    # get the user's odd or even bet
    def getOddEvenBet(self):
        odd_even = input("Enter your odd or even bet: ").lower().strip() # convert to lowercase and remove leading/trailing whitespace
        
        # validate the odd/even input
        while odd_even not in ["odd", "even"]: # only two options -- the array of options is just a nice way to not have to write compound conditions
            odd_even = input("Invalid input. Please enter odd or even: ").lower().strip() # re-prompt the user repeatedly until they enter a valid input
        return odd_even
    
    # tell the user if they have won or lost
    def displayOutcome(self, outcome):
        if outcome:
            print("Congratulations! You have won!")
        else:
            print("Sorry, you have lost.")
        print() # blank line
