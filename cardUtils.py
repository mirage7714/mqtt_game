# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:41:49 2019

@author: mirag
"""

import random

cards = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13',
         'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11','B12','B13',
         'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13',
         'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13'
         ]

cards_occupied = []
cards_for_players = {}

def get_first_card(players):
    for n in range(players):
        send_cards = []
        while(len(send_cards) < 5):
            index = random.randrange(len(cards))
            card = cards[index]
            if card not in cards_occupied:
                send_cards.append(card)
                cards_occupied.append(card)
        cards_for_players[n] = send_cards

def request_change_card(cards_for_players, player):
    cards_to_exchange = cards_for_players[player]
    new_cards = []
    for card in cards_to_exchange:
        cards_occupied.remove(card)
    while(len(new_cards) < 5):
        index = random.randrange(len(cards))
        card = cards[index]
        if card not in cards_occupied:
            new_cards.append(card)
            cards_occupied.append(card)
    cards_for_players[player] = new_cards
            