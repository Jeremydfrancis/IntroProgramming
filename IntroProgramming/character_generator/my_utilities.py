"""
Jeremy Francis
2026_02_18
my_utilities.py
"""
import random
import subprocess
import platform
import pickle
import os

def roll_dice(times, sides):
    """Rolls a die (times*sides) and returns the total."""
    total = 0
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total

def clear_terminal():
    """Clears the terminal screen based on the operating system."""
    platform.system()
    # https://docs.python.org/3/library/platform.html
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
        # https://docs.python.org/3/library/subprocess.html#frequently-used-arguments
    else:
        subprocess.run("clear", shell=True)
def show_saves():
    """Lists all available save files in the current directory."""
    directory = os.listdir()
    for file in directory:
        if file.endswith(".pkl"):
            print(file.replace(".pkl", ""))
def save_game(player,board,treasure,save_name):
    """Saves the current game state to a pickle file with the given name from user input."""
    game_data = {"player": player, "board": board, "treasure": treasure}
    try:
            if os.path.exists(f"{save_name}.pkl"):
                overwrite_game = input("Do you want to overwrite existing game? (y/n): ")
                if overwrite_game == "y":
                    with open(f"{save_name}.pkl", "wb") as file:
                        pickle.dump(game_data, file)
                elif overwrite_game == "n":
                    return None
            else:
                with open(f"{save_name}.pkl", "wb") as file:
                    pickle.dump(game_data, file)
    except OSError as error:
        print(f"Error saving game: {error}")
    except pickle.PicklingError as error:
        print(f"Error saving game: {error}")

def load_game(save_name):
    """Loads and returns game state from a pickle file with the given name."""
    try:
        with open(f"{save_name}.pkl","rb") as file:
                game_data = pickle.load(file)
                return game_data
    except OSError as error:
        input(f"Error loading game: {error}")
    except pickle.UnpicklingError as error:
        input(f"Error loading game: {error}")
    except EOFError as error:
        input(f"Error loading game: {error}")








def roll_target(times, sides, target):
    """Rolls a die up to ( Times*sides) and returns True if (target) is hit."""
    for i in range(times):
        roll = random.randint(1, sides)
        if roll == target:
            return True
    return False







