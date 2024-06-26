# Roulette Game

A simple roulette game simulation in Python, allowing users to place bets on numbers, colors, and odd/even outcomes. The game is designed for educational purposes and demonstrates basic Python programming concepts, including classes, enums, input validation, and game logic.

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
    python --version
    ```

## Usage

Run the game using Python:
```bash
python3 main.py
```
Follow the on-screen prompts to place your bets and spin the roulette wheel. You start with a balance of $100 and can bet on numbers, colors, or whether the result will be odd or even.

## Game Rules

- **Number Bet**: Bet on a specific number (0-36, 00). If the ball lands on your number, you win 35 times your bet.
- **Color Bet**: Bet on a color (red, black, green). If the ball lands on your color, you win:
  - 1:1 for red or black
  - 35:1 for green (0 or 00)
- **Odd/Even Bet**: Bet on whether the number will be odd or even. If the ball lands on your choice, you win 1:1. Note: 0 and 00 are neither odd nor even.

## Betting Options

When prompted, you can choose from the following betting options:

1. **Bet on a number**: Enter a number between 0 and 36, or 00.
2. **Bet on a color**: Enter "red", "black", or "green".
3. **Bet on odd/even**: Enter "odd" or "even".
4. **Quit**: Exit the game.

## Project Structure
roulette-game/
│
├── __pycache__/       # Cache files generated by Python
├── .gitignore         # Git ignore file
├── color.py           # Enum class for color definitions
├── main.py            # Main game script
├── README.md          # This README file
├── roulette.py        # Roulette class with game logic
└── screen.py          # Screen class for handling user interaction


## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes.
4. Commit and push your changes to your forked repository.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. 


