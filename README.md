# Blackjack Game

Welcome to the Blackjack game! This is a simple Python-based blackjack game that you can run on your local machine.

## Prerequisites

To run the program, you will need:

- Python 3.11.9 installed on your system.

## Installation and Running the Game

1. **Download all files:**
   - Clone this repository or download all the files to the same folder on your local machine (A zip file can be found in the repository).
2. **How to run the Game:**
   - To run the game all you need to is run the file titled BlackJack.py

## Author
- **Name**: Tyne Readman
- **Date Created**: January 19, 2023

## Improvements To Be Made:
- Fix improper naming conventions for variables, classes, and functions.
- Make comments more concise and readable (Work in progress as of Sept 20th, 2024).
- Implement a leaderboard mode by adding a blue button to the left of the "Start" button on the title screen.
- Add a "Quit Game" button to the betting screen for better user control.

## Description
This is a simple blackjack game that begins with a title screen featuring two buttons: "Play" and "Quit".
- The "Play" button starts the game.
- The "Quit" button exits the game.

### Gameplay Overview
- The user starts with $500 in cash and is prompted to place a bet at the start of each game.
- The bet amount is deducted from their cash. If the user wins, they receive twice their bet; if they lose, they forfeit the bet.

### Game Mechanics
- The dealer deals two cards each to the user and themselves.
- The user can see both of the dealer's cards and must choose an action based on that information.

### User Actions
1. **Hit**: The user can choose to receive additional cards (one at a time) to improve their hand.
   - The user can hit as many times as they want, but if their hand total exceeds 21, they bust and lose the game.
   
2. **Hold**: The user can choose to hold, ending their turn.
   - After the user holds, if the dealer's hand value is less than 17, the dealer will continue to hit until their total reaches 17 or higher.
   - If the dealer's hand exceeds 21, the dealer busts, and the user wins the game.

### End of Game
- If neither the user nor the dealer busts, the player with the highest hand value wins.
- If both players have the same hand value, the result is a draw.

### Post-Game Options
- After each round, the user can choose to keep playing or return to the title screen.
- From the title screen, they can press "Quit" to completely exit the game.
