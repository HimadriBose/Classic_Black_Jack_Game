"""
Blackjack, also known as 21, is a popular casino card game where players compete against the dealer rather than each other. The objective is to have a hand value as close to 21 as possible without exceeding it.

### Basic Rules:
1. **Card Values:**
   - Number cards (2-10) are worth their face value.
   - Face cards (King, Queen, Jack) are each worth 10 points.
   - Aces can be worth either 1 or 11, depending on which value is more favorable for the hand.

2. **Starting the Game:**
   - Each player and the dealer are dealt two cards.
   - Players’ cards are dealt face up, while the dealer has one card face up (known as the "upcard") and one face down (the "hole card").

3. **Objective:**
   - The goal is to have a hand value of 21 or as close as possible without exceeding it ("busting").
   - Players aim to beat the dealer by having a higher hand value or by the dealer busting.

4. **Gameplay Actions:**
   - **Hit**: Request another card from the dealer. You can keep hitting as long as you don’t bust.
   - **Stand**: Keep your current hand and end your turn.
   - **Double Down**: Double your original bet, receive only one more card, and then you must stand.
   - **Split**: If the first two cards are of equal value (e.g., two 8s), you can split them into two separate hands, placing a second bet equal to the first.
   - **Surrender**: Some versions allow players to surrender after the first two cards, reclaiming half of their bet and forfeiting the round.

5. **Dealer's Turn:**
   - After the players finish their actions, the dealer reveals their hole card.
   - The dealer must hit until their hand totals at least 17 (in most versions of the game).
   - If the dealer exceeds 21, they bust, and all players who didn’t bust win.

6. **Blackjack:**
   - A "blackjack" is an Ace and a 10-point card on the initial deal. It typically pays out at 3:2 odds.
   - If both the player and dealer have blackjack, it’s a push (tie), and the bet is returned.

7. **Insurance:**
   - If the dealer’s upcard is an Ace, players can choose to place an insurance bet (usually half of the original bet). This pays 2:1 if the dealer has blackjack.

8. **Winning Conditions:**
   - Players win by having a higher hand total than the dealer without busting.
   - A player also wins if the dealer busts.
   - If the player busts or has a lower hand total than the dealer, they lose.

Blackjack blends strategy, probability, and luck, making it a favorite for many casino players.
"""
import random  #  used in shuffling of cards
# card class
class Card:
   def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank
   def __str__(self):
      return f'{self.rank['rank']} of {self.suit}'
 
# Deck Class
class Deck:
   def __init__(self):  
      self.cards = []
      self.suits = ['spades', 'clubs', 'hearts', 'diamonds']
      self.ranks = [
         {'rank':'A','value':11},
         {'rank':'2','value':2},
         {'rank':'3','value':3},
         {'rank':'4','value':4},
         {'rank':'5','value':5},
         {'rank':'6','value':6},
         {'rank':'7','value':7},
         {'rank':'8','value':8},
         {'rank':'9','value':9},
         {'rank':'10','value':10},
         {'rank':'J','value':10},
         {'rank':'Q','value':10},
         {'rank':'K','value':10}
      ]

      #populates the cards
      for suit in self.suits :
         for rank in self.ranks:
            self.cards.append(Card(suit,rank))

   # random module has a method 'shuffle' that suffeles the indices of the list element placing it in any random order
   def shuffle(self):
      if len(self.cards) > 1: 
         random.shuffle(self.cards)

   #picking cards from tha last of the deck of cards
   def deal(self, number :int)->list:
      cards_dealt = []
      for i in range(0,number):
            if len(self.cards) > 0:
               card = self.cards.pop()
               cards_dealt.append(card)  
      return cards_dealt

