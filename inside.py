import pygame
import os
import sys

class Inside:
    """Class to Handle Inside Bets"""

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

        self.frames = {}
        frame_folder = "seinfeld_gif"  # Replace with your folder name
        for filename in os.listdir(frame_folder):
            if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
                frame_path = os.path.join(frame_folder, filename)
                frame_name = os.path.splitext(filename)[0]
                self.frames[frame_name] = pygame.image.load(frame_path).convert_alpha()

        # Load celebration frames
        self.celebration_frames = [self.frames[f"seinfeld_frame{i + 1}"] for i in
                                   range(30)]  # Adjust the range based on your GIF frames


    def display_inside_bets_menu(self):
        """Display the inside bets menu."""
        self.screen.fill(self.background_color)  # Fill the screen with the background color
        self.game_screen.display_balance()
        self.display_message('Inside Bets', (100, 100), self.accent_color)
        self.display_message('1. Bet on a number', (100, 200))
        self.display_message('2. Street Bet', (100, 300))
        self.display_message('3. Corner Bet', (100, 400))
        self.display_message('4. Sixline Bet', (100, 500))
        self.display_message('5. Return to main menu', (100, 600))
        roulette_board = pygame.image.load("roulette_gameboard.png")
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

    def generate_valid_streets(self):
        """Generate a list of valid street bets."""
        valid_streets = []
        for i in range(1, 34):
            if i % 3 == 0:
                continue
            street = (i, i + 1, i + 2)
            valid_streets.append(street)
        return valid_streets

    def generate_valid_corners(self):
        """Generate a list of valid corners."""
        valid_corners = []
        for i in range(1, 32):
            if i % 2 == 2:
                continue
            corner = (i, i + 1, i + 3, i + 4)
            valid_corners.append(corner)
        return valid_corners

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
            bet_choice = self.get_user_input("Choose a row or 'street' of numbers (e.g., '1,2,3'): ")
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
        return tuple(sorted(street)) in self.generate_valid_streets()

    def get_corner_bet(self):
        """Get the user's corners bet, ensuring valid input."""
        while True:
            bet_choice = self.get_user_input("Choose a corner bet (e.g., ;'1,2,4,5'): ")
            corner = [int(num) for num in bet_choice.split(",")]
            if self.is_valid_corner(corner):
                return tuple(corner)
            else:
                print("Invalid input. Please enter a valid corner bet (e.g., ;'1,2,4,5'): ")

    def is_valid_corner(self, corner):
        """
        Checks if the given corner bet is a valid corner bet.
        """
        return tuple(sorted(corner)) in self.generate_valid_corners()

    def get_sixline_bet(self):
        """Get the user's sixline bet, ensuring valid input."""
        while True:
            bet_choice = self.get_user_input("Choose a sixline of numbers (e.g., '1,2,3,4,5,6'): ")
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
        return tuple(sorted(sixline)) in self.generate_valid_sixlines()

    def handle_bet_on_number(self):
        """Handle the bet on a specific number."""
        bet = self.get_bet_amount()
        number = self.get_number_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByNumber(number):  # Check if the user won
            payout_ratio = 35
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_winning_gif()
            self.display_message(f"You won ${winnings}!", (100, 750))
            
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
            self.game_screen.sound.play_losing_sound()
            pygame.time.wait(1500)
            self.game_screen.sound.stop_losing_sound()
            pygame.display.flip()
            pygame.time.wait(2000)


    def handle_bet_on_street(self):
        """Handle a street bet."""
        bet = self.get_bet_amount()
        street = self.get_street_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByStreet(street):  # Check if the user won
            payout_ratio = 11
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_winning_gif()
            self.display_message(f"You won ${winnings}!", (100, 750))
            
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
            self.game_screen.sound.play_losing_sound()
            pygame.time.wait(1500)
            self.game_screen.sound.stop_losing_sound()
        pygame.display.flip()
        pygame.time.wait(2000)

    def handle_bet_on_corner(self):
        """Handle a corner bet."""
        bet = self.get_bet_amount()
        corner = self.get_corner_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerByCorner(corner):  # Check if the user won
            payout_ratio = 8
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_winning_gif()
            self.display_message(f"You won ${winnings}!", (100, 750))
            
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
            self.game_screen.sound.play_losing_sound()
            pygame.time.wait(1500)
            self.game_screen.sound.stop_losing_sound()
        pygame.display.flip()
        pygame.time.wait(2000)

    def handle_bet_on_sixline(self):
        """Handle a sixline bet."""
        bet = self.get_bet_amount()
        sixline = self.get_sixline_bet()

        self.spin_wheel_animation()
        ball, color = self.roulette.spin()  # Spin the wheel
        self.screen.fill(self.background_color)
        self.display_message(f"The ball landed in pocket {ball} ({color.name.lower()})", (100, 700), self.result_color)
        pygame.display.flip()
        pygame.time.wait(2000)

        if self.roulette.isWinnerBySixline(sixline):  # Check if the user won
            payout_ratio = 5
            winnings = self.roulette.calculateWinnings(bet, payout_ratio)
            self.game_screen.balance += winnings
            self.display_winning_gif()
            self.display_message(f"You won ${winnings}!", (100, 750))
            
        else:
            self.game_screen.balance -= bet
            self.display_message(f"You lost ${bet}.", (100, 750))
            self.game_screen.sound.play_losing_sound()
            pygame.time.wait(1500)
            self.game_screen.sound.stop_losing_sound()
        pygame.display.flip()
        pygame.time.wait(2000)

    def display_winning_gif(self):
        """Display a GIF animation on the winning screen."""
        self.screen.fill(self.background_color)
        
        # Play the winning sound
        self.game_screen.sound.play_winning_sound()

        frame_duration = 100  # Milliseconds between frames
        start_time = pygame.time.get_ticks()

        running = True
        while running:
            current_time = pygame.time.get_ticks()
            frame_index = (current_time - start_time) // frame_duration % len(self.celebration_frames)

            self.screen.blit(self.celebration_frames[frame_index], (350, 300))  # Adjust position as needed

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    running = False

            if current_time - start_time > 2900:  # Display for 3 seconds
                running = False

        self.game_screen.sound.stop_winning_sound()  # Stop the sound after the animation
        pygame.time.wait(0)
