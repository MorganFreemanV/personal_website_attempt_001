#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self) -> None:
        print('Creating deck...')
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
        print(self.allcards)
        

    def shuffle(self):
        print('Shuffling deck...')
        shuffle(self.allcards)
    
    def split_cards(self):
        return (self.allcards[:26],self.allcards[26:])
    
class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, cards) -> None:
        self.cards = cards
    
    def __str__(self):
        return 'Contains {} cards.'.format(len(self.cards))
    
    def addcard(self, addedcards):
        self.cards.extend(addedcards)
    
    def removecard(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.removecard()
        print('{} has played {}'.format(self.name, drawn_card))
        print('\n')
        return drawn_card
    
    def remove_war_cards(self):
        warcards = []
        for x in range(3):
            warcards.append(self.hand.removecard())
        return warcards
    
    def still_has_cards(self):
        '''
        Return True if player still has cards left
        '''
        return (len(self.hand.cards)) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Use the 3 classes along with some logic to play a game of war!
d = Deck()
d.shuffle()
half1, half2 = d.split_cards()
""" print(half1)
print()
print(half2) """

comp = Player('Computer', Hand(half1))
player = input('What is your name?')
player = Player(player, Hand(half2))

total_rounds = 0
war_count = 0

while player.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print('Time for new round!')
    print('Here are the current standings.')
    print(player.name + ' has the count: ' + str(len(player.hand.cards)))