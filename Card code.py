import random
from Blackjack import Hit_Delaer_Hand
from graphics import *

game_mode = 1
cash = 500
all_cards_in_play = []

class Card:
    def __init__(self, rank, suit):
        """Initializes the card with a rank and suit."""
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        """Converts the card into a string representation."""
        return str(self.rank) + str(self.suit)

def pull_card():
    """
    Generates a random card from the rank and suit lists and returns it
    as a string after creating a Card object.
    """
    rankList = [2, 3, 4, 5, 6, 7, 8, 9, "j", "q", "k", "a"]
    suitList = ["c", "s", "h", "d"]

    rank = random.choice(rankList)  # Choose a random rank
    suit = random.choice(suitList)  # Choose a random suit

    new_card = Card(rank, suit)  # Creates a Card object with the chosen rank and suit
    return str(new_card)  # Returns the string representation of the card

def deal_hand():
    """
    Deals a hand of two cards to the user, ensuring no duplicate cards are in the hand.
    Returns a list of the cards dealt.
    """
    cardsDelt = []

    while len(cardsDelt) < 2:  # Stop once the hand contains two cards
        new_card = pull_card()  # Get a new card
        if new_card not in cardsDelt:  # Check if the card is unique
            cardsDelt.append(new_card)  # Add the new card to the hand

    return cardsDelt

def find_hand_total(hand):
    """
    Takes a hand of cards and calculates the total value.
    Face cards ('j', 'q', 'k') are worth 10, and aces ('a') are worth 1.
    """
    total = 0
    for card in hand:
        value = str(card[0])  # Get the rank of the card
        if value == 'a':
            total += 1
        elif value in ['j', 'q', 'k']:
            total += 10
        else:
            total += int(value)  # Convert numeric rank to its integer value

    return total

def hit_dealer_hand(hand):
    """
    Recursively adds cards to the dealer's hand until the total value is 17 or higher.
    Returns the final total of the dealer's hand.
    """
    total = find_hand_total(hand)

    if total >= 17:
        return total
    else:
        hand.append(pull_card())  # Dealer takes another card
        return hit_dealer_hand(hand)

def game_lobby():
    class button():
        def __init__(self, x, y, l, h, c):
            """Initializes the button with coordinates, dimensions, and color."""
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            """Calculates the button's coordinates and draws it on the screen."""
            self.x1 = self.x - (self.l / 2)  # Left boundary of the button
            self.x2 = self.x + (self.l / 2)  # Right boundary of the button
            self.y1 = self.y - (self.h / 2)  # Top boundary of the button
            self.y2 = self.y + (self.h / 2)  # Bottom boundary of the button
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
            rect.setOutline("black")
            rect.setFill(self.c)
            rect.setWidth(5)
            rect.draw(win)

        def check_click(self):
            """Checks if a mouse click is within the button's boundaries."""
            clicked = win.getMouse()  # Waits for a mouse click
            x = clicked.getX()
            y = clicked.getY()

            # Check if the click is within the button's boundaries
            if self.x1 < x < self.x2 and self.y1 < y < self.y2:
                return 1
            else:
                return 0

    title = Image(Point(0, 0), "Blackjack_title.gif")

    # In graphics.py, Point(0,0) is the center, so adjust based on image dimensions
    center_x = int(title.getWidth() / 2)
    center_y = int(title.getHeight() / 2)

    myPhoto = Image(Point(center_x, center_y), "Blackjack_title.gif")

    width = myPhoto.getWidth()  # Get the width of the image
    height = myPhoto.getHeight()  # Get the height of the image

    win = GraphWin("Blackjack Game", width, height)  # Create a window for the game

    myPhoto.draw(win)  # Display the title image in the window

    start = button(450, 450, 200, 120, "blue")  # Create a start button
    start.draw_button()  # Draw the start button

    # Wait until the start button is clicked, then close the window and return "play"
    while True:
        if start.check_click() == 1:
            win.close()
            return "play"

