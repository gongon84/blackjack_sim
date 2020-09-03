import pprint
import collections
import matplotlib.pyplot as plt
import numpy as np
from random import shuffle


# 山札
class Deck:

    def __init__(self):

        # 山札準備
        self.suits = ['スペード', 'クラブ', 'ダイヤ', 'ハート']
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        self.deck = []

        # シャッフル
        for i in self.suits:
            for j in self.values:
                self.deck.append([i, j])
                shuffle(self.deck)


class Person(Deck):

    def __init__(self):

        # 手札
        self.hands = []
        self.point = 0
        self.deliver = []

    # カードを引く
    def draw(self, deck):

        self.deliver = deck.pop(0)

        # 山札に加える
        self.hands.append(self.deliver)

        # 点数計算
        self.point = self.count()

    # 点数計算
    def count(self):

        count = 0
        ace = 0

        # 計算
        for i in range(len(self.hands)):
            try:
                count += self.hands[i][1]
            except:
                # J,Q,Kを引いたとき
                if self.hands[i][1] == 'J' or self.hands[i][1] == 'Q' or self.hands[i][1] == 'K':
                    count += 10

        # 1を引いたとき、合計が11以下なら、1→11
        for i in range(len(self.hands)):
            if self.hands[i][1] == 1:
                ace += 1

        if ace == 1:
            if count <= 11:
                count += 10
        elif ace == 2:
            count += 10

        return count

    # ディーラーのオープンカードを決定
    def opencard(self, dealer):

        number = 0

        # 計算
        # J,Q,Kを引いたとき
        if dealer.hands[0][1] == 'J' or dealer.hands[0][1] == 'Q' or dealer.hands[0][1] == 'K':
            number = 10
        else:
            number = dealer.hands[0][1]

        return number

    # ずっと１


def normal(money, bet, judge):
    if judge == 'win':
        money += bet
        bet = 1
    elif judge == 'draw':
        money += 0
        bet = 1
    elif judge == 'lose':
        money -= bet
        bet = 1
    return money, bet


# 負けたら２倍
def bai(money, bet, judge):
    if judge == 'win':
        money += bet
        bet = 1
    elif judge == 'draw':
        money += 0
    elif judge == 'lose':
        money -= bet
        bet = bet * 2
    return money, bet


# 勝敗決定
def winlose(point1, point2):
    if point1 > 21:
        return "lose"
    else:
        if point2 > 21:
            return "win"
        elif 21 - point1 < 21 - point2:
            return "win"
        elif 21 - point1 > 21 - point2:
            return "lose"
        else:
            return "draw"


# 点数計算（1以外）
def count2(self):
    count = 0

    # 計算
    for i in range(len(self.hands)):
        if self.hands[i][1] != 1:
            try:
                count += self.hands[i][1]
            except:
                # J,Q,Kを引いたとき
                if self.hands[i][1] == 'J' or self.hands[i][1] == 'Q' or self.hands[i][1] == 'K':
                    count += 10

    return count


