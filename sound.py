import pygame

class Sound:
    """Class to handle sound effects in the game."""

    def __init__(self):
        pygame.mixer.init()
        self.spinning_sound = pygame.mixer.Sound("audio/spinning.mp3")
        self.coins_sound = pygame.mixer.Sound("audio/coins.mp3")

    def play_spinning_sound(self):
        """Play the spinning sound effect."""
        self.spinning_sound.play()

    def stop_spinning_sound(self):
        """Stop the spinning sound effect."""
        self.spinning_sound.stop()

    def play_coins_sound(self):
        self.coins_sound.play()

    def stop_coins_sound(self):
        self.coins_sound.stop()
