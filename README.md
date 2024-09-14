
# Blackjack Game

## Overview
This is a simple Blackjack game implemented in Python. The game simulates a classic card game between a player and a dealer, featuring key gameplay elements such as shuffling, dealing, hitting, and standing. The game determines winners based on standard Blackjack rules, including handling Blackjacks and busts.

## Features
- **Deck of Cards**: Implements a standard deck with suits and ranks.
- **Card Shuffling**: Uses randomization to shuffle the deck.
- **Gameplay**: Allows the player to hit or stand, and the dealer plays according to standard Blackjack rules.
- **Blackjack Detection**: Checks for Blackjacks for both player and dealer.
- **Game Rounds**: Supports playing multiple rounds in one session.
- **Game Status**: Displays the status of each round, including who wins or loses.

## Classes
- **Card**: Represents a single card with a suit and rank.
- **Deck**: Manages the deck of cards, including shuffling and dealing.
- **Hand**: Handles a player's or dealer's hand, including card addition and value calculation.
- **Game**: Manages the overall game flow, including dealing cards, handling player choices, and determining the winner.

## How to Play
1. **Start the Game**: Run the `Game` class to begin.
2. **Choose Number of Games**: Input how many rounds you want to play.
3. **Player Decisions**: During each round, choose to 'hit' (draw a card) or 'stand' (keep current hand).
4. **Dealer's Turn**: The dealer will draw cards according to the rules.
5. **Results**: The game will display the outcome, including who won or if there was a tie.