# Hand class
class Hand:
   def __init__(self, dealer = False):
      self.cards = []
      self.value = 0
      self.dealer = dealer

   # adds card to the players
   def add_card(self, card_list):
      # diff. b/w extend method & append method is that extend takes an iterable object as an argument while append takes a single variable and adds it to the class
      self.cards.extend(card_list)
   
   # calculates value of cards combined
   def calculate_value(self):
      self.value = 0
      has_ace = False
      for card in self.cards:
         self.value += int(card.rank['value'])

         if card.rank['rank'] == 'A':
            has_ace = True

      if has_ace and self.value >21:
         self.value -= 10

   # gets hands value
   def get_value(self):
      # to call method defined inside of a function , inside function we have to use self to reference it
      self.calculate_value()
      return self.value
   # this methods checks if you're a blackJack
   def is_black_jack(self):
      return self.get_value() == 21

   # shows the cards in your hand
   def display(self, show_all_dealer_card = False):
      whos_hand = 'Dealer\'s' if self.dealer else 'Player\'s'
      print(f'{whos_hand} hand:')
      for index,card in enumerate(self.cards):
         if index == 0 and self.dealer  and not show_all_dealer_card and not  self.is_black_jack():
            print('hidden')
         else:
            print(card)
      if not self.value :
         print('value:',self.get_value())
      print()

# Game class
class Game:
   def play(self):
      game_number = 0
      games_to_play = 0
      while games_to_play <= 0:
         try:
            games_to_play = int(input('How many games do you want to play:'))
         except :
            print('You must enter a number')

      while game_number < games_to_play :
         game_number += 1

         deck = Deck()
         deck.shuffle()

         player_hand = Hand()
         dealer_hand = Hand(True)

         for i in range(2):
            player_hand.add_card(deck.deal(1))
            dealer_hand.add_card(deck.deal(1))
         print()
         print('*'*30)
         print(f'Game {game_number} of {games_to_play}')
         print('*'*30)
         player_hand.display()
         dealer_hand.display()
         if self.check_winner(player_hand, dealer_hand):
            continue 
         choice = ''
         while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
            choice = input('please choose \'Hit\' or \'stand\':').lower()
            print()
            while choice not in['h', 's', 'hit', 'stand']:
               choice = input("please enter 'hit' or 'stand' or (H/S):").lower()
               print()
            if choice  in ['hit', 'h']:
               player_hand.add_card(deck.deal(1))
               player_hand.display()

         if self.check_winner(player_hand, dealer_hand):
            continue    

         player_hand_value = player_hand.get_value()
         dealer_hand_value = dealer_hand.get_value()

         while dealer_hand_value < 17:
            dealer_hand.add_card(deck.deal(1))
            dealer_hand_value = dealer_hand.get_value()
         
         dealer_hand.display(show_all_dealer_card=True)
         if self.check_winner(player_hand, dealer_hand):
            continue   
         
         print('Final Results:')
         print(f"Your's hand: {player_hand_value}")
         print(f"Dealer's hand: {dealer_hand_value}")

         self.check_winner(player_hand, dealer_hand, True)

      print('\n Thanks for Playing!!! 🥰')
      


   def check_winner(self, player_hand, dealer_hand, game_over = False):
      if not game_over:
         if player_hand.get_value() > 21:
            print('you\'re busted. Dealer wins 😭')
            return True
         elif dealer_hand.get_value() > 21:
            print('Dealer busted.you winwin 🥇')
            return True
         elif dealer_hand.is_black_jack() and player_hand.is_black_jack():
            print('Both players have BlackJack, it\'s a tie 😅')
            return True
         elif dealer_hand.is_black_jack():
            print('Dealer has BlackJack, Dealer wins 🥹')
            return True
         elif player_hand.is_black_jack():
            print('Player has BlackJack, Player wins 🥳')
            return True
      else:
         if player_hand.get_value() > dealer_hand.get_value():
            print('You win 🥶')
         elif dealer_hand.get_value() > player_hand.get_value():
            print('Dealer win 😱')
         else:
            print('Tie! 😅')
         return True
      return False 
   

game = Game()
game.play()