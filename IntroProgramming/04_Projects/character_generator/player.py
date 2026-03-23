"""
Jeremy Francis
2026_18_2026
Player.py
"""

import random
import subprocess
import platform
import textwrap


def gen_name():
    first_name = "Taco Biscuit Pickle Waffle Noodle Dumpling Pretzel Pudding Brisket Crumpet Nacho Cobbler Gravy Muffin Churro Gumbo Beignet Scone Pierogi Grits".split()
    middle_name = "Flowerdew, Moneypenny III, Wildblood Jr., Clutterbuck, Gotobed IV, Noodleman Jr., Muddington, Lickfold III, Winterflood Jr., Cavendish, Picklebottom IV, Younghusband Jr., Floodgate, Earwalker III, Valiant Jr., Choco, Wizard IV, Wildgoose Jr., Fetherstonehaugh, Newlove III".split(
        ", "
    )

    last_name = "The Cursed One, The Slightly Feared, The Pretty OK Wizard, The Moderately Evil, The Destroyer of Snacks, The Somewhat Legendary, The Dread of Tuesdays, The Barely Tolerated, The Mildly Terrifying, The Almost Chosen One, The Forgotten One, The Bringer of Mild Discomfort".split(
        ", "
    )

    pos1 = random.choice(first_name)
    pos2 = random.choice(middle_name)
    pos3 = random.choice(last_name)
    full_name = "Player Name: " + pos1 + " " + pos2 + ", " + pos3
    return full_name


