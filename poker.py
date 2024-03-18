import random
class Card:
    SUITS = ["♡", "♦", "♤", "♣"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise Exception(f"Invalid Suit, needs to be one of: {self.SUITS}")
        if rank not in self.RANKS:
                raise Exception(f"Invalid Rank, needs to be one of: {self.RANKS}")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    #need to be able to print the card!
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(suit=suit, rank=rank))
        cards = tuple(cards)
        self._cards = cards

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)

    def __str__(self):
        return f"{self.cards}"

class PokerHand:
    def __init__(self, deck):
        hand = []
        for i in range(5):
            hand.append(deck.cards[i])
        self._hand = hand

    @property
    def hand(self):
        return self._hand

    def __str__(self):
        return f"{self.hand}"

    @property
    def is_flush(self):
        suit= self.hand[0].suit
        for i in range(1, 5):
            if self.hand[i].suit != suit:
                return False
        return True


card = Card("♦", "K")
print(card)
card2 = Card(rank = "2", suit = "♣")
print(card2)
cards_list = [card, card2]
print(cards_list)

deck = Deck()
print(deck)
#deck.cards.append(card) #You cannot append to a tuple
deck.shuffle()
print(deck)

hand = PokerHand(deck)
print(f"A random poker hand is: {hand}")
print(f"Is this hand a flush? {hand.is_flush}")
attempt = 0
flushes = 0
while True:
    attempt += 1
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush == True:
        flushes += 1
        if flushes == 100:
            break

print(flushes/attempt*100)