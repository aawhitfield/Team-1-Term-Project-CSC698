import pygame
import sys
from color import Color
from roulette import Roulette

class PyGameScreen:
    """Class to handle the UI and user interactions using PyGame."""
    
    def __init__(self):
        """Initialize the PyGame screen and set up initial game settings."""
        pygame.init()  # Initialize all imported pygame modules
        self.screen = pygame.display.set_mode((800, 800))  # Set the display window size
        pygame.display.set_caption('Roulette Game')  # Set the window caption
        self.clock = pygame.time.Clock()  # Create an object to help track time
        self.font = pygame.font.SysFont(None, 48)  # Set the font and size for rendering text
        self.roulette = Roulette()  # Initialize the Roulette game logic
        self.balance = 100  # Set the initial balance for the player

    def display_message(self, message, pos):
        """Render and display a message on the screen.

        Args:
            message (str): The message to display.
            pos (tuple): The (x, y) position to display the message on the screen.
        """
        text = self.font.render(message, True, (255, 255, 255))  # Render the text to an image
        self.screen.blit(text, pos)  # Draw the text image on the screen at the specified position

    def display_balance(self):
        """Display the current balance at the top of the screen."""
        self.display_message(f"Current Balance: ${self.balance}", (100, 50))
    
    def display_welcome(self):
        """Display the welcome screen."""
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        self.display_balance()
        self.display_message('Welcome to Roulette!', (100, 100))
        self.display_message('You have $100 to start with.', (100, 200))
        self.display_message('Good luck!', (100, 300))
        self.display_message('Press any key to continue...', (100, 400))
        pygame.display.flip()  # Update the full display Surface to the screen

        # Wait for the user to press any key to continue
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle window close button
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # Handle any key press
                    waiting = False

    def display_menu(self):
        """Display the main menu with options."""
        self.screen.fill((0, 0, 0))  # Fill the screen with black
        self.display_balance()
        self.display_message('1. Bet on a number', (100, 100))
        self.display_message('2. Bet on a color', (100, 200))
        self.display_message('3. Bet on odd or even', (100, 300))
        self.display_message('4. Quit', (100, 400))
        pygame.display.flip()  # Update the full display Surface to the screen

    def get_user_input(self, prompt=""):
        """Get user input from the screen.

        Args:
            prompt (str): The prompt message to display.

        Returns:
            str: The user input.
        """
        input_box = pygame.Rect(300, 650, 140, 48)  # Create a rectangle for the input box
        color_inactive = pygame.Color('lightskyblue3')  # Inactive color for the input box
        color_active = pygame.Color('dodgerblue2')  # Active color for the input box
        color = color_active  # Start with the active color to automatically focus
        active = True  # Automatically set the input box to active
        # this will allow the user to start typing without having to click on the input box
        text = ''  # Text entered by the user
        done = False  # State to track when input is complete

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Handle window close button
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
                    # Toggle the active state if the input box is clicked
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

            self.screen.fill((0, 0, 0))  # Clear the screen
            self.display_balance()
            self.display_menu()  # Redraw the menu
            self.display_message(prompt, (100, 600))  # Display the prompt
            txt_surface = self.font.render(text, True, color)  # Render the text entered by the user
            width = max(200, txt_surface.get_width() + 10)  # Set the width of the input box
            input_box.w = width  # Update the input box width
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # Draw the text on the screen
            pygame.draw.rect(self.screen, color, input_box, 2)  # Draw the input box
            pygame.display.flip()  # Update the full display Surface to the screen
            self.clock.tick(30)  # Control the loop's frame rate

        return text  # Return the text entered by the user

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

    def get_number_bet(self):
        """Get the user's number bet, ensuring valid input."""
        while True:
            number = self.get_user_input("Enter your number bet (0-36, 00):")
            if number == "00":
                return 37
            try:
                number = int(number)
                if 0 <= number <= 36:
                    return number
                else:
                    self.display_message("Number must be between 0 and 36 or '00'. Please try again.", (100, 650))
            except ValueError:
                self.display_message("Invalid input. Please enter a number between 0 and 36 or '00'.", (100, 650))

    def get_color_bet(self):
        """Get the user's color bet, ensuring valid input."""
        while True:
            color_string = self.get_user_input("Enter your color bet (red, black, green):").lower().strip()
            if color_string in ["red", "black", "green"]:
                return Color.RED if color_string == "red" else Color.BLACK if color_string == "black" else Color.GREEN
            else:
                self.display_message("Invalid color. Please enter red, black, or green.", (100, 650))

    def get_odd_even_bet(self):
        """Get the user's odd/even bet, ensuring valid input."""
        while True:
            odd_even = self.get_user_input("Enter your odd or even bet:").lower().strip()
            if odd_even in ["odd", "even"]:
                return odd_even
            else:
                self.display_message("Invalid input. Please enter odd or even.", (100, 650))

    def handle_bet_on_number(self):
        """Handle the bet on a specific number."""
        bet = self.get_bet_amount()
        number = self.get_number_bet()

        ball, color = self.roulette.spin()  # Spin the wheel
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700))
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByNumber(number):  # Check if the user won
            payout_ratio = 35
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += bet + winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))

        pygame.display.flip()
        pygame.time.wait(2000)

    def handle_bet_on_color(self):
        """Handle the bet on a color."""
        bet = self.get_bet_amount()
        color = self.get_color_bet()

        ball, result_color = self.roulette.spin()  # Spin the wheel
        self.display_message(f"The ball landed in pocket {ball} ({result_color.name.lower()})", (100, 700))
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByColor(color):  # Check if the user won
            payout_ratio = 35 if color == Color.GREEN else 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += bet + winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))

        pygame.display.flip()
        pygame.time.wait(2000)

    def handle_bet_on_odd_even(self):
        """Handle the bet on odd or even."""
        bet = self.get_bet_amount()
        odd_even = self.get_odd_even_bet()

        ball, color = self.roulette.spin()  # Spin the wheel
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700))
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByOddEven(odd_even):  # Check if the user won
            payout_ratio = 1
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += bet + winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))

        pygame.display.flip()
        pygame.time.wait(2000)

    def main_loop(self):
        """Main game loop to handle game logic and user interactions."""
        self.display_welcome()  # Display the welcome screen
        running = True  # State to track if the game is running

        while running:
            self.display_menu()  # Display the menu
            choice = self.get_user_input("Enter your choice:")  # Get the user's menu choice

            if choice == "4":  # Quit the game
                running = False
            elif choice == "1":
                self.handle_bet_on_number()
            elif choice == "2":
                self.handle_bet_on_color()
            elif choice == "3":
                self.handle_bet_on_odd_even()

        pygame.quit()  # Quit pygame
