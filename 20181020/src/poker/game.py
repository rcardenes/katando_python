# -*- coding: utf-8 -*-

from .hand import Hand

def play(hand1, hand2):
    if hand1 < hand2:
        wins = 2
    elif hand2 < hand1:
        wins = 1
    else:
        wins = 0

    if wins == 1:
        return "Player 1 - {}".format(hand1.rank())
    elif wins == 2:
        return "Player 2 - {}".format(hand2.rank())
    else:
        return "Tie"
