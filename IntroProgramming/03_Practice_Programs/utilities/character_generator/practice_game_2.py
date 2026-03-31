"""
Jeremy Francis
2026_03_25
DND Character Generation
"""

import my_utilities
import random
from player import gen_name, gen_history
import textwrap


def gen_player(level):
    player = {}
    # player["str"] = my_utilities.roll_dice(3, 6)
    # player["dex"] = my_utilities.roll_dice(3, 6)
    # player["con"] = my_utilities.roll_dice(3, 6)
    # player["int"] = my_utilities.roll_dice(3, 6)
    # player["wis"] = my_utilities.roll_dice(3, 6)
    # player["cha"] = my_utilities.roll_dice(3, 6)

    player["attack"] = my_utilities.roll_dice(3, 6) + my_utilities.roll_dice(level, 4)
    player["defense"] = my_utilities.roll_dice(3, 6) + my_utilities.roll_dice(level, 4)
    player["health"] = my_utilities.roll_dice(5, 6) + my_utilities.roll_dice(level, 4)
    player["row"] = 0
    player["column"] = 0
    # player["class"] = gen_class(player)
    player["name"] = gen_name()
    player["history"] = gen_history()
    return player


def drop_roller():
    rolls = []
    for i in range(4):
        rolls.append(random.randint(1, 4))
    rolls.sort(reverse=True)
    rolls = rolls[0:3]
    return sum(rolls)


# def gen_class(player):
#     classes = {
#         "str": "Fighter",
#         "int": "Wizard",
#         "wis": "Cleric",
#         "dex": "Thief",
#         "cha": "Bard",
#         "con": "Fighter",
#     }
#     max_key = max(player, key=player.get)
#     return classes[max_key]

def generate_all():
    wrapper = textwrap.TextWrapper(width=65)
    while True:
        player = gen_player(5)
        print(wrapper.fill("NAME: " + player["name"]))
        # print("CLASS:\t"  + player["class"])
        for key in player:
            if key != "name":
                print(wrapper.fill(key.upper() + ":" + " " + str(player[key])))
        user_input = input("Generate another character (Y/N)? ").upper()
        if user_input == "N":
            break
        else:
            my_utilities.clear_terminal()

