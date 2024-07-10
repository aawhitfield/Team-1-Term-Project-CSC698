# Roulette Game

A comprehensive roulette game simulation in Python, allowing users to place a variety of bets, including numbers, colors, odd/even outcomes, high/low ranges, columns, and dozens. The game includes sound effects, animated GIFs for wins and losses, and a detailed instructions page. Designed for educational purposes, this project demonstrates advanced Python programming concepts, including classes, enums, input validation, game logic, and user interaction via the PyGame library. The project now supports a more user-friendly experience with scrollable instructions and an improved betting menu.

## Authers
- Edgar

## Table of Contents



- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Betting Options](#betting-options)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aawhitfield/CSC-698-Project.git
    ```
2. Ensure you have Python 3 installed. You can check your Python version with:
    ```bash
    python3 --version
    ```

## Usage

Run the game using Python:
```bash
python3 main.py
```
## Usage

1. **Starting the Game**: Run the game script to start with an initial balance of $100.
2. **Main Menu**: 
   - Choose from the following options:
     1. Outside Bets
     2. Inside Bets
     3. Instructions
     4. Quit
3. **Placing Bets**:
   - **Outside Bets**:
     1. Bet on a color: Choose either red or black.
     2. Bet on odd or even: Choose either odd or even numbers.
     3. Bet on high/low: Bet on numbers 1-18 (low) or 19-36 (high).
     4. Bet on column: Choose one of the three columns.
     5. Bet on dozen: Choose from 1-12, 13-24, or 25-36.
   - **Inside Bets**:
     1. Bet on a number: Choose a specific number.
     2. Street Bet: Bet on a row of three numbers.
     3. Corner Bet: Bet on a block of four numbers.
     4. Sixline Bet: Bet on a block of six numbers.
4. **Spinning the Wheel**: After placing your bet, the roulette wheel will spin and the result will be displayed along with the outcome of your bet.
5. **Instructions**: Access the instructions page for detailed descriptions of each bet type, how they work, how you win, and the payout ratios. Use the UP/DOWN arrow keys to scroll through the instructions. Press any other key to return to the main menu.
6. **Sound Effects**: Enjoy sound effects for spinning the wheel, winning, and losing, enhancing the gaming experience.

Follow the on-screen prompts to place your bets, spin the roulette wheel, and manage your balance.


## Game Rules

- **Number Bet**: Bet on a specific number (0-36, 00). If the ball lands on your number, you win 35 times your bet.
- **Color Bet**: Bet on a color (red, black). If the ball lands on your color, you win 1:1.
- **Odd/Even Bet**: Bet on whether the number will be odd or even. If the ball lands on your choice, you win 1:1. Note: 0 and 00 are neither odd nor even.
- **High/Low Bet**: Bet on whether the number will be in the low range (1-18) or high range (19-36). If the ball lands in your chosen range, you win 1:1.
- **Column Bet**: Bet on one of the three columns of numbers on the table. If the ball lands in your chosen column, you win 2:1.
- **Dozen Bet**: Bet on one of the three dozens of numbers (1-12, 13-24, 25-36). If the ball lands in your chosen dozen, you win 2:1.
- **Street Bet**: Bet on a row of three consecutive numbers. If the ball lands on any of the three numbers, you win 11:1.
- **Corner Bet**: Bet on a block of four numbers. If the ball lands on any of the four numbers, you win 8:1.
- **Sixline Bet**: Bet on a block of six consecutive numbers. If the ball lands on any of the six numbers, you win 5:1.


## Betting Options

When prompted, you can choose from the following betting options:

1. **Bet on a number**: Enter a number between 0 and 36, or 00.
2. **Bet on a color**: Enter "red" or "black".
3. **Bet on odd/even**: Enter "odd" or "even".
4. **Bet on high/low**: Enter "high" for numbers 19-36 or "low" for numbers 1-18.
5. **Bet on a column**: Enter the column number (1, 2, or 3).
6. **Bet on a dozen**: Enter the dozen number (1, 2, or 3).
7. **Bet on a street**: Enter three consecutive numbers (e.g., "1,2,3").
8. **Bet on a corner**: Enter four numbers forming a square (e.g., "1,2,4,5").
9. **Bet on a sixline**: Enter six consecutive numbers (e.g., "1,2,3,4,5,6").
10. **Instructions**: View the game instructions and betting options.
11. **Quit**: Exit the game.


## Project Structure

```bash
roulette-game/
├── audio/                       # Sound effects used in the game
│   ├── coins.mp3
│   ├── failure.mp3
│   ├── game_over.mp3
│   └── spinning.mp3
├── gif_frames/                  # Frames for game animations
├── seinfeld_gif/                # Frames for winning animations
├── .gitignore                   # Git ignore file
├── color.py                     # Enum class for color definitions
├── inside.py                    # Inside bets handling
├── instructions.py              # Instructions for game rules
├── main.py                      # Main game script
├── outside.py                   # Outside bets handling
├── pygame_screen.py             # Screen class for handling user interaction
├── README.md                    # This README file
├── roulette_gameboard.png       # Image of the roulette gameboard
├── roulette.jpeg                # Image of the roulette wheel
├── roulette.png                 # Image of the roulette wheel
├── roulette.py                  # Roulette class with game logic
├── screen_info.py               # Screen information class
└── sound.py                     # Sound handling class
└── wheel.png                    # Image of the roulette wheel
```



## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes.
4. Commit and push your changes to your forked repository.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. 