def gen_history():
    backgrounds = "You were born in [LOCATION1] to a [ADJECTIVE1] [NOUN1] who [VERB1] for a living. Your childhood was [ADJECTIVE2] at best.|A [ADJECTIVE1] [NOUN1] [VERB1] your entire village in [LOCATION1] when you were young. You were the only survivor, mostly because you were hiding behind a [NOUN2].|You grew up as the [ADJECTIVE1] apprentice of a [NOUN1] in [LOCATION1] who [VERB1] you on a daily basis. You learned nothing useful.|Your parents were a [ADJECTIVE1] [NOUN1] and an even more [ADJECTIVE2] [NOUN2] who met in [LOCATION1] after one of them accidentally [VERB1] the other.|You were abandoned as a child in [LOCATION1] and raised by a [ADJECTIVE1] [NOUN1] who [VERB1] for sport. It was character building apparently.".split(
        "|"
    )
    templates = "You are currently on a quest to [PRESENTVERB1] a [ADJECTIVE1] [NOUN1] somewhere in [LOCATION1]. Nobody hired you. You just showed up.|You have been tasked by a [ADJECTIVE1] [NOUN1] to [PRESENTVERB1] the legendary [NOUN2] of [LOCATION1]. The pay is terrible but the snacks are decent.|You are hunting a [ADJECTIVE1] [NOUN1] across [LOCATION1] who [VERB1] your favorite [NOUN2]. This is personal.|Your current mission is to [PRESENTVERB1] every [NOUN1] in [LOCATION1] before a [ADJECTIVE1] [NOUN2] does it first. You are already behind schedule.|You have three days to [PRESENTVERB1] a [ADJECTIVE1] [NOUN1] from [LOCATION1] or a very disappointed [NOUN2] will never speak to you again.".split(
        "|"
    )
    nouns = "goblin, dragon, wizard, bard, paladin, enchanted spatula, cursed ladle, haunted muffin, sentient cheese wheel, rogue baker, undead pastry chef, possessed cauldron, ancient recipe scroll, enchanted frying pan, skeletal soup spoon, confused necromancer, retired assassin, discount sorcerer, enchanted rolling pin, cursed whisk, legendary turnip, suspicious stew, immortal sandwich, rebellious kettle, haunted cookbook, disgruntled dwarf, overqualified goblin, enchanted colander, cursed gravy boat, slightly evil crouton, bewildered knight, discount dragon, enchanted napkin, possessed cutting board, reluctant demon".split(
        ", "
    )
    verbs = "defeated, befriended, accidentally summoned, ate, traded, challenged, insulted, cooked for, escaped from, negotiated with, smuggled, enchanted, cursed, baked into a pie, tripped over, accidentally married, deeply offended, mildly inconvenienced, sat on, accidentally adopted, threw soup at, got lost with, accidentally freed, argued with, dramatically betrayed, politely ignored, accidentally cursed, fell asleep on, loudly insulted, quietly disappointed".split(
        ", "
    )
    present_verbs = "defeat, retrieve, locate, destroy, befriend, steal from, negotiate with, cook for, escape from, capture, rescue, challenge, smuggle, deliver, find, apologize to, return a borrowed item to, make soup for, argue with, politely intimidate, dramatically confront, accidentally free, bake a pie for, have a conversation with, race against, outwit, begrudgingly assist, loudly defeat, quietly relocate, confuse".split(
        ", "
    )
    adjectives = "cursed, enchanted, mediocre, slightly evil, suspiciously delicious, moderately legendary, deeply confusing, mildly terrifying, overcooked, aggressively bland, surprisingly powerful, unnecessarily dramatic, poorly seasoned, reluctantly heroic, legally questionable, suspiciously cheerful, accidentally immortal, thoroughly bewildered, mildly cursed, quietly menacing, aggressively average, professionally incompetent, suspiciously well dressed, moderately haunted, deeply unremarkable, accidentally enchanted, slightly crispy, overwhelmingly mediocre, disturbingly polite, confusingly powerful".split(
        ", "
    )
    locations = "the Dungeon of Mild Inconvenience, the Tavern of Broken Dreams, the Forest of Suspicious Smells, the Kingdom of Overcooked Meats, the Cave of Endless Soup, the Tower of Dubious Wizardry, the Swamp of Regrettable Decisions, the Bakery of Ancient Secrets, the Valley of Unfortunate Choices, the Castle of Moderate Despair, the Marsh of Questionable Decisions, the Village of Perpetual Confusion, the Fortress of Accidental Evil, the Library of Forbidden Recipes, the Harbor of Lost Spatulas, the Mountains of Mild Peril, the Plains of Overwhelming Blandness, the Ruins of the Ancient Buffet, the Citadel of Unnecessary Drama, the Bog of Eternal Stew, the Academy of Mediocre Magic, the Temple of the Sacred Whisk, the Arena of Polite Combat, the Crypt of the Forgotten Chef, the Outpost of Reluctant Heroes".split(
        ", "
    )
    background = random.choice(backgrounds)
    template = random.choice(templates)
    full_story = (
        background.replace("[NOUN1]", random.choice(nouns))
        .replace("[NOUN2]", random.choice(nouns))
        .replace("[VERB1]", random.choice(verbs))
        .replace("[LOCATION1]", random.choice(locations))
        .replace("[ADJECTIVE1]", random.choice(adjectives))
        .replace("[ADJECTIVE2]", random.choice(adjectives))
        .replace("[PRESENTVERB1]", random.choice(present_verbs))
    ) + (
        template.replace("[NOUN1]", random.choice(nouns))
        .replace("[NOUN2]", random.choice(nouns))
        .replace("[VERB1]", random.choice(verbs))
        .replace("[LOCATION1]", random.choice(locations))
        .replace("[ADJECTIVE1]", random.choice(adjectives))
        .replace("[ADJECTIVE2]", random.choice(adjectives))
        .replace("[PRESENTVERB1]", random.choice(present_verbs))
    )
    return full_story


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


def generate_new_char():
    while True:
        clear_terminal()
        print(textwrap.fill(gen_name(), width=75))
        print("\n")
        print(textwrap.fill(gen_history(), width=75))
        print("\n")
        user_input = input("Do you like this character (Y/N)? ").upper()
        if user_input == "Y":
            break
        while True:
            if user_input != "N" and user_input != "Y":
                user_input = input("Do you like this character (Y/N)? ").upper()
            else:
                break
