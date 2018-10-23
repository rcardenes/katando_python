# -*- coding: utf-8 -*-
card_values = '23456789TJQKA'
card_suits  = 'SHCD'
card_rank   = {value:n for (n, value) in enumerate(card_values)}

card_value_set = set(card_values)
card_suit_set  = set(card_suits)

class Card(object):
    def __init__(self, face):
        if len(face) != 2 or face[0] not in card_value_set or face[1] not in card_suits:
            raise ValueError("Illegal value: {}".format(face))
        self.value = face[0]
        self.suit  = face[1]

    def __lt__(self, other):
        if isinstance(other, Card):
            return card_rank[self.value] < card_rank[other.value]
        else:
            raise TypeError("Can only compare two instances of Card")

    def __repr__(self):
        return '<Card: {{ value: {}, suit: {} }}>'.format(self.value, self.suit)
