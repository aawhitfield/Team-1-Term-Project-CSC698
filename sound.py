import pygame

class Sound:
    """Class to handle sound effects in the game."""

    def __init__(self):
        pygame.mixer.init()
        self.spinning_sound = pygame.mixer.Sound("audio/spinning.mp3")

    def play_spinning_sound(self):
        """Play the spinning sound effect."""
        self.spinning_sound.play()

    def stop_spinning_sound(self):
        """Stop the spinning sound effect."""
        self.spinning_sound.stop()
