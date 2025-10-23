import game_logic.game

# BONUS 2 : Break the tie between the two players
# by adding up the total value of all their winning cards.
def break_a_tie(game_dic):
    p1_total_value = 0
    p2_total_value = 0
    for i in range(0, len(game_dic["player_1"]["won_pile"])):
        p1_total_value += game_dic["player_1"]["won_pile"][i]["value"]
    for i in range(0, len(game_dic["player_2"]["won_pile"])):
        p2_total_value += game_dic["player_2"]["won_pile"][i]["value"]
    if p1_total_value > p2_total_value:
        print("But the total value of " + game_dic["player_1"]["name"] + "'s cards is the highest," + game_dic["player_1"]["name"] + " wins !")
    if p1_total_value < p2_total_value:
        print("But the total value of " + game_dic["player_2"]["name"] + "'s cards is the highest," + game_dic["player_2"]["name"] + " wins !")
    if p1_total_value == p2_total_value:
        print("The total value of the cards of both players is also equal")


def main():
    if __name__ == "__main__":
        game_dic = game_logic.game.init_game()
        while len(game_dic["player_1"]["hand"]) > 0 and  len(game_dic["player_2"]["hand"]) > 0:
            game_logic.game.play_round(game_dic["player_1"], game_dic["player_2"])
        # if both players have the same number of cards
        if len(game_dic["player_1"]["won_pile"]) ==  len(game_dic["player_2"]["won_pile"]):
            print("\nboth players have the same number of cards, tie!")
            break_a_tie(game_dic) # Bonus 2
        # if player 1 has more cards
        if len(game_dic["player_1"]["won_pile"]) >  len(game_dic["player_2"]["won_pile"]):
            print("\n" + game_dic["player_1"]["name"] + " is the winner of the game with " + str(len(game_dic["player_1"]["won_pile"])) + " cards !!!\n")
        #if player 2 has more cards
        if len(game_dic["player_1"]["won_pile"]) <  len(game_dic["player_2"]["won_pile"]):
            print("\n" + game_dic["player_2"]["name"] + " is the winner of the game with " + str(len(game_dic["player_2"]["won_pile"])) + " cards !!!\n")

main()