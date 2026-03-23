import random
import subprocess
import platform
from hangman_words import word_list
from hangman_art import stages, logo


def clear_terminal():
    platform.system()
    # Returns the system/OS name, such as 'Linux', 'Darwin', 'Java', 'Windows'.
    # An empty string is returned if the value cannot be determined.
    # https://docs.python.org/3/library/platform.html
    if platform.system() == "Windows":
        subprocess.run("cls", shell=True)
        # args is required for all calls and should be a string, or a sequence of program arguments.
        # https://docs.python.org/3/library/subprocess.html#frequently-used-arguments
    else:
        subprocess.run("clear", shell=True)


lives = 6

input(logo + "\n\n\n PRESS ENTER TO START THE GAME...........")

chosen_word = random.choice(word_list)

game_over = False
correct_letters = []
wrong_letters = []

while not game_over:
    clear_terminal()
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(stages[lives])
    print(f"════════════════════════{lives}/6 LIVES LEFT════════════════════════")
    print("Correct letters: " + " ".join(correct_letters))
    print("Wrong letters: " + " ".join(wrong_letters))
    print("Word to guess: " + " ".join(display))
    print()

    if "_" not in display:
        game_over = True
        print("════════════════════════YOU WIN════════════════════════")
        input("Press Enter to continue...")
        break

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters or guess in wrong_letters:
        print(f"You've already guessed {guess}")
    elif guess in chosen_word:
        correct_letters.append(guess)
    else:
        wrong_letters.append(guess)
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            clear_terminal()
            print(stages[lives])
            print(
                f"════════════════════════IT WAS {chosen_word}! YOU LOSE════════════════════════\n"
            )
            input("Press Enter to quit...")
