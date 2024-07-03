import pygame

class Instructions:
    """Class to display game instructions."""

    def __init__(self, screen, font, background_color, text_color):
        self.screen = screen
        self.font = font
        self.background_color = background_color
        self.text_color = text_color
        self.instructions = [
            "Use UP/DOWN arrow keys to scroll through instructions.",
            "Press any other key to return to the main menu.",
            "",
            "Outside Bets:",
            "1. Bet on a color: Choose either red or black. If the ball lands on your chosen color, you win. Payout is 1:1.",
            "",
            "2. Bet on odd or even: Choose either odd or even numbers. If the ball lands on a number of your chosen type, you win. Payout is 1:1.",
            "",
            "3. Bet on high/low: Bet on numbers 1-18 (low) or 19-36 (high). If the ball lands in your chosen range, you win. Payout is 1:1.",
            "",
            "4. Bet on column: Choose one of the three columns. If the ball lands on a number in your chosen column, you win. Payout is 2:1.",
            "",
            "5. Bet on dozen: Choose from 1-12, 13-24, or 25-36. If the ball lands in your chosen dozen, you win. Payout is 2:1.",
            "",
            "Inside Bets:",
            "1. Bet on a number: Choose a specific number. If the ball lands on your chosen number, you win. Payout is 35:1.",
            "",
            "2. Street Bet: Bet on a row of three numbers. If the ball lands on any of the three numbers, you win. Payout is 11:1.",
            "",
            "3. Corner Bet: Bet on a block of four numbers. If the ball lands on any of the four numbers, you win. Payout is 8:1.",
            "",
            "4. Sixline Bet: Bet on a block of six numbers. If the ball lands on any of the six numbers, you win. Payout is 5:1.",
        ]
        self.position = 0

    def wrap_text(self, text, max_width):
        """Wrap text to fit within the specified width."""
        words = text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if self.font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word

        lines.append(current_line)
        return lines

    def display(self):
        self.screen.fill(self.background_color)
        y_offset = 100
        max_width = self.screen.get_width() - 200  # Padding for left and right

        for i, line in enumerate(self.instructions):
            if i >= self.position and i < self.position + 10:  # Display 10 lines at a time
                wrapped_lines = self.wrap_text(line, max_width)
                for wrapped_line in wrapped_lines:
                    text = self.font.render(wrapped_line, True, self.text_color)
                    self.screen.blit(text, (100, y_offset))
                    y_offset += 40  # Add spacing between lines
                y_offset += 20  # Additional spacing between paragraphs

        pygame.display.flip()

    def scroll(self, direction):
        if direction == "up":
            self.position = max(self.position - 1, 0)
        elif direction == "down":
            self.position = min(self.position + 1, len(self.instructions) - 8)
