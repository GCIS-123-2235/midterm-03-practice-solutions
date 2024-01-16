import cards

"""
Question 5 (List Comprehension) MEDIUM

Description:
Given a deck of cards, use list comprehension to return a 2D list whose rows are a list of cards all of the same suit.
Because a deck of cards has 52 cards and 4 suits, the result 2D list should have 4 rows with 13 cards each (of the same suit). Each row should be sorted from rank 2 to 14 (hint: use the sorted function)

deck = cards.make_deck()
shuffle(deck)
deck_suits = deck_suits(deck)
--SHOULD ALWAYS RETURN---
[
[2C, 3C, 4C, 5C, 6C, 7C, 8C, 9C, 10C, JC, QC, KC, AC],
[2D, 3D, 4D, 5D, 6D, 7D, 8D, 9D, 10D, JD, QD, KD, AD],
[2H, 3H, 4H, 5H, 6H, 7H, 8H, 9H, 10H, JH, QH, KH, AH],
[2S, 3S, 4S, 5S, 6S, 7S, 8S, 9S, 10S, JS, QS, KS, AS]
]

NOTE: Only shows the shorthand in example output. A card is a tuple w/ 4 values rank, suit, friendly name, shorthand
NOTE: a modified cards.py has been provided

"""
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


def deck_suits(deck: list[tuple[int, str, str, str]]) -> list[list[tuple[int, str, str, str]]]:
    return [sorted([card for card in deck if card[1] == suit]) for suit in SUITS]
