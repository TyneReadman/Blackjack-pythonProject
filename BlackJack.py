# Author: Tyne Readman
# Date Created: January 19, 2023
#
# TO BE IMPROVED:
#   -Impoper Nameing convections
#   -Concise and more readabul coments (In progesse as of Sept 20th 2024)
#   -Make leaderBord mode by adding a blue button to the left of 
#
# Description:
# This is a simple blackjack game that begins with a title screen featuring two buttons: "Play" and "Quit".
# - The "Play" button starts the game.
# - The "Quit" button exits the game.
#
# Gameplay Overview:
# - The user starts with $500 in cash and is prompted to place a bet at the start of each game.
# - The bet amount is deducted from their cash. If the user wins, they receive twice their bet; if they lose, they forfeit the bet.
#
# Game Mechanics:
# - The dealer deals two cards each to the user and themselves.
# - The user can see both of the dealer's cards and must choose an action based on that information.
#
# User Actions:
# 1. **Hit**: The user can choose to receive additional cards (one at a time) to improve their hand.
#    - The user can hit as many times as they want, but if their hand total exceeds 21, they bust and lose the game.
#
# 2. **Hold**: The user can choose to hold, ending their turn.
#    - After the user holds, if the dealer's hand value is less than 17, the dealer will continue to hit until their total reaches 17 or higher.
#    - If the dealer's hand exceeds 21, the dealer busts, and the user wins the game.
#
# End of Game:
# - If neither the user nor the dealer busts, the player with the highest hand value wins.
# - If both players have the same hand value, the result is a draw.
#
# Post-Game Options:
# - After each round, the user can choose to keep playing or return to the title screen.
# - From the title screen, they can press "Quit" to completely exit the game.

import random
import time
from graphics import *

game_mode = 1  # Tracks the current state of the game: 1 for title screen, 2 for active game, 0 for exit.
cash = 500     # The initial amount of money the user starts with, used for placing bets in the game.

import random

