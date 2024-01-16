'''
Author: Kamron Cole
Originally created for assignment 8.1
Various functions to create and manipulate cards
'''
from random import randint

def make_card(rank, suit):
    '''
    Returns a tuple containing all information of a card.
    EX: Ace of Clubs
        (14, 'Clubs', 'Ace of Clubs', ' AC')
    '''
    # Error checking
    proper_suit = suit == 'Hearts' or suit == 'Spades' or suit == 'Clubs' or suit == 'Diamonds'
    if not proper_suit: # Makes sure a valid suit is entered
        raise ValueError('Invalid Suit: ' + str(suit))
    if rank < 2 or rank > 14: # Makes sure a valid rank is entered
        raise IndexError('Rank must be 2-14: ' + str(rank))

    identifier = str(rank) # Identifier used to create the name and shortand

    # Set identifier for face cards
    if rank == 14:
        identifier = 'Ace'
    if rank == 13:
        identifier = 'King'
    if rank == 12:
        identifier = 'Queen'
    if rank == 11:
        identifier = 'Jack'

    # Set the shorthand for a card
    shorthand = ' ' + identifier[0] + suit[0]
    if rank == 10: # 10 doesnt need the space
        shorthand = identifier + suit[0]

    name = identifier + ' of ' + suit
    return (rank, suit, name, shorthand)


def make_deck(shuffle_deck: bool = False):
    '''
    Makes a deck for 52 cards
    Starts with hearts, then diamonds, then spades, then clubs
    '''
    deck = []
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    r = 2
    s = 0
    for _ in range(52):
        if r > 14:
            r = 2
            s += 1
        if s > 3:
            s = 0
        deck.append(make_card(r, suits[s]))
        r += 1

    if shuffle_deck:
        return shuffle(deck)
    return deck


def shuffle(deck):
    '''
    Shuffles a list swaping each vlaue in the list with a random value someplace else in the list
    '''
    for index in range(0, len(deck)):
        random_index = randint(0, len(deck) - 1)
        swap_values_1 = deck[index]
        swap_values_2 = deck[random_index]

        deck[index] = swap_values_2
        deck[random_index] = swap_values_1
    return deck


def suit_key(card: tuple) -> int:
    '''
    The sort key used to sort cards by suit then rank
    '''
    sort_key = 0

    if card[1] == 'Clubs':
        sort_key = 100
    if card[1] == 'Diamonds':
        sort_key = 200
    if card[1] == 'Hearts':
        sort_key = 300
    if card[1] == 'Spades':
        sort_key = 400

    sort_key += card[0]

    return sort_key
