import pygame
import sys
import time
from color import Color

class Outside:
    """Class to Handle Outside Bets"""

    def __init__(self, game_screen):
        self.screen = game_screen.screen
        self.roulette = game_screen.roulette
        self.font = game_screen.font
        self.background_color = game_screen.background_color
        self.accent_color = game_screen.accent_color
        self.result_color = game_screen.result_color
        self.clock = game_screen.clock
        self.spin_wheel_animation = game_screen.spin_wheel_animation
        self.display_message = game_screen.display_message
        self.get_user_input = game_screen.get_user_input
        self.game_screen = game_screen

    def display_outside_bets_menu(self):
        """Display the outside bets menu."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.game_screen.display_balance()
        self.display_message('Outside Bets', (100, 100), self.accent_color)
        self.display_message('1. Bet on a color', (100, 200))
        self.display_message('2. Bet on odd or even', (100, 300))
        self.display_message('3. Bet on high/low', (100, 400))
        self.display_message('4. Return to main menu', (100, 500))
        roulette_board = pygame.image.load("Roulette_Board.png")
        roulette_board = pygame.transform.scale(roulette_board, (250, 500))
        self.screen.blit(roulette_board, (500, 100))  # Blit the Surface object directly
        pygame.display.flip()  # Update the full display Surface to the screen

    def get_bet_amount(self):
        """Get the bet amount from the user, ensuring valid input."""
        while True:
            bet = self.get_user_input("Enter your bet amount:")
            try:
                bet = int(bet)  # Convert the input to an integer
                if bet > 0 and bet <= self.game_screen.balance:
                    return bet
                elif bet > self.game_screen.balance:
                    self.display_message("Bet amount cannot exceed current balance. Please try again.", (100, 650))
                else:
                    self.display_message("Bet amount must be a positive number. Please try again.", (100, 650))
            except ValueError:
                self.display_message("Invalid input. Please enter a number.", (100, 650))

    def get_color_bet(self):
        """Get the user's color bet, ensuring valid input."""
        while True:
            color_string = self.get_user_input("Enter your color bet (red, black):").lower().strip()
            if color_string in ["red", "black"]:
                return Color.RED if color_string == "red" else Color.BLACK
            else:
                self.display_message("Invalid color. Please enter red, black.", (100, 650))

    def handle_bet_on_color(self):
        """Handle the bet on a color."""
        bet = self.get_bet_amount()
        color = self.get_color_bet()

        self.spin_wheel_animation()
        ball, result_color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({result_color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByColor(color):  # Check if the user won
            payout_ratio = 35 if color == Color.GREEN else 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)

    def get_odd_even_bet(self):
        """Get the user's odd/even bet, ensuring valid input."""
        while True:
            odd_even = self.get_user_input("Enter your odd or even bet:").lower().strip()
            if odd_even in ["odd", "even"]:
                return odd_even
            else:
                self.display_message("Invalid input. Please enter odd or even.", (100, 650))

    def handle_bet_on_odd_even(self):
        """Handle the bet on odd or even."""
        bet = self.get_bet_amount()
        odd_even = self.get_odd_even_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByOddEven(odd_even):  # Check if the user won
            payout_ratio = 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)

    def get_high_low_bet(self):
        """Get the user's high/low bet, ensuring valid input."""
        while True:
            high_low = self.get_user_input("Enter your high/low bet (high [19-36], low [1-18]):").lower().strip()
            if high_low in ["high", "low"]:
                return high_low
            else:
                self.display_message("Invalid input. Please enter high or low.", (100, 650))

    def handle_bet_on_high_low(self):
        """Handle the bet on high or low."""
        bet = self.get_bet_amount()
        high_low = self.get_high_low_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByHighLow(high_low):  # Check if the user won
            payout_ratio = 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)
