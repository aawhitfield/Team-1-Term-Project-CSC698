import pygame
import sys
import time
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
        self.background_color = (0, 100, 0)  # Dark green background color
        self.text_color = (255, 255, 255)  # White text color
        self.accent_color = (255, 215, 0)  # Gold accent color
        self.result_color = (255, 255, 0)  # Yellow color for results
        self.wheel_image = pygame.image.load("wheel.png")
        self.wheel_image = pygame.transform.scale(self.wheel_image, (400, 400))
        self.wheel_rect = self.wheel_image.get_rect(center=(400, 400))
        self.banner_image = pygame.image.load("roulette.png")
        self.banner_image = pygame.transform.scale(self.banner_image, (400, 200))
        self.advanced_bets_image = pygame.image.load("roulette_table.png")
        
        # Additional attributes
        self.valid_streets = self.generate_valid_streets()
        self.valid_sixlines = self.generate_valid_sixlines()

    def display_message(self, message, pos, color=None):
        """Render and display a message on the screen.

        Args:
            message (str): The message to display.
            pos (tuple): The (x, y) position to display the message on the screen.
            color (tuple): The color of the text. Defaults to self.text_color.
        """
        if color is None:
            color = self.text_color
        text = self.font.render(message, True, color)  # Render the text to an image
        self.screen.blit(text, pos)  # Draw the text image on the screen at the specified position

    def display_balance(self):
        """Display the current balance at the top of the screen."""
        self.display_message(f"Current Balance: ${self.balance}", (100, 50), self.accent_color)
    
    def display_welcome(self):
        """Display the welcome screen."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.display_balance()
        self.screen.blit(self.banner_image, (200, 150))  # Position the image lower
        self.display_message('You have $100 to start with.', (100, 400))
        self.display_message('Good luck!', (100, 500))
        self.display_message('Press any key to continue...', (100, 600))
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
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.display_balance()
        self.display_message('Main Menu', (100, 100), self.accent_color)
        self.display_message('1. Outside Bets', (100, 200))
        self.display_message('2. Inside Bets', (100, 300))
        self.display_message('3. Quit', (100, 400))
        roulette_board = pygame.image.load("Roulette_Board.png")
        roulette_board = pygame.transform.scale(roulette_board, (250, 500))
        self.screen.blit(roulette_board, (500, 100))  # Blit the Surface object directly

        pygame.display.flip()  # Update the full display Surface to the screen

    def display_outside_bets_menu(self):
        """Display the outside bets menu."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.display_balance()
        self.display_message('Outside Bets', (100, 100), self.accent_color)
        self.display_message('1. Bet on a color', (100, 200))
        self.display_message('2. Bet on odd or even', (100, 300))
        self.display_message('3. Return to main menu', (100, 400))
        roulette_board = pygame.image.load("Roulette_Board.png")
        roulette_board = pygame.transform.scale(roulette_board, (250, 500))
        self.screen.blit(roulette_board, (500, 100))  # Blit the Surface object directly
        pygame.display.flip()  # Update the full display Surface to the screen

    def display_inside_bets_menu(self):
        """Display the inside bets menu."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.display_balance()
        self.display_message('Inside Bets', (100, 100), self.accent_color)
        self.display_message('1. Bet on a number', (100, 200))
        self.display_message('2. Street Bet', (100,300))
        self.display_message('3. Sixline', (100, 400))
        self.display_message('4. Return to main menu', (100, 500))
        roulette_board = pygame.image.load("Roulette_Board.png")
        roulette_board = pygame.transform.scale(roulette_board, (250, 500))
        self.screen.blit(roulette_board, (500, 100))  # Blit the Surface object directly
        pygame.display.flip()  # Update the full display Surface to the screen

    def get_user_input(self, prompt="", menu_function=None):
        """Get user input from the screen.

        Args:
            prompt (str): The prompt message to display.
            menu_function (function): Function to call to display a specific menu.

        Returns:
            str: The user input.
        """
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
            color_string = self.get_user_input("Enter your color bet (red, black):").lower().strip()
            if color_string in ["red", "black"]:
                return Color.RED if color_string == "red" else Color.BLACK
            else:
                self.display_message("Invalid color. Please enter red, black.", (100, 650))

    def get_odd_even_bet(self):
        """Get the user's odd/even bet, ensuring valid input."""
        while True:
            odd_even = self.get_user_input("Enter your odd or even bet:").lower().strip()
            if odd_even in ["odd", "even"]:
                return odd_even
            else:
                self.display_message("Invalid input. Please enter odd or even.", (100, 650))

    def generate_valid_streets(self):
        """Generate a list of valid street bets."""
        valid_streets = []
        for i in range(1, 34):
            if i % 3 == 0:
                continue
            street = (i, i + 1, i + 2)
            valid_streets.append(street)
        return valid_streets

    def generate_valid_sixlines(self):
        """Generate a list of valid sixline bets."""
        valid_sixlines = []
        for i in range(1, 31):
            if i % 3 == 2:
                continue
            sixline = (i, i + 1, i + 2, i + 3, i + 4, i + 5)
            valid_sixlines.append(sixline)
        return valid_sixlines

    def get_street_bet(self):
        """Get the user's street bet, ensuring valid input."""
        while True:
            bet_choice = input("Choose a row or 'street' of numbers (e.g., '1,2,3'): ")
            street = [int(num) for num in bet_choice.split(",")]
            if self.is_valid_street(street):
                return tuple(street)
            else:
                print("Invalid input. Please enter a valid row or 'street' of numbers (e.g., '1,2,3').")

    def is_valid_street(self, street):
        """
        Checks if the given street of numbers is a valid street bet.
        A valid street bet consists of three consecutive numbers on the roulette wheel.
        """
        return tuple(sorted(street)) in self.valid_streets

    def get_sixline_bet(self):
        """Get the user's sixline bet, ensuring valid input."""
        while True:
            bet_choice = input("Choose a sixline of numbers (e.g., '1,2,3,4,5,6'): ")
            sixline = [int(num) for num in bet_choice.split(",")]
            if self.is_valid_sixline(sixline):
                return tuple(sixline)
            else:
                print("Invalid input. Please enter a valid sixline of numbers (e.g., '1,2,3,4,5,6').")

    def is_valid_sixline(self, sixline):
        """
        Checks if the given sixline of numbers is a valid sixline bet.
        A valid sixline bet consists of six consecutive numbers on the roulette wheel.
        """
        return tuple(sorted(sixline)) in self.valid_sixlines

    def spin_wheel_animation(self):
        """Display the spinning wheel animation."""
        overlay = pygame.Surface((800, 800))  # Create a transparent overlay
        overlay.set_alpha(255)  # Set transparency level
        overlay.fill((0, 0, 0))  # Fill the overlay with black color
        angle = 0

        start_time = time.time()
        while time.time() - start_time < 2:  # Rotate for 2 seconds
            self.screen.fill(self.background_color)
            self.display_balance()

            angle += 10  # Rotate the image
            rotated_image = pygame.transform.rotate(self.wheel_image, angle)
            new_rect = rotated_image.get_rect(center=self.wheel_rect.center)

            self.screen.blit(overlay, (0, 0))  # Apply the transparent overlay
            self.screen.blit(rotated_image, new_rect.topleft)
            pygame.display.flip()
            self.clock.tick(30)

    def handle_bet_on_number(self):
        """Handle the bet on a specific number."""
        bet = self.get_bet_amount()
        number = self.get_number_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByNumber(number):  # Check if the user won
            payout_ratio = 35
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
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

    def handle_bet_on_street(self):
        """Handle a street bet."""
        bet = self.get_bet_amount()
        street = self.get_street_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByStreet(street):  # Check if the user won
            payout_ratio = 11
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)

    def handle_bet_on_sixline(self):
        """Handle a sixline bet."""
        bet = self.get_bet_amount()
        sixline = self.get_sixline_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_balance()
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerBySixline(sixline):  # Check if the user won
            payout_ratio = 5
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.balance += winnings
            self.display_message(f"You won ${winnings}!", (100, 750))
        else:
            self.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
        pygame.display.flip()
        pygame.time.wait(2000)

    def show_advanced_bets(self):
        """Display the advanced bets image for 5 seconds and then return to menu."""
        self.screen.fill(self.background_color)
        self.screen.blit(self.advanced_bets_image, (100, 100))
        pygame.display.flip()
        pygame.time.wait(5000)

    def main_loop(self):
        """Main game loop to handle game logic and user interactions."""
        self.display_welcome()  # Display the welcome screen
        running = True  # State to track if the game is running

        while running:
            if self.balance <= 0:
                running = False
                self.display_message("Game over! You have no money left.", (100, 800))
                pygame.display.flip()
                pygame.time.wait(3000)
                break

            self.display_menu()  # Display the menu
            choice = self.get_user_input("Enter your choice:", menu_function=self.display_menu)  # Get the user's menu choice

            if choice == "3":  # Quit the game
                running = False
            elif choice == "1":
                self.display_outside_bets_menu()
                outside_choice = self.get_user_input("Enter your choice:", menu_function=self.display_outside_bets_menu)
                if outside_choice == "1":
                    self.handle_bet_on_color()
                elif outside_choice == "2":
                    self.handle_bet_on_odd_even()
                elif outside_choice == "3":
                    continue
            elif choice == "2":
                self.display_inside_bets_menu()
                inside_choice = self.get_user_input("Enter your choice:", menu_function=self.display_inside_bets_menu)
                if inside_choice == "1":
                    self.handle_bet_on_number()
                elif inside_choice == "2":
                    self.handle_bet_on_street()
                elif inside_choice == "3":
                    continue

        pygame.quit()  # Quit pygame
