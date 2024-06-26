import sys
import time
import os
import pygame
from inside import Inside
from outside import Outside
from roulette import Roulette


class PyGameScreen:
    """Class to handle the UI and user interactions using PyGame."""

    def __init__(self, screen_info):
        """Initialize the PyGame screen and set up initial game settings."""
        pygame.init()  # Initialize all imported pygame modules
        self.screen_info = screen_info
        self.screen = pygame.display.set_mode((self.screen_info.width, self.screen_info.height))  # Set the display window size
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
        self.wheel_image = pygame.transform.scale(self.wheel_image, self.screen_info.center)
        self.wheel_rect = self.wheel_image.get_rect(center=self.screen_info.center)
        self.banner_image = pygame.image.load("roulette.png")
        self.banner_image = pygame.transform.scale(self.banner_image, (self.screen_info.width // 2, 200))
        self.advanced_bets_image = pygame.image.load("roulette_table.png")

        self.images = {}
        image_folder = "gif_frames"  # Replace with your folder name
        for filename in os.listdir(image_folder):
            if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
                image_path = os.path.join(image_folder, filename)
                image_name = os.path.splitext(filename)[0]
                self.images[image_name] = pygame.image.load(image_path).convert_alpha()

        # Load game over frames
        self.game_over_frames = [self.images[f"gif_frame{i+1}"] for i in
                                 range(30)]  # Adjust the range based on your GIF frames

        # Initialize Outside and Inside bets handlers
        self.outside = Outside(self)
        self.inside = Inside(self)

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
        balance_rect = pygame.Rect(100, 50, 300, 50)
        pygame.draw.rect(self.screen, self.background_color, balance_rect)  # Clear the area
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

    def spin_wheel_animation(self):
        """Display the spinning wheel animation."""
        overlay = pygame.Surface((self.screen_info.width, self.screen_info.height))  # Create a transparent overlay
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

    def show_advanced_bets(self):
        """Display the advanced bets image for 5 seconds and then return to menu."""
        self.screen.fill(self.background_color)
        self.screen.blit(self.advanced_bets_image, (100, 100))
        pygame.display.flip()
        pygame.time.wait(5000)

    def display_game_over_gif(self):
        """Display a GIF animation on the game over screen."""
        self.screen.fill(self.background_color)
        self.display_message("Game over! You have no money left.", (100, 300), self.result_color)

        frame_duration = 100  # Milliseconds between frames
        start_time = pygame.time.get_ticks()

        running = True
        while running:
            current_time = pygame.time.get_ticks()
            frame_index = (current_time - start_time) // frame_duration % len(self.game_over_frames)

            self.screen.blit(self.game_over_frames[frame_index], (200, 400))  # Adjust position as needed

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False

            if current_time - start_time > 3000:  # Display for 3 seconds
                running = False

        pygame.time.wait(1000)  # Wait for 1 second after animation ends

    def main_loop(self):
        """Main game loop to handle game logic and user interactions."""
        self.display_welcome()  # Display the welcome screen
        running = True  # State to track if the game is running

        while running:
            if self.balance <= 0:
                running = False
                self.display_game_over_gif()  # Call game over screen method here
                break
                self.display_message("Game over! You have no money left.", (100, 800))

            self.display_menu()  # Display the menu
            self.display_balance()  # Ensure balance is displayed in the main loop
            choice = self.get_user_input("Enter your choice:", menu_function=self.display_menu)  # Get the user's menu choice

            if choice == "3":  # Quit the game
                running = False
            elif choice == "1":
                self.outside.display_outside_bets_menu()
                outside_choice = self.get_user_input("Enter your choice:", menu_function=self.outside.display_outside_bets_menu)
                if outside_choice == "1":
                    self.outside.handle_bet_on_color()
                elif outside_choice == "2":
                    self.outside.handle_bet_on_odd_even()
                elif outside_choice == "3":
                    self.outside.handle_bet_on_high_low()
                elif outside_choice == "4":
                    continue
            elif choice == "2":
                self.inside.display_inside_bets_menu()
                inside_choice = self.get_user_input("Enter your choice:", menu_function=self.inside.display_inside_bets_menu)
                if inside_choice == "1":
                    self.inside.handle_bet_on_number()
                elif inside_choice == "2":
                    self.inside.handle_bet_on_street()
                elif inside_choice == "3":
                    self.inside.handle_bet_on_sixline()
                elif inside_choice == "4":
                    continue

        pygame.quit()  # Quit pygame