class Card:
    """Represents a playing card with a rank and suit."""
    
    def __init__(self, rank, suit):
        """Initializes a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        """Returns the string representation of the card."""
        return f"{self.rank}{self.suit}"

def pull_card(all_cards_in_play):
    """
    Randomly generates a new card, ensuring it's not already in play.
    
    Args:
        all_cards_in_play (list): A list of all cards currently in play.
        
    Returns:
        str: The newly generated card in string format.
    """
    rank_list = [2, 3, 4, 5, 6, 7, 8, 9, 'j', 'q', 'k', 'a']  # Possible card ranks
    suit_list = ['c', 's', 'h', 'd']  # Possible suits: clubs, spades, hearts, diamonds

    while True:
        # Pick random rank and suit
        rank = random.choice(rank_list)
        suit = random.choice(suit_list)
        new_card = Card(rank, suit)

        # Check if the card is already in play
        if str(new_card) not in all_cards_in_play:
            all_cards_in_play.append(str(new_card))
            print('New card drawn:', new_card, '| Cards in play:', all_cards_in_play)
            return str(new_card)  # Return the valid new card

def deal_hand(all_cards_in_play):
    """
    Deals a hand of two cards, ensuring no duplicates.
    
    Args:
        all_cards_in_play (list): A list of all cards currently in play.
        
    Returns:
        list: A list of two dealt cards.
    """
    cards_dealt = []

    while len(cards_dealt) < 2:
        new_card = pull_card(all_cards_in_play)
        cards_dealt.append(new_card)

    return cards_dealt

def find_hand_total(hand):
    """
    Calculate the total value of a hand in a game of blackjack.

    Args:
        hand (list): A list of cards, where each card is represented as a string (e.g., '7c', 'kh').

    Returns:
        int: The total point value of the hand.
    """
    total = 0
    num_of_ace = 0  # Track the number of Aces in the hand, as their value can be 1 or 11.
    
    # Dictionary mapping card ranks to their respective values in blackjack
    card_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'j': 10, 'q': 10, 'k': 10, 'a': 1  # Aces start with a value of 1
    }

    # Loop through each card in the hand
    for card in hand:
        value = str(card[0]).lower()  # Extract the card rank (first character) and make it lowercase
        if value == 'a':
            num_of_ace += 1  # Count the number of Aces for possible adjustment later
        total += card_values.get(value, 0)  # Add the card's value to the total

    # Adjust the value of Aces from 1 to 11 if it won't cause the hand to bust
    for _ in range(num_of_ace):
        if total + 10 <= 21:  # Only add 10 to turn an Ace from 1 to 11 if the total stays <= 21
            total += 10

    return total

def Hit_Delaer_Hand(hand, all_cards_in_play): 
    # This function hits the dealer's hand until the total reaches 17 or more
    # It recursively draws cards for the dealer and calculates the total each time

    total = find_hand_total(hand)  # Calculate the current total of the dealer's hand

    if total >= 17:  # If the total is 17 or more, the dealer stands
        return total
    else:
        hand.append(pull_card(all_cards_in_play))  # Otherwise, dealer draws a new card from the deck
        return Hit_Delaer_Hand(hand, all_cards_in_play)  # Recursive call with updated hand

def game_lobby(): 
    # This function handles the main game lobby screen, where players can start the game or quit
    # It creates buttons, handles user input, and manages screen rendering

    class button():
        # This class simplifies the creation and management of buttons
        # Buttons can be drawn on the screen and checked for user clicks

        def __init__(self, x, y, l, h, c):
            # Initialize button with position (x, y), dimensions (l, h), and color (c)
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            # This method draws the button on the screen based on its position and dimensions
            self.x1 = self.x - (self.l / 2)  # Left boundary of the button
            self.x2 = self.x + (self.l / 2)  # Right boundary of the button
            self.y1 = self.y - (self.h / 2)  # Top boundary of the button
            self.y2 = self.y + (self.h / 2)  # Bottom boundary of the button
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))  # Create a rectangle
            rect.setOutline("black")  # Set button outline color
            rect.setFill(self.c)  # Set button fill color
            rect.setWidth(5)  # Set button outline width
            rect.draw(win)  # Draw the button on the window

        def check_click(self, clicked): 
            # This method checks if the button was clicked by the user
            # Returns 1 if the button was clicked, otherwise 0
            x = clicked.getX()  # Get x-coordinate of the click
            y = clicked.getY()  # Get y-coordinate of the click

            # Check if the click is within the button boundaries
            if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
                return 1
            else:
                return 0

    class mod_text(): 
        # This class simplifies the creation and display of text on the screen
        def __init__(self, text, x, y, size):
            # Initialize text with content (text), position (x, y), and font size (size)
            self.text = text
            self.x = x
            self.y = y
            self.size = size

        def print_text(self):
            # This method prints the text at the specified location on the screen
            self.label = Text(Point(self.x, self.y), self.text)  # Create a text object
            self.label.setTextColor("black")  # Set the text color to black
            self.label.setSize(self.size)  # Set the font size
            self.label.draw(win)  # Draw the text on the window

    # This section initializes and draws the main game lobby screen background
    title = Image(Point(0, 0), "Blackjack_title.gif")  # Load the background image
    # In graphics.py, Point(0,0) is the center of the photo, so we calculate the exact center
    center_x = int(title.getWidth() / 2)  # Calculate the x-coordinate for the center of the image
    center_y = int(title.getHeight() / 2)  # Calculate the y-coordinate for the center of the image
    myPhoto = Image(Point(center_x, center_y), "Blackjack_title.gif")  # Create an image object centered in the window
    width = myPhoto.getWidth()  # Get the width of the image
    height = myPhoto.getHeight()  # Get the height of the image
    win = GraphWin("image gif", width, height)  # Create the window with the size of the image
    myPhoto.draw(win)  # Draw the image in the window

    # Create and draw the start button on the screen
    start = button(450, 450, 200, 120, "blue")  # Define button at (450,450) with width 200, height 120, and color blue
    start.draw_button()  # Draw the start button on the window
    start_text = mod_text("Start",450,450,35)  # Create text for the start button
    start_text.print_text()  # Draw the start button text

    # Create and draw the quit button on the screen
    quit = button(700, 450, 200, 120, "blue")  # Define quit button at (700,450) with similar specs to the start button
    quit.draw_button()  # Draw the quit button
    quit_text = mod_text("Quit", 700, 450, 35)  # Create text for the quit button
    quit_text.print_text()  # Draw the quit button text

    while True:  # Main loop to check for user input and button clicks
        clicked = win.getMouse()  # Wait for a mouse click
        if start.check_click(clicked) == 1:  # If the start button is clicked
            win.close()  # Close the window
            return "play"  # Return "play" to indicate game start
        elif quit.check_click(clicked) == 1:  # If the quit button is clicked
            win.close()  # Close the window
            return "quit"  # Return "quit" to indicate game exit

def make_bet(cash):
    # This function handles the betting process, asking the player how much they want to bet
    # It displays the current cash, takes user input for the bet, and ensures valid input

    class button():
        # This class simplifies creating and managing buttons for user interaction

        def __init__(self, x, y, l, h, c):
            # Initialize the button with position (x, y), dimensions (l, h), and color (c)
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            # This method draws the button on the screen using the specified position and dimensions
            self.x1 = self.x - (self.l / 2)  # Left boundary of the button
            self.x2 = self.x + (self.l / 2)  # Right boundary of the button
            self.y1 = self.y - (self.h / 2)  # Top boundary of the button
            self.y2 = self.y + (self.h / 2)  # Bottom boundary of the button
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))  # Create a rectangle for the button
            rect.setOutline("black")  # Set button outline color
            rect.setFill(self.c)  # Set button fill color
            rect.setWidth(5)  # Set button outline width
            rect.draw(win)  # Draw the button on the window

        def check_click(self): 
            # This method checks if the button was clicked by the user
            # Returns 1 if the button was clicked, otherwise 0
            clicked = win.getMouse()  # Get the mouse click event
            x = clicked.getX()  # Get the x-coordinate of the click
            y = clicked.getY()  # Get the y-coordinate of the click

            # Check if the click is within the button's boundaries
            if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
                return 1
            else:
                return 0

    # This section initializes the betting screen with the blackjack table background
    title = Image(Point(0, 0), "Black_Jack_Table.gif")  # Load the blackjack table background image
    # The center of the image is placed at (0, 0), so we calculate the center
    center_x = int(title.getWidth() / 2)  # Calculate the x-coordinate for the image's center
    center_y = int(title.getHeight() / 2)  # Calculate the y-coordinate for the image's center
    myPhoto = Image(Point(center_x, center_y), "Black_Jack_Table.gif")  # Create the image object centered in the window
    win = GraphWin("image gif", 500, 500)  # Create the window for the betting screen with fixed dimensions
    myPhoto.draw(win)  # Draw the image in the window

    # Display a prompt asking the user how much they want to bet and their current cash balance
    Text(Point(250, 150), "How much would you like to bet?: ").draw(win)  # Draw bet prompt text
    Text(Point(250, 450), "Cash: " + str(cash)).draw(win)  # Draw the user's current cash balance
    make_bet = Entry(Point(250, 200), 5)  # Create an input box for the bet amount, allowing up to 5 characters
    make_bet.setText(10)  # Set a default bet value of 10
    make_bet.draw(win)  # Draw the input box on the window

    # Create and draw a green button for submitting the bet amount
    bet_button = button(250, 275, 70, 50, "green")  # Create a bet button at (250,275) with width 70, height 50, and color green
    bet_button.draw_button()  # Draw the bet button on the window

    # Main loop for handling user input and ensuring valid bets
    while True:
        while True:
            try:
                while True:
                    if bet_button.check_click() == 1:  # If the bet button is clicked
                        bet = int(make_bet.getText())  # Retrieve the bet amount from the input box
                        if bet < 0 or bet > cash:  # Ensure the bet is between 0 and the player's available cash
                            t = Text(Point(250, 350), "Number must be between 0-" + str(cash))  # Show an error message if the bet is invalid
                            t.draw(win)  # Draw the error message on the window
                            time.sleep(1.5)  # Wait 1.5 seconds
                            t.undraw()  # Remove the error message
                            continue  # Recheck the input
                        break  # Valid bet is entered, break out of the loop
                break  # Exit the try block
            except ValueError:  # Catch invalid input (non-integer values)
                t = Text(Point(250, 350), 'Must be a whole number')  # Show an error message if the input is not a valid number
                t.draw(win)  # Draw the error message
                time.sleep(1.5)  # Wait 1.5 seconds
                t.undraw()  # Remove the error message
                continue  # Recheck the input
        win.close()  # Close the window once a valid bet is placed
        return bet  # Return the valid bet amount


def play_game(cash, bet, all_cards_in_play):
    # This function simulates a round of blackjack, allowing the user to play and interact with the game UI
    
    class button():
        # This class simplifies creating and managing buttons for user interaction

        def __init__(self, x, y, l, h, c):
            # Initialize the button with position (x, y), dimensions (l, h), and color (c)
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            # Draw the button on the screen using the specified position and dimensions
            self.x1 = self.x - (self.l / 2)  # Left boundary of the button
            self.x2 = self.x + (self.l / 2)  # Right boundary of the button
            self.y1 = self.y - (self.h / 2)  # Top boundary of the button
            self.y2 = self.y + (self.h / 2)  # Bottom boundary of the button
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))  # Create a rectangle for the button
            rect.setOutline("black")  # Set button outline color
            rect.setFill(self.c)  # Set button fill color
            rect.setWidth(5)  # Set button outline width
            rect.draw(win)  # Draw the button on the window

        def check_click(self, spot_clicked):
            # This method checks if the button was clicked by the user based on the mouse position
            x = spot_clicked.getX()  # Get the x-coordinate of the click
            y = spot_clicked.getY()  # Get the y-coordinate of the click

            # Check if the click is within the button's boundaries
            if x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2:
                return 1
            else:
                return 0

    def print_image(pic, mod_x, mod_y):
        # This function displays an image on the screen, with optional position adjustments (mod_x, mod_y)
        title = Image(Point(0, 0), pic + ".gif")  # Load the image
        center_x = int(title.getWidth() / 2) + mod_x  # Calculate the adjusted x-coordinate for centering
        center_y = int(title.getHeight() / 2) + mod_y  # Calculate the adjusted y-coordinate for centering
        myPhoto = Image(Point(center_x, center_y), pic + ".gif")  # Create the image object centered in the window
        myPhoto.draw(win)  # Draw the image on the window

    class mod_text():
        # This class simplifies creating and displaying text elements on the screen

        def __init__(self, text, x, y, size):
            # Initialize the text object with content, position (x, y), and font size
            self.text = text
            self.x = x
            self.y = y
            self.size = size

        def print_text(self):
            # Display the text on the screen
            self.label = Text(Point(self.x, self.y), self.text)  # Create the text object
            self.label.setTextColor("black")  # Set text color to black
            self.label.setSize(self.size)  # Set text size
            self.label.draw(win)  # Draw the text on the window

        def del_text(self):
            # Remove the text from the screen
            self.label.undraw()

    # Initialize the game screen with a background
    win = GraphWin("Table", 1400, 700)  # Create a window with specific dimensions for the game
    print_image("Black_Jack_Table", 0, 0)  # Load and display the blackjack table background

    # Deal the user's hand and the dealer's hand
    hand = deal_hand(all_cards_in_play)  # Deal cards to the user
    delaer_hand = deal_hand(all_cards_in_play)  # Deal cards to the dealer

    while True:
        # Main game loop for user actions (hit or hold) until they either hold or their total reaches 21 or more

        user_total = find_hand_total(hand)  # Calculate the user's hand total
        delaer_total = find_hand_total(delaer_hand)  # Calculate the dealer's hand total

        # Display the user's and dealer's cards
        for i in range(len(hand)):
            print_image(hand[i], 80 + 86 + (i * 180), 450)  # Display each card in the user's hand
        for i in range(len(delaer_hand)):
            print_image(delaer_hand[i], 80 + 86 + (i * 180), 50)  # Display each card in the dealer's hand

        # Display the user's total, dealer's total, cash, and bet amount
        total = mod_text("Hand Total: " + str(user_total), 250, 400, 20)  # Display the user's hand total
        total.print_text()
        d_total = mod_text("Dealer Total: " + str(delaer_total), 257, 350, 20)  # Display the dealer's hand total
        d_total.print_text()
        user_cash = mod_text("Cash: " + str(cash), 200, 20, 15)  # Display the user's current cash
        user_cash.print_text()
        bet_amount = mod_text("Bet: " + str(bet), 320, 20, 15)  # Display the current bet amount
        bet_amount.print_text()

        # End game early if user reaches or exceeds 21
        if user_total >= 21:
            break

        # Create and display the "Hit" and "Hold" buttons
        hit = button(630, 420, 120, 40, "green")  # Create the hit button
        hit.draw_button()  # Draw the hit button
        hit_text = mod_text("Hit", 630, 420, 15)  # Label the hit button
        hit_text.print_text()

        hold = button(770, 420, 120, 40, "green")  # Create the hold button
        hold.draw_button()  # Draw the hold button
        hold_text = mod_text("Hold", 770, 420, 15)  # Label the hold button
        hold_text.print_text()

        clicked = win.getMouse()  # Wait for the user to click somewhere

        if hit.check_click(clicked) == 1:
            # If the hit button was clicked, add a card to the user's hand
            hand.append(pull_card(all_cards_in_play))
        if hold.check_click(clicked) == 1:
            # If the hold button was clicked, end the game loop
            break

        # Remove previous totals from the screen to update them later
        total.del_text()
        d_total.del_text()

    d_total.del_text()  # Remove the dealer's total to update it later
    Hit_Delaer_Hand(delaer_hand, all_cards_in_play)  # Let the dealer hit until they reach 17 or more
    delaer_total = find_hand_total(delaer_hand)  # Update the dealer's hand total
    d_total = mod_text("Dealer Total: " + str(delaer_total), 257, 350, 20)  # Display the updated dealer total
    d_total.print_text()

    # Display the dealer's updated hand
    for i in range(len(delaer_hand)):
        print_image(delaer_hand[i], 80 + 86 + (i * 180), 50)

        # Determine the outcome of the game based on the final totals
    if user_total > 21 and delaer_total > 21:
        outcome = "Tie"
    elif user_total == delaer_total:
        outcome = "Tie"
    elif user_total > 21:
        outcome = "Lose"
    elif delaer_total > 21 or user_total == 21 or user_total > delaer_total:
        outcome = "Win"
    else:
        outcome = "Lose"

    print(outcome)


    # Display the outcome of the game and create buttons for "Play Again" and "Quit"
    end_game = button(700, 350, 150, 75, "red")  # Create a rectangle to show the game outcome
    end_game.draw_button()
    end = mod_text(outcome, 700, 350, 30)  # Display the game outcome (win, lose, tie)
    end.print_text()

    # Create the "Play Again" and "Quit" buttons
    play_again_button = button(100, 100, 100, 100, "red")
    play_again_button.draw_button()
    play_again_text = mod_text("Play Again?", 100, 100, 13)
    play_again_text.print_text()

    quit_button = button(100, 220, 100, 100, "red")
    quit_button.draw_button()
    quit_text = mod_text("Quit?",100,220,13)
    quit_text.print_text()

    print("ALL CARDS:", all_cards_in_play)

    while True:  # Keep running until a button is clicked
        clicked = win.getMouse()  # Wait for a mouse click
        if play_again_button.check_click(clicked) == 1:  # Check if "Play Again" button is clicked
            win.close()
            return outcome  # Return the outcome of the game
        if quit_button.check_click(clicked) == 1:  # Check if "Quit" button is clicked
            win.close()
            return 'quit'  # Return 'quit' to exit the game

while True:
    if game_mode == 1:  # Lobby: allows player to navigate to other game modes
        button_pressed = game_lobby()  # Display the lobby and get the button pressed
        if button_pressed == "play":  # If "Play" button is pressed
            game_mode = 2  # Switch to game mode 2
        elif button_pressed == 'quit':  # If "Quit" button is pressed
            break  # Exit the main game loop

    if game_mode == 2:  # Game mode 2: gameplay phase
        all_cards_in_play = []  # Reset the list of cards in play for each game
        bet = make_bet(cash)  # Prompt the player to make a bet
        int(bet)  # Convert bet to an integer
        cash -= int(bet)  # Deduct the bet amount from cash
        outcome = play_game(cash, bet, all_cards_in_play)  # Play the game and get the outcome
        
        # Update cash based on the game outcome
        if outcome == "Win":  # If the player wins
            cash += int(bet) * 2  # Double the bet amount is added to cash
        elif outcome == "Tie":  # If the game is a tie
            cash += int(bet)  # Refund the bet amount to cash
        elif outcome == "quit":  # If the player decides to quit
            game_mode = 1  # Return to the lobby
