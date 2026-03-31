"""
Jeremy Francis
2026_02_18
my_utilities.py
"""

import random
import subprocess
import platform

def roll_dice(times, sides):
    total = 0
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total


def roll_target(times, sides, target):
    total = 0
    for i in range(times):
        roll = random.randint(1, sides)
        if roll == target:
            return total
    return total
def clear_terminal():
    platform.system()
    # An empty string is returned if the value cannot be determined.
    # https://docs.python.org/3/library/platform.html
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
        # args is required for all calls and should be a string, or a sequence of program arguments.
        # https://docs.python.org/3/library/subprocess.html#frequently-used-arguments
    else:
        subprocess.run("clear", shell=True)




