import random # to be able to "spin" the wheel and get a random pocket

class Roulette:
    def __init__(self):
        # there are 38 pockets in a roulette wheel (0-36, 00, 0)
        self.pockets = [i for i in range(0, 37)]
        self.ball = None

    def spin(self):
        self.ball = random.choice(self.pockets)

        # return a String representation of the ball pocket number
        if self.ball == 37:
            ballString = "00"
        else: 
            ballString = str(self.ball)
        return ballString

    