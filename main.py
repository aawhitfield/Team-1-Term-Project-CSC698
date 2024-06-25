from pygame_screen import PyGameScreen
from screen_info import ScreenInfo

# Initialize screen information
screen_info = ScreenInfo(900, 900)

if __name__ == "__main__":
    game = PyGameScreen(screen_info)
    game.main_loop()
