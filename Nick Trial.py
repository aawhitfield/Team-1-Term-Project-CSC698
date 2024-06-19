import random
import pygame

class RouletteBetting:
    def __init__(self):
        self.money = 1000  # Starting money
        self.colors = ["red", "black"]
        self.numbers = list(range(0, 37))  # Roulette numbers (0-36)
        self.bet_amount = 0
        self.bet_type = None  # "color", "number", "pair", "trio", "corner", "sixline", "dozen"
        self.bet_choice = None

        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

    def place_bet(self):
        """
        Prompts the user to place a bet and handles input validation.
        """
        # Get bet type from user
        bet_type = input("Place your bet on color, number, pair, trio, corner, sixline, or dozen? ").lower()
        while bet_type not in ["color", "number", "pair", "trio", "corner", "sixline", "dozen"]:
            bet_type = input("Invalid input. Please enter 'color', 'number', 'pair', 'trio', 'corner', 'sixline', or 'dozen': ").lower()
        self.bet_type = bet_type

        # Get bet choice from user
        if bet_type == "color":
            bet_choice = input("Choose 'red' or 'black': ").lower()
            while bet_choice not in ["red", "black"]:
                bet_choice = input("Invalid input. Please enter 'red' or 'black': ").lower()
            self.bet_choice = bet_choice
        elif bet_type == "number":
            bet_choice = input("Choose a number between 0 and 36: ")
            while not bet_choice.isdigit() or int(bet_choice) not in self.numbers:
                bet_choice = input("Invalid input. Please enter a number between 0 and 36: ")
            self.bet_choice = int(bet_choice)
        elif bet_type == "pair":
            bet_choice = input("Choose a pair of numbers (e.g., '1,2'): ")
            pair = [int(num) for num in bet_choice.split(",")]
            while len(pair) != 2 or any(num not in self.numbers for num in pair):
                bet_choice = input("Invalid input. Please enter a valid pair of numbers (e.g., '1,2'): ")
                pair = [int(num) for num in bet_choice.split(",")]
            self.bet_choice = tuple(pair)
        elif bet_type == "trio":
            bet_choice = input("Choose a trio of numbers (e.g., '1,2,3'): ")
            trio = [int(num) for num in bet_choice.split(",")]
            while len(trio) != 3 or any(num not in self.numbers for num in trio):
                bet_choice = input("Invalid input. Please enter a valid trio of numbers (e.g., '1,2,3'): ")
                trio = [int(num) for num in bet_choice.split(",")]
            self.bet_choice = tuple(trio)
        elif bet_type == "corner":
            bet_choice = input("Choose a corner of four numbers (e.g., '1,2,4,5'): ")
            corner = [int(num) for num in bet_choice.split(",")]
            while len(corner) != 4 or any(num not in self.numbers for num in corner):
                bet_choice = input("Invalid input. Please enter a valid corner of four numbers (e.g., '1,2,4,5'): ")
                corner = [int(num) for num in bet_choice.split(",")]
            self.bet_choice = tuple(corner)
        elif bet_type == "sixline":
            bet_choice = input("Choose a six-line of six numbers (e.g., '1,2,3,4,5,6'): ")
            sixline = [int(num) for num in bet_choice.split(",")]
            while len(sixline) != 6 or any(num not in self.numbers for num in sixline):
                bet_choice = input("Invalid input. Please enter a valid six-line of six numbers (e.g., '1,2,3,4,5,6'): ")
                sixline = [int(num) for num in bet_choice.split(",")]
            self.bet_choice = tuple(sixline)
        elif bet_type == "dozen":
            bet_choice = input("Choose a dozen (1st, 2nd, or 3rd): ").lower()
            while bet_choice not in ["1st", "2nd", "3rd"]:
                bet_choice = input("Invalid input. Please enter '1st', '2nd', or '3rd': ").lower()
            self.bet_choice = bet_choice

        # Get bet amount from user
        bet_amount = input("Enter your bet amount: ")
        while not bet_amount.isdigit() or int(bet_amount) > self.money:
            bet_amount = input(f"Invalid input or insufficient funds. Please enter a valid amount (max {self.money}): ")
        self.bet_amount = int(bet_amount)

    def spin_roulette(self):
        """
        Simulates the roulette spin and determines the winning color and number.
        """
        winning_number = random.choice(self.numbers)
        winning_color = "red" if winning_number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36] else "black"
        return winning_number, winning_color

    def check_result(self, winning_number, winning_color):
        """
        Checks the result of the bet and updates the player's money.
        """
        if self.bet_type == "color":
            if self.bet_choice == winning_color:
                self.money += self.bet_amount
                print(f"You won! The winning color is {winning_color}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning color is {winning_color}. Your new balance is {self.money}.")
        elif self.bet_type == "number":
            if self.bet_choice == winning_number:
                self.money += self.bet_amount * 35  # Payout for winning number bet is 35:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")
        elif self.bet_type == "pair":
            if winning_number in self.bet_choice:
                self.money += self.bet_amount * 17  # Payout for winning pair bet is 17:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")
        elif self.bet_type == "trio":
            if winning_number in self.bet_choice:
                self.money += self.bet_amount * 11  # Payout for winning trio bet is 11:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")
        elif self.bet_type == "corner":
            if winning_number in self.bet_choice:
                self.money += self.bet_amount * 8  # Payout for winning corner bet is 8:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")
        elif self.bet_type == "sixline":
            if winning_number in self.bet_choice:
                self.money += self.bet_amount * 5  # Payout for winning six-line bet is 5:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")
        elif self.bet_type == "dozen":
            if self.bet_choice == "1st" and winning_number in range(1, 13):
                self.money += self.bet_amount * 2  # Payout for winning dozen bet is 2:1
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            elif self.bet_choice == "2nd" and winning_number in range(13, 25):
                self.money += self.bet_amount * 2
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            elif self.bet_choice == "3rd" and winning_number in range(25, 37):
                self.money += self.bet_amount * 2
                print(f"You won! The winning number is {winning_number}. Your new balance is {self.money}.")
            else:
                self.money -= self.bet_amount
                print(f"You lost. The winning number is {winning_number}. Your new balance is {self.money}.")

    def play_game(self):
        """
        Main game loop.
        """
        while self.money > 0:
            self.place_bet()
            winning_number, winning_color = self.spin_roulette()
            self.check_result(winning_number, winning_color)
            play_again = input("Play again? (y/n) ").lower()
            if play_again != "y":
                break
        print("Game over. Thanks for playing!")

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1000
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Roulette Betting Game")

# Create an instance of the RouletteBetting class
game = RouletteBetting()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the window
    window.fill((39, 119, 20))

    # Draw game elements
    money_text = game.font.render(f"Money: ${game.money}", True, (255, 255, 255))
    window.blit(money_text, (800, 750))  # Display money text at (10, 10)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()