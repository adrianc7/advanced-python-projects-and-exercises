"""
### Blackjack Game Program
### By: Adrian Chavez-Loya

This program simulates a Blackjack game where the player competes against a randomly assigned dealer. The game uses a deck of cards and calculates scores for both the player and dealer based on traditional Blackjack rules. The objective is for the player to outscore the dealer without going over 21.

#### Key Components:
1. **Deck Management**: Utilizes the `DeckOfCards` class to create, shuffle, and deal cards.
2. **Score Calculation**: Calculates the score of each hand, accounting for Aces as either 1 or 11 to prevent busting.
3. **Gameplay Flow**:
   - The player is given the option to "hit" (draw more cards) or "stay" (keep their current hand) until they reach 21 or decide to stop.
   - The dealer draws cards until reaching a score of 17 or higher.
4. **Winner Determination**: Compares the player’s and dealer’s scores to declare a winner, with additional checks for busting.
5. **Replay Option**: Allows the player to choose whether to play another round or end the game.

#### Outputs:
- **Dealer and Player Cards**: Displays the cards each participant holds, with the dealer’s first card hidden initially.
- **Score Display**: Shows the current score of the player and the dealer after each action.
- **Game Result**: Announces the winner of each round based on scores, with personalized messages depending on the outcome.
- **Play Again Prompt**: Offers the player an option to play another round or conclude the game with a farewell message.

This Blackjack game is a fun and interactive way to explore conditional logic, loops, and object-oriented programming in Python. It also provides a practical example of score calculation and decision-making in a game setting.
"""



from DeckOfCards import DeckOfCards  # Import the DeckOfCards class to manage the deck

import random  # Random module to shuffle deck and assign dealer names

def calculate_score(cards):
    score = 0  # Initial score starts at 0
    ace_count = 0  # Keep track of Aces to adjust their value as needed
    for card in cards:
        score += card.val  # Add each card's value to the total score
        if card.face == "Ace":
            ace_count += 1  # Count Aces for possible adjustment
    # If the score goes over 21, treat Aces as 1 instead of 11
    while score > 21 and ace_count:
        score -= 10  # Subtract 10 from the score for each Ace if necessary
        ace_count -= 1  # Decrease the Ace count
    return score  # Return the final calculated score

def display_cards(cards, hidden=False):
    if hidden:
        print("Hidden card, ", cards[1])  # Hide the first card if needed (for the dealer's first card)
    else:
        for card in cards:
            print(card)  # Show all cards in the hand

def check_winner(user_score, dealer_score, dealer_name):
    if user_score > 21:
        print(f"You busted! {dealer_name} wins this one.")  # Player busts, dealer wins
    elif dealer_score > 21:
        print(f"{dealer_name} busted! You win!")  # Dealer busts, player wins
    elif user_score > dealer_score:
        print(f"You outscored {dealer_name}! Victory!")  # Player wins if score is higher
    elif dealer_score > user_score:
        print(f"{dealer_name} wins! Better luck next time.")  # Dealer wins with higher score
    else:
        print(f"It's a tie with {dealer_name}. Close one!")  # A tie if scores match

def blackjack_game():
    print("Welcome to Black Jack MGM Grand!")  # Intro message

    dealer_names = ["Carl Skank", "Brad Pitstop", 
    "Sylvester Stillalone", "Scarlett Yo-handsome", "Vin Dieseled", 
    "Chris Pratfall", "Dwayne 'The Stone' Johnson", "Tom Crankz",
    "Matt Blahmon", "Leo DiCramprio", "Morgan Freezing", 
    "Keanu Grieves", "Justin Timberfake", "Nick Flurry", "Harrison 'Old' Ford", "Robert Downhill Jr.", 
    "Chris Hemsworst", "Jack Blackout", "Chuck 'The Sneeze' Norris"]  # List of dealer names
    
    deck = DeckOfCards()  # Initialize the deck of cards once

    while True:
        dealer_name = random.choice(dealer_names)  # Randomly pick a dealer for the game
        print(f"\nYour dealer this game is {dealer_name}. Try to beat {dealer_name}!")  # Announce the dealer
        
        # Show the deck before and after shuffling
        print("\nDeck before shuffle:")
        deck.print_deck()  # Show all the cards before shuffling
        deck.shuffle_deck()  # Shuffle the deck (reuse the same deck each time)
        print("\nDeck after shuffle:")
        deck.print_deck()  # Show the shuffled deck

        # Deal two cards to both the player and the dealer
        user_cards = [deck.get_card(), deck.get_card()]
        dealer_cards = [deck.get_card(), deck.get_card()]

        # Display user's cards and calculate their score
        print("\nYour cards:")
        display_cards(user_cards)  # Show the user's cards
        user_score = calculate_score(user_cards)  # Calculate user's score
        print("Your score:", user_score)

        # Let the player hit (get more cards) or stay
        while user_score < 21:  # Continue if player's score is under 21
            hit = input("Would you like a hit? (y/n): ").lower()
            if hit == 'y':
                new_card = deck.get_card()  # Get a new card
                user_cards.append(new_card)  # Add it to player's hand
                print("You drew:", new_card)  # Show the new card
                user_score = calculate_score(user_cards)  # Update player's score
                print("Your new score:", user_score)
            else:
                break  # Player chooses to stay

        # Reveal the dealer's cards if player hasn't busted
        if user_score <= 21:
            print(f"\n{dealer_name}'s cards:")
            display_cards(dealer_cards, hidden=False)  # Show all of the dealer's cards
            dealer_score = calculate_score(dealer_cards)  # Calculate the dealer's score
            print(f"{dealer_name}'s score:", dealer_score)

            # Dealer keeps drawing if their score is below 17
            while dealer_score < 17:
                new_card = deck.get_card()  # Dealer draws a new card
                dealer_cards.append(new_card)  # Add it to dealer's hand
                print(f"{dealer_name} drew:", new_card)  # Show the new card
                dealer_score = calculate_score(dealer_cards)  # Update dealer's score
                print(f"{dealer_name}'s new score:", dealer_score)

            # Determine who wins
            check_winner(user_score, dealer_score, dealer_name)
        else:
            print(f"You busted! {dealer_name} wins!")  # Player busts, dealer wins automatically

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':  # If player says 'n', end the game
            print("Game Over, WOMP WOMP")  # End message
            break

if __name__ == "__main__":
    blackjack_game()  # Start the game
