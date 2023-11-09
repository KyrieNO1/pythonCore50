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
        self.cards = [for s