def start():
    finalmoneylist = []

    for f in range(1):
        money = 1000
        bet = 1
        loop = 500
        moneylist = [money]
        countlist = [0]
        opencard1 = 0

        # 戦略 < normal or basic > < normal or bai>
        st = 'basic'
        betst = 'bai'

        for t in range(loop):
            # デッキと人を用意
            deck1 = Deck()
            player1 = Person()
            dealer1 = Person()
            judge = ""

            # ディーラーが２枚引く
            for i in range(2):
                dealer1.draw(deck1.deck)

            # プレイヤーが２枚引く
            for i in range(2):
                player1.draw(deck1.deck)

            # ディーラーのオープンカード決定
            opencard1 = dealer1.opencard(dealer1)

            # プレイヤー　ベーシックシート通りに引く
            if st == 'normal':
                while player1.point < 17:
                    player1.draw(deck1.deck)
            elif st == 'basic':

                while True:
                    ace = 0

                    # 1があるか確認
                    for i in range(len(player1.hands)):
                        if player1.hands[i][1] == 1:
                            ace += 1

                    # 手札にAがあるとき
                    if ace == 1:

                        # A以外の数を求める
                        other = 0
                        for i in range(len(player1.hands)):
                            if player1.hands[i][1] != 1:
                                other = count2(player1)

                                # プレイヤーが選択決定
                        if other == 2 or other == 3:
                            if 5 <= opencard1 <= 6:  # double
                                if len(player1.hands) < 3:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif other == 4 or other == 5:
                            if 4 <= opencard1 <= 6:  # double
                                if len(player1.hands) < 3:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif other == 6:
                            if 3 <= opencard1 <= 6:  # double
                                if len(player1.hands) < 3:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif other == 7:
                            if 3 <= opencard1 <= 6:  # double
                                if len(player1.hands) < 3:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            elif opencard1 == 2 or opencard1 == 7 or opencard1 == 8:
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif other == 8 or other == 9 or other == 10:
                            break
                        elif other >= 11:  # Aが1の扱いのとき
                            if other == 11:
                                if 4 <= opencard1 <= 6:  # stay
                                    break
                                else:
                                    player1.draw(deck1.deck)
                            elif 12 <= other <= 15:
                                if 2 <= opencard1 <= 6:  # stay
                                    break
                                else:
                                    player1.draw(deck1.deck)
                            elif other >= 16:  # stay
                                break
                    elif ace == 2:
                        # A以外の数を求める
                        other = 0
                        for i in range(len(player1.hands)):
                            if player1.hands[i][1] != 1:
                                other = count2(player1)
                        other += 11

                        # 場合分け
                        if other == 11:
                            if 4 <= opencard1 <= 6:  # stay
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif 12 <= other <= 15:
                            if 2 <= opencard1 <= 6:  # stay
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif other >= 16:  # stay
                            break
                    elif ace >= 3:
                        print("error--------------------------------------")
                        break
                    else:
                        # 手札にAがないとき
                        if player1.point <= 8:
                            player1.draw(deck1.deck)
                        elif player1.point == 9:
                            if 3 <= opencard1 <= 6:  # double
                                if len(player1.hands) <= 2:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif player1.point == 10:
                            if 2 <= opencard1 <= 9:  # double
                                if len(player1.hands) <= 2:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif player1.point == 11:
                            if 2 <= opencard1 <= 10:  # double
                                if len(player1.hands) <= 2:
                                    bet = bet * 2
                                    player1.draw(deck1.deck)
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif player1.point == 12:
                            if 4 <= opencard1 <= 6:  # stay
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif 13 <= player1.point <= 16:
                            if 2 <= opencard1 <= 6:  # stay
                                break
                            else:
                                player1.draw(deck1.deck)
                        elif player1.point >= 17:  # stay
                            break

            # ディーラーが１７以上になるまで引く
            while dealer1.point < 17:
                dealer1.draw(deck1.deck)

            # 勝敗決定
            judge = winlose(player1.point, dealer1.point)

            # 掛け金
            if betst == 'normal':
                money, bet = normal(money, bet, judge)
            elif betst == 'bai':
                money, bet = bai(money, bet, judge)

            # お金を記録　回数を＋１
            moneylist.append(money)
            countlist.append(t + 1)

            # print
            # print("player {} {}".format(player1.point, player1.hands))
            # print("dealer {} {}".format(dealer1.point, dealer1.hands))
            # print("{}:{} → {}".format(judge, moneylist[t], moneylist[t+1]))

        print(money)
        finalmoneylist.append(money)

        # グラフ表示
        plt.plot(countlist, moneylist)
        plt.xlabel("count")
        plt.ylabel("money")

        # 表示範囲
        # plt.xticks(list(range(0,t+1)))
        # plt.yticks(list(range(90,111)))

        plt.show()

    # マネーリスト表示
    # print("\n")
    # print(finalmoneylist)
    # print("\n")


if __name__ == "__main__":
    start()
