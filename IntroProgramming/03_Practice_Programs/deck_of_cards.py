"""
Jeremy Francis
2026_03_30
Build Deck Of Cards
"""
import random

cards = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

def create_deck():
    deck = []
    for suit in suits:
        for card, value in cards.items():
            if value >10 and card != '10':
                deck.append({"suit": suit, "card": card, "value": value})
            else:
                deck.append({"suit": suit, "value": value})
    random.shuffle(deck)
    return deck
def draw_cards(deck):
    if

def fisher_yates_shuffle(deck):
    for i in range(len(deck) -1,0,-1):
        j = random.randint(0,i)
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp
    return deck