import random # to be able to "spin" the wheel and get a random pocket
from color import Color # to be able to get the color of the pocket

# contains all the methods and attributes needed to simulate a roulette wheel and ball
class Roulette:
    def __init__(self):
        # there are 38 pockets in a roulette wheel (0-36, 00)
        # in Python, the upper bound of a range is exclusive, so we need to go up to 38 to include 37
        self.pockets = [i for i in range(0, 38)] # Include 0-36 and 37 for '00' 
        self.colors = self.assign_colors()
        self.ball = None
        self.balance = 100

    def assign_colors(self):
        # Assign colors to pockets
        colors = {}
        for i in range(1, 37):
            if i % 2 == 0:
                colors[i] = Color.BLACK # Even numbers are black
            else:
                colors[i] = Color.RED  # Odd numbers are red
        colors[0] = Color.GREEN  # Assigning green to zero
        colors[37] = Color.GREEN # Assigning green to double zero (37 will be used to represent 00)
        return colors

    def spin(self):
        self.ball = random.choice(self.pockets)
        color = self.colors.get(self.ball, Color.GREEN)  # Default color if not found

        # return a tuple with String representation of the ball pocket number and its color
        if self.ball == 37:
            ballString = "00"
        else: 
            ballString = str(self.ball)
        return ballString, color
    
    # determine if the pocket number is the same as the user's number bet
    def isWinnerByNumber(self, number):
        return self.ball == number

    def isWinnerByColor(self, color):
        return self.colors[self.ball] == color
    
    def isWinnerByOddEven(self, odd_or_even):
        if self.ball == 0 or self.ball == 37:
            return False  # 0 and 00 are neither odd nor even in roulette
        if odd_or_even == "odd":
            return self.ball % 2 != 0 # standard CS way to check for odd numbers - if the number divided by 2 has a remainder, it's odd
        elif odd_or_even == "even":
            return self.ball % 2 == 0 # if the number is divisible by 2, it's even
        
    # calculate the amount of money the user has won
    def calculateWinnings(self, bet, payout_ratio):
        return bet * payout_ratio
