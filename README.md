# Hangman-Game

This is a simple command-line implementation of the classic Hangman word guessing game. The game selects a random word and the player has to figure out the word by guessing letters. For each wrong guess, a part of the hangman figure is drawn. The game continues until the player either guesses the word or the entire hangman figure is drawn.

# Features

- The game selects a random word from a predefined list.
- The player can guess one letter at a time.
- For each incorrect guess, the player loses a life, and a part of the hangman figure is drawn.
- The game provides feedback on the player's guesses, displaying the current state of the word (with underscores for letters that haven't been guessed.
- The player wins when they correctly guess all letters in the word.
- The game ends when the player runs out of lives.

# Files

- hangman.py: The main game script that implements the game logic.
- hangman_art.py: Contains ASCII art of the hangman stages and the game logo.
- hangman_words.py: Constains a list of words to be selected for the game.
