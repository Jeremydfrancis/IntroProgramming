"""
Jeremy Francis
2026_03_22
Slot Machine
"""

import random
import subprocess
import platform

jackpot = 1000

payouts = {
    "7": 10,
    "BELL": 5,
    "BAR": 4,
    "PLUM": 3,
    "ORANGE": 3,
    "LEMON": 2,
    "CHERRY": 2,
}


def clear_terminal():
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)


def spin_slots():
    slot_items = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]
    return (
        str(random.choice(slot_items)),
        str(random.choice(slot_items)),
        str(random.choice(slot_items)),
    )


def play_slots(balance):
    user_input = input("\nHow much would you like to bet (Enter 0 to quit)? ")
    try:
        play = float(user_input)
        if play == 0:
            print(f"\nYour total winnings are: ${balance}")
            return 0
        if play < 0:
            print("\nPlease enter a number greater than 0.")
            return None
        if play > balance:
            print("\nYou don't have enough balance.")
            return None
        balance -= play
        return play, balance
    except ValueError:
        print(
            f'\n"{user_input}" is an invalid entry, enter a number greater than 0 to play.'
        )
        return None


def calculate_score(slot_one, slot_two, slot_three, bet):
    if slot_one == slot_two == slot_three:
        muliplier = payouts[slot_one]
        return muliplier * bet
    else:
        return 0


def main():
    balance = 100
    while True:
        print(f"\nYour total balance is ${balance}")
        result = play_slots(balance)
        if result is None:
            continue
        if result == 0:
            print(f"\nYour total winnings are: ${balance}")
            break
        play, balance = result
        print(f"\nYou have bet a total of {play}")
        one, two, three = spin_slots()
        print(f"\n{one}-{two}-{three}")
        winnings = calculate_score(one, two, three, play)

        if winnings > 0:
            print(f"\nYou have won ${winnings}!")
        else:
            print(f"\nNo match you have lost ${play}")

        balance += winnings

        if balance <= 0:
            print("You have lost all of your money, maybe quit gambling!")
            break
        input("\nPress enter to continue....")
        clear_terminal()


if __name__ == "__main__":
    main()
