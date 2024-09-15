# Number Guessing Game 🎲

A console-based number guessing game implemented in Python. Players guess a randomly generated number within a given range, with different difficulty levels affecting the number of attempts.

## Features

- **Difficulty Levels**: Choose between easy (10 attempts) and hard (5 attempts).
- **Random Number Generation**: The game generates a random number between 1 and 100 for the player to guess.
- **User Interaction**: Provides feedback on guesses, informs the player of remaining attempts, and reveals the number if they run out of attempts.
- **Replay Option**: Players can choose to play again or exit after each game.

## How It Works

1. **Introduction**: Displays a welcome message and the game logo.
2. **Difficulty Selection**: Prompts the player to choose between easy and hard difficulty levels.
3. **Guessing**:
    - **Easy Mode**: Player has 10 attempts to guess the number.
    - **Hard Mode**: Player has 5 attempts to guess the number.
    - Provides feedback for each guess, indicating if the guess is too high or too low.
    - Displays the correct number if the player runs out of attempts.
4. **Replay or Exit**: After a game, the player can choose to play again or exit.

## Code Overview

- **`clear()`**: Clears the console screen.
- **`menu()`**: Provides options to continue playing or exit the game.
- **`easy()`**: Handles the game logic for easy mode.
- **`hard()`**: Handles the game logic for hard mode.
- **`start()`**: Manages the difficulty choice and game initiation.
- **`intro()`**: Displays the introduction and starts the game.


## Future Improvements

- Add more difficulty levels or varying ranges.
- Implement a scoring system based on the number of attempts used.
- Enhance the user interface with graphical elements or a web-based version.

## License

This project is licensed under the MIT License.