def make_bet(cash):
    class button():
        def __init__(self, x, y, l, h, c):
            """Initializes the button with coordinates, dimensions, and color."""
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            """Calculates the button's coordinates and draws it on the screen."""
            self.x1 = self.x - (self.l / 2)  # Left boundary of the button
            self.x2 = self.x + (self.l / 2)  # Right boundary of the button
            self.y1 = self.y - (self.h / 2)  # Top boundary of the button
            self.y2 = self.y + (self.h / 2)  # Bottom boundary of the button
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
            rect.setOutline("black")
            rect.setFill(self.c)
            rect.setWidth(5)
            rect.draw(win)

        def check_click(self):
            """Checks if a mouse click is within the button's boundaries."""
            clicked = win.getMouse()  # Waits for a mouse click
            x = clicked.getX()
            y = clicked.getY()

            # Check if the click is within the button's boundaries
            if self.x1 < x < self.x2 and self.y1 < y < self.y2:
                return 1
            else:
                return 0

    title = Image(Point(0, 0), "Black_Jack_Table.gif")

    # In graphics.py, Point(0,0) is the center, so adjust based on image dimensions
    center_x = int(title.getWidth() / 2)
    center_y = int(title.getHeight() / 2)

    myPhoto = Image(Point(center_x, center_y), "Black_Jack_Table.gif")

    win = GraphWin("Place Your Bet", 500, 500)  # Create a window for the betting screen

    myPhoto.draw(win)  # Display the table image in the window

    # Display text for bet instructions and current cash
    Text(Point(250, 150), "How much would you like to bet?: ").draw(win)
    Text(Point(250, 450), "Cash: " + str(cash)).draw(win)

    bet = Entry(Point(250, 200), 5)  # Create an input field for the bet
    bet.draw(win)

    bet_button = button(250, 275, 70, 50, "green")  # Create a bet confirmation button
    bet_button.draw_button()  # Draw the bet button

    # Wait for the bet button to be clicked, then close the window and return the bet
    while True:
        if bet_button.check_click() == 1:
            win.close()
            return bet.getText()  # Return the entered bet amount


