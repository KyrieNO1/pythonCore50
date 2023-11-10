from enum import Enum
import random


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)
    
"""for suite in Suite:
    print(f'{suite}:{suite.value}')"""

class Card:
    """牌类"""
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}, {faces[self.face]}'
    
"""card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)    # ♠5 ♥K"""

class Poker:
    """扑克类"""
    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


class Player:
    """玩家类"""
    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()

players = [Player('amy'), Player('bob'), Player('candy'), Player('dove')]

poker = Poker()
poker.shuffle()

for i in range(13):
    for player in players:
        player.get_one(poker.deal())

for player in players:
    player.arrange()
    print(f'{player.name}: {player.cards}')