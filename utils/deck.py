from logging import exception
import random

def create_card(rank:str,suite:str) -> dict:
    value = 0
    # if rank is letter
    if (rank == "J"):
        value = 11
    elif (rank == "Q"):
        value = 12
    elif (rank == "K"):
        value = 13
    elif (rank == "A"):
        value = 14
    # if rank is number
    else:
        try:
            value = int(rank)
        except ValueError:
            print("Invalid rank")
        if value < 2 or value > 10:
            print("Invalid rank")
    # check if valid suite
    if suite != "H" and suite != "C" and suite != "D" and suite != "S":
        print("Invalid suite")
    # do the dic
    dic = {"rank" : rank, "suite" : suite, "value" : value}
    return dic



def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] == p2_card["value"]:
        return "WAR"
    elif p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p1_card["value"] < p2_card["value"]:
        return "p2"



def create_deck() -> list[dict]:
    ranks_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10","J", "Q", "K", "A"]
    suite_list = ["H", "C", "D", "S"]
    lst = []
    for suite in suite_list:
        for rank in ranks_list:
            lst.append(create_card(rank, suite))
    return lst



def shuffle(deck:list[dict]) -> list[dict]:
    index1 = 0
    index2 = 0
    repeat = 0
    while repeat < 1000:
        flag = True
        while flag:
            index1 = random.randint(0, len(deck)-1)
            index2 = random.randint(0, len(deck)-1)
            if index1 != index2:
                flag = False
        tmp = deck[index1]
        deck[index1] = deck[index2]
        deck[index2] = tmp
        repeat += 1
    return deck