def play_game(cash, bet):

    class button:
        def __init__(self, x, y, l, h, c):
            """Initializes button with coordinates, dimensions, and color."""
            self.x = x
            self.y = y
            self.l = l
            self.h = h
            self.c = c

        def draw_button(self):
            """Calculates button's coordinates and draws it."""
            self.x1 = self.x - (self.l / 2)  # Left boundary
            self.x2 = self.x + (self.l / 2)  # Right boundary
            self.y1 = self.y - (self.h / 2)  # Top boundary
            self.y2 = self.y + (self.h / 2)  # Bottom boundary
            rect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
            rect.setOutline("black")
            rect.setFill(self.c)
            rect.setWidth(5)
            rect.draw(win)

        def check_click(self, spot_clicked):
            """Checks if a mouse click is within the button's boundaries."""
            x = spot_clicked.getX()
            y = spot_clicked.getY()

            # Return 1 if the click is within the button's boundaries
            if self.x1 < x < self.x2 and self.y1 < y < self.y2:
                return 1
            else:
                return 0

    def print_image(pic, mod_x, mod_y):
        """Draws an image at the specified position on the screen."""
        title = Image(Point(0, 0), pic + ".gif")

        # Adjust the image position using calculated offsets
        center_x = int(title.getWidth() / 2) + mod_x
        center_y = int(title.getHeight() / 2) + mod_y

        myPhoto = Image(Point(center_x, center_y), pic + ".gif")
        myPhoto.draw(win)

    class mod_text:
        def __init__(self, text, x, y, size):
            """Initializes modifiable text at a given position and size."""
            self.text = text
            self.x = x
            self.y = y
            self.size = size

        def print_text(self):
            """Prints the text on the screen."""
            self.label = Text(Point(self.x, self.y), self.text)
            self.label.setTextColor("black")
            self.label.setSize(self.size)
            self.label.draw(win)

        def del_text(self):
            """Deletes the text from the screen."""
            self.label.undraw()

    win = GraphWin("Table", 1400, 700)  # Create a window for the game table
    print_image("Black_Jack_Table", 0, 0)  # Display the table image

    hand = deal_hand()  # Deal player hand
    delaer_hand = deal_hand()  # Deal dealer hand

    while True:
        user_total = find_hand_total(hand)
        delaer_total = find_hand_total(delaer_hand)

        print("hand", hand)
        print("user_total", user_total)
        print("delaer_hand", delaer_hand)
        print("delaer_total", delaer_total)

        # Display player and dealer cards
        for i in range(len(hand)):
            print_image(hand[i], 80 + 86 + (i * 180), 450)

        for i in range(len(delaer_hand)):
            print_image(delaer_hand[i], 80 + 86 + (i * 180), 50)

        # Display game information (hand total, dealer total, cash, bet)
        total = mod_text("Hand Total: " + str(user_total), 250, 400, 20)
        total.print_text()
        d_total = mod_text("Dealer Total: " + str(delaer_total), 257, 350, 20)
        d_total.print_text()
        user_cash = mod_text("Cash: " + str(cash), 200, 20, 15)
        user_cash.print_text()
        bet_amount = mod_text("Bet: " + str(bet), 500, 20, 15)
        bet_amount.print_text()

        if user_total > 21:  # If player busts, end loop
            break
        if user_total == 21:  # If player hits blackjack, end loop
            break

        # Create hit and hold buttons
        hit = button(630, 420, 120, 40, "green")
        hit.draw_button()
        hold = button(770, 420, 120, 40, "green")
        hold.draw_button()

        clicked = win.getMouse()  # Wait for user input

        if hit.check_click(clicked) == 1:  # If hit is clicked, pull another card
            hand.append(pull_card())

        if hold.check_click(clicked) == 1:  # If hold is clicked, end player's turn
            break

        total.del_text()  # Remove old hand total
        d_total.del_text()  # Remove old dealer total

    d_total.del_text()  # Clear dealer total after player decision
    Hit_Delaer_Hand(delaer_hand)  # Dealer's turn to hit 
    delaer_total = find_hand_total(delaer_hand)

    # Reprint dealer's full hand
    for i in range(len(delaer_hand)):
        print_image(delaer_hand[i], 80 + 86 + (i * 180), 50)

    end_game = button(700, 350, 150, 75, "red")  # Create end game button
    end_game.draw_button()

    # Determine game outcome
    if user_total > 21 and delaer_total > 21:
        print("Tie")
        outcome = "Tie"
    elif user_total > 21:
        print("Lose")
        outcome = "Lose"
    elif delaer_total > 21 or user_total == 21 or user_total > delaer_total:
        print("Win")
        outcome = "Win"
    elif user_total == delaer_total:
        print("Tie")
        outcome = "Tie"
    else:
        print("Lose")
        outcome = "Lose"


    end = mod_text(outcome, 700, 350, 30)  # Display the outcome
    end.print_text()

    ok = button(100, 100, 100, 100, "blue")  # Create OK button to close game
    ok.draw_button()

    # Wait for OK button click to close the window
    while True:
        if ok.check_click(win.getMouse()) == 1:
            win.close()
            return 2

# Main game loop
while True:
    if game_mode == 1:
        # If in game mode 1, display game lobby and wait for user to click "play"
        print("Mode 1")
        if game_lobby() == "play":
            game_mode = 2  # Switch to betting mode

    if game_mode == 2:
        # Player makes a bet, then switch to play mode
        print("Mode 2")
        bet = make_bet(cash)
        game_mode = play_game(cash, bet)  # Play the game and update game mode based on outcome

    if game_mode == 3:
        # Placeholder for post-game or error handling
        print("Mode 3")
        break  # End the loop or replace this with appropriate game-ending logic
