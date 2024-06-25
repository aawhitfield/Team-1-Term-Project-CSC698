import pygame
import sys
import time
from color import Color

class Outside:
    """Class to Handle Outside Bets"""

    def __init__(self, screen, roulette, font, background_color, accent_color, result_color, clock, spin_wheel_animation):
        self.screen = screen
        self.roulette = roulette
        self.font = font
        self.background_color = background_color
        self.accent_color = accent_color
        self.result_color = result_color
        self.balance = 100
        self.clock = clock
        self.spin_wheel_animation = spin_wheel_animation

    def display_message(self, message, pos, color=None):
        """Render and display a message on the screen."""
        if color is None:
            color = self.accent_color
        text = self.font.render(message, True, color)  # Render the text to an image
        self.screen.blit(text, pos)  # Draw the text image on the screen at the specified position

    def display_balance(self):
        """Display the current balance at the top of the screen."""
        self.display_message(f"Current Balance: ${self.balance}", (100, 50), self.accent_color)

    def display_outside_bets_menu(self):
        """Display the outside bets menu."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.display_balance()
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
                if bet > 0:
                    return bet
                else:
                    self.display_message("Bet amount must be a positive number. Please try again.", (100, 650))
            except ValueError:
                self.display_message("Invalid input. Please enter a number.", (100, 650))

    def get_user_input(self, prompt="", menu_function=None):
        """Get user input from the screen."""
        input_box = pygame.Rect(300, 650, 140, 48)  # Create a rectangle for the input box
        color_inactive = pygame.Color('lightskyblue3')  # Inactive color for the input box
        color_active = self.accent_color  # Active color for the input box
        color = color_active  # Start with the active color to automatically focus
        active = True  # Automatically set the input box to active
        text = ''  # Text entered by the user
        done = False  # State to track when input is complete

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle window close button
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:  # Handle key press
                    if active:
                        if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:  # Complete input on Enter or keypad Enter key
                            done = True
                        elif event.key == pygame.K_BACKSPACE:  # Remove last character on Backspace key
                            text = text[:-1]
                        else:  # Add typed character to the text
                            text += event.unicode

            self.screen.fill(self.background_color)  # Clear the screen with background color
            self.display_balance()
            if menu_function:
                menu_function()  # Call the appropriate menu function
            self.display_message(prompt, (100, 600))  # Display the prompt
            txt_surface = self.font.render(text, True, color)  # Render the text entered by the user
            width = max(200, txt_surface.get_width() + 10)  # Set the width of the input box
            input_box.w = width  # Update the input box width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw the text on the screen
            pygame.draw.rect(self.screen, color, input_box, 2)  # Draw the input box
            roulette_board = pygame.image.load("Roulette_Board.png")
            roulette_board = pygame.transform.scale(roulette_board, (250, 500))
            self.screen.blit(roulette_board, (500, 100))  # Blit the Surface object directly
            pygame.display.flip()  # Update the full display Surface to the screen
            self.clock.tick(30)  # Control the loop's frame rate

        return text  # Return the text entered by the user

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
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({result_color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByColor(color):  # Check if the user won
            payout_ratio = 35 if color == Color.GREEN else 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
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
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByOddEven(odd_even):  # Check if the user won
            payout_ratio = 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
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
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByHighLow(high_low):  # Check if the user won
            payout_ratio = 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)
