from enum import Enum
import random


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)

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
        self.hands = []

    def get_one(self, card):
        """摸牌"""
        self.hands.append(card)

    def clear_hand(self):
        """清空手牌"""
        self.hands = []

    def show_hand(self):
        """展示手牌"""
        print(f"{self.name}'s hand: {self.hands}")

    def calculate_score(self):
        """计算手牌分数"""
        score = 0
        num_aces = 0 #1点数量

        """ 数字牌（2-10）的点数等于其面值。
            J、Q、K的点数为10。
            A的点数可以是1或11，玩家可以根据需要选择其点数。"""
        for card in self.hands:
            if card.face == 1:
                score += 11
                num_aces += 1
            elif card.face >= 10:
                score += card.face
            else:
                score += card.face

            """A可以为1或者11，超过21时选择更靠近21的"""
            while score > 21 and num_aces >0:
                score -= 10
                num_aces -= 1

        return score


    def arrange(self):
        """洗牌"""
        self.hands.sort()


class Game:
    """游戏类"""
    def __init__(self, players):
        self.players = players
        self.poker = Poker()

    def start(self):
        print("Welcome to the BLACKJACK!")

        for player in self.players:
            player.clear_hand()

        self.poker.shuffle()

        for i in range(1, 3):
            for player in self.players:
                player.get_one(self.poker.deal())

        for player in self.players:
            player.show_hand()

        self.play_round()

    def play_round(self):
        for player in self.players:
            while True:
                choice = input(f"{player.name}, do you want to 'hit' or 'stand'")
                if choice == 'hit':
                    player.get_one(self.poker.deal())
                    player.show_hand()
                    """如果有人超过或等于21点，接受False，结束此玩家游戏"""
                    if not self.check_score(player):
                        break
                elif choice == 'stand':
                    break
                else:
                    print("Invalid input. Please enter 'hit' or 'stand'")

        self.show_results()
        self.play_again()


    def check_score(self, player):
        score = player.calculate_score()
        """如果此玩家超过或等于21点，返回False"""
        if score > 21:
            print(f"{player.name}, you bust! Your score is {score}.")
            return False
        elif score == 21:
            print(f"{player.name}, you win! Your score is 21!")
            return False
        """如果游戏没有结束，返回True"""
        return True

    def show_results(self):
        print("\n----- 游戏结果 -----")

        # 根据分数降序排序玩家
        sorted_players = sorted(self.players, key=lambda player: player.calculate_score(), reverse=True)

        winning_player = None
        winning_score = 0

        for player in sorted_players:
            score = player.calculate_score()
            if score <= 21:
                if winning_player is None or (score > winning_score and score <= 21):
                    winning_player = player
                    winning_score = score

                print(f"{player.name}: {player.show_hand()} -> 分数: {score}")

        if winning_player:
            print(f"\n{winning_player.name} 获胜，分数为 {winning_score} 分!")
        else:
            print("\n没有玩家获胜，平局!")

        print("-------------------")

    def play_again(self):
        choice = input("Do you want to play again? (yes/no)")
        if choice == 'yes':
            self.start()
        elif choice == 'no':
            print("Thank you for playing!")


# Create players
players = [Player('Amy'), Player('Bob')]

game = Game(players)
game.start()


