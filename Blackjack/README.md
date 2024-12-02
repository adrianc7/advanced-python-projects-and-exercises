# Blackjack Game Program

**Author**: Adrian Chavez-Loya

This is an interactive Python program that simulates a classic Blackjack game. The player competes against a randomly selected dealer, aiming to outscore the dealer without exceeding a total of 21. The game follows traditional Blackjack rules and uses a custom `DeckOfCards` class for managing the deck.

---

## How to Play

1. **Objective**: Beat the dealer by getting a score closer to 21 without exceeding it.
2. **Gameplay**:
   - Both the player and the dealer are dealt two cards.
   - The player can choose to "hit" (draw a card) or "stay" (keep their hand).
   - The dealer draws until their score reaches 17 or higher.
3. **Winning**:
   - Scores are compared to determine the winner unless one of the participants busts (exceeds 21).
4. **Replay**: Players can choose to play multiple rounds or exit after each game.

---

## Features

- **Dynamic Dealer**: Randomly selects a humorous dealer name for each game.
- **Deck Management**: Utilizes the `DeckOfCards.py` file for:
  - Creating a standard 52-card deck.
  - Shuffling the deck.
  - Dealing cards dynamically during gameplay.
- **Score Calculation**: Aces adjust dynamically to avoid busting.
- **Replay Option**: Play multiple games in one session.

---

## Required Files

This program requires the following files to work:

1. **`BlackJackGame.py`**: Main game logic and player interaction.
2. **`DeckOfCards.py`**: A Python class used to manage the deck of cards.

**Note**: Both files must be located in the **same directory** for the import statement to work correctly.

---

## How to Run

1. **Install Python**: Ensure Python 3.x is installed on your system.
2. **Prepare the Files**:
   - Place both `BlackJackGame.py` and `DeckOfCards.py` in the same directory.
3. **Run the Game**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the files.
   - Execute the game with the command:
     ```bash
     python BlackJackGame.py
     ```
4. **Enjoy**: Follow the on-screen prompts to play the game.

---

## Sample Code Snippet

Here's how the import works in your `BlackJackGame.py` file:

```python
from DeckOfCards import DeckOfCards  # Import the DeckOfCards class to manage the deck

# Rest of your blackjack game code...
