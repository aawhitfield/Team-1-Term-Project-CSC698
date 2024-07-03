# screen_info.py
class ScreenInfo:
    """Class to store and manage screen information."""

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)

    def update_size(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)