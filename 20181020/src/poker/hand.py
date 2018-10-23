# -*- coding: utf-8 -*-

from .card import Card, card_values, card_rank
from .exceptions import DuplicatedCardError

ranks = [
        'High Card', 'Pair', 'Two Pairs', 'Three of a Kind', 'Straight',
        'Flush', 'Full House', 'Four of a Kind', 'Straight Flush'
        ]

rank_order = {rnk: n for (n, rnk) in enumerate(ranks)}

class Hand(object):
    def __init__(self, hand):
        raw_cards = hand.split()
        if len(set(raw_cards)) < 5:
            raise DuplicatedCardError("Illegal hand")
        self.cards = sorted([Card(face) for face in hand.split()])
        self.suit_set = set(c.suit for c in self.cards)
        self.values = [c.value for c in self.cards]
        value_set = set(self.values)
        self.value_groups = tuple(sorted((self.values.count(x), card_rank[x]) for x in value_set))

    def __lt__(self, other):
        if isinstance(other, Hand):
            rord1, rord2 = rank_order[self.rank()], rank_order[other.rank()]
            if rord1 == rord2:
                rev1, rev2 = reversed(self.value_groups), reversed(other.value_groups)
                for g1, g2 in zip(rev1, rev2):
                    if g1[1] < g2[1]:
                        return True
                return False
            else:
                return rord1 < rord2
        else:
            raise TypeError("Can only compare instances of Hand")

    def rank(self):
        joined = ''.join(self.values)
        vg = tuple(number for (number, value) in self.value_groups)
        if joined in card_values or joined == '2345A':
            rnk = 'Straight Flush' if len(self.suit_set) == 1 else 'Straight'
        elif len(self.suit_set) == 1:
            rnk = 'Flush'
        elif vg[-1] == 4:
            rnk = 'Four of a Kind'
        elif vg[-1] == 3:
            rnk = 'Full House' if vg == (2, 3) else 'Three of a Kind'
        elif vg == (1, 2, 2):
            rnk = 'Two Pairs'
        elif vg[-1] == 2:
            rnk = 'Pair'
        else:
            rnk = 'High Card'

        return rnk
