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

class Game:
    """21点游戏类"""

    def __init__(self, players):
        self.players = players
        self.poker = Poker()

    def start(self):
        """开始游戏"""
        print("Welcome to the game of 21 points!")

        for player in self.players:
            player.clear_hand()

        self.poker.shuffle()

        for i in range(2):  # 发两张牌
            for player in self.players:
                player.get_one(self.poker.deal())

        for player in self.players:
            player.show_hand()

        self.play_round()

    def play_round(self):
        """进行一轮游戏"""
        for player in self.players:
            while True:
                choice = input(f"{player.name}, do you want to 'hit' or 'stand'? ")
                if choice == 'hit':
                    player.get_one(self.poker.deal())
                    player.show_hand()
                    if not self.check_score(player):
                        break
                elif choice == 'stand':
                    break
                else:
                    print("Invalid choice. Please enter 'hit' or 'stand'.")

        self.show_results()
        self.play_again()

    def check_score(self, player):
        """检查玩家分数"""
        score = player.calculate_score()
        if score > 21:
            print(f"Sorry {player.name}, you bust! Your score is {score}.")
            return False
        elif score == 21:
            print(f"Congratulations {player.name}, you scored 21!")
            return False
        return True

    def show_results(self):
        """展示最终结果"""
        print("\n----- Results -----")
        for player in self.players:
            score = player.calculate_score()
            if score <= 21:
                print(f"{player.name}: {player.show_hand()} -> Score: {score}")
        print("-------------------")

    def play_again(self):
        """询问是否重新开始游戏"""
        choice = input("Do you want to play again? (yes/no) ")
        if choice == "yes":
            self.start()
        else:
            print("Thank you for playing!")


class Player:
    """21点玩家类"""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_one(self, card):
        """摸牌"""
        self.hand.append(card)

    def clear_hand(self):
        """清空手牌"""
        self.hand = []

    def show_hand(self):
        """展示手牌"""
        print(f"{self.name}'s hand: {self.hand}")

    def calculate_score(self):
        """计算手牌分数"""
        score = 0
        num_aces = 0

        for card in self.hand:
            if card.face == 1:  # Ace
                score += 11
                num_aces += 1
            elif card.face >= 10:  # Face cards (Jack, Queen, King)
                score += 10
            else:
                score += card.face

        while score > 21 and num_aces > 0:
            score -= 10
            num_aces -= 1

        return score


# Create players
players = [Player('Amy'), Player('Bob')]

# Start the game
game = Game(players)
game.start()