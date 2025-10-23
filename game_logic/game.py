from operator import truediv

import utils.deck

def create_player(name:str = "AI") -> dict:
    hand_lst = []
    won_pile_lst = []
    dic = {"name" : name, "hand" : hand_lst, "won_pile" : won_pile_lst }
    return dic



def init_game()->dict:
    p1 = create_player("Aviel")
    p2 = create_player("AI")
    deck_no_shuffle = utils.deck.create_deck()
    deck = utils.deck.shuffle(deck_no_shuffle)
    card_number = 0 # to count and give 26 to each
    for card in deck:
        if card_number < 26:
            p1["hand"].append(card)
        else:
            p2["hand"].append(card)
        card_number += 1
    dic = {"deck" : deck, "player_1" : p1, "player_2" : p2}
    return dic



def play_round(p1:dict,p2:dict):
    winner = p1 # just value to init the winner
    card_1 = p1["hand"].pop()
    card_2 = p2["hand"].pop()
    result = utils.deck.compare_cards(card_1, card_2)
    if result == "p1":
        winner = p1
        p1["won_pile"].append(card_1)
        p1["won_pile"].append(card_2)
    elif result == "p2":
        winner = p2
        p2["won_pile"].append(card_1)
        p2["won_pile"].append(card_2)
#    BONUS : elif result == "WAR":
    print (winner["name"] + " won this round")

# BONUS 1
# def war_game(p1:dict,card1,p2:dict,card2):
#     flag = True
#     while flag:
#         flag = False
#         card1_1price = p1["hand"].pop()
#         card1_2price = p2["hand"].pop()
#         card1_3price = p1["hand"].pop()
#         card1_4 = p2["hand"].pop()
#
#         card2_1price = p2["hand"].pop()
#         card2_2price = p2["hand"].pop()
#         card2_3price = p2["hand"].pop()
#         card2_4 = p2["hand"].pop()
#
#         result = utils.deck.compare_cards(card1_4, card2_4)
#         if result == "p1":
#             winner = p1
#             p1["won_pile"].append(card1)
#             p1["won_pile"].append(card1_1price)
#             p1["won_pile"].append(card1_2price)
#             p1["won_pile"].append(card1_3price)
#             p1["won_pile"].append(card1_4)
#
#             p1["won_pile"].append(card2)
#             p1["won_pile"].append(card2_1price)
#             p1["won_pile"].append(card2_2price)
#             p1["won_pile"].append(card2_3price)
#             p1["won_pile"].append(card2_4)
#
#         elif result == "p2":
#             winner = p2
#             p2["won_pile"].append(card1)
#             p2["won_pile"].append(card1_1price)
#             p2["won_pile"].append(card1_2price)
#             p2["won_pile"].append(card1_3price)
#             p2["won_pile"].append(card1_4)
#
#             p2["won_pile"].append(card2)
#             p2["won_pile"].append(card2_1price)
#             p2["won_pile"].append(card2_2price)
#             p2["won_pile"].append(card2_3price)
#             p2["won_pile"].append(card2_4)
#
#         elif result == "WAR":
#             flag = True





