import pygame

class Sound:
    """Class to handle sound effects in the game."""

    def __init__(self):
        pygame.mixer.init()
        self.spinning_sound = pygame.mixer.Sound("audio/spinning.mp3")
        self.coins_sound = pygame.mixer.Sound("audio/coins.mp3")
        self.failure_sound = pygame.mixer.Sound("audio/failure.mp3")

    def play_spinning_sound(self):
        """Play the spinning sound effect."""
        self.spinning_sound.play()

    def stop_spinning_sound(self):
        """Stop the spinning sound effect."""
        self.spinning_sound.stop()

    def play_winning_sound(self):
        self.coins_sound.play()

    def stop_winning_sound(self):
        self.coins_sound.stop()

    def play_losing_sound(self):
        """Play the failure sound effect."""
        self.failure_sound.play()

    def stop_losing_sound(self):
        """Stop the failure sound effect."""
        self.failure_sound.stop()
