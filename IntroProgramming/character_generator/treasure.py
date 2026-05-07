"""
Jeremy Francis
2026_04_17
treasure.py
"""
import random
from my_utilities import roll_dice
minor_treasure_names = [
"A Bag of Suspiciously Warm Coins",
"Somebody Else's Wedding Ring",
"A Map That Is Probably Wrong",
"Three Gold Coins and a Button",
"An IOU From a Dead King",
"A Perfectly Normal Rock (It Is Not Normal)",
"Half a Diamond (The Good Half)",
"A Jar of Something Glowing",
"Expired Adventurer's Guild Card",
"A Boot With Something Inside It",
"Directions to Somewhere Dangerous",
"A Crown That Is Slightly Too Big",
"Someone's Lucky Rabbit (Just the Foot)",
"A Very Heavy Envelope, Sealed",
"The Wrong Map to the Right Place",
"A Coin That Keeps Coming Back",
"A Trophy for Second Place",
"An Ancient Coupon of Unknown Value",
"A Key With No Obvious Lock",
"A Letter That Reads Only 'Run'"]
major_treasure_names = [
    "👑 The Crown of the Ancient Empire",
    "⚔️ Sword of the Fallen General",
    "🔮 The Orb of Eternal Sight",
    "🛡️ Armor of the Last Guardian",
    "🛡️ The Aegis of the Iron Throne",
    "🗡️ Blade of the First King",
    "🪄 The Staff of High Sorcery",
    "🥊 Gauntlets of the Warlord",
    "📖 The Tome of Forbidden Knowledge",
    "🪑 Throne Fragment of the Lost Dynasty",
    "⚔️ The Sword of the Chosen",
    "👢 Boots of the Shadow Walker",
    "⛑️ The Helmet of the Undying",
    "🧥 Cloak of the Phantom King",
    "📿 The Amulet of Ancient Power",
    "🏹 Bow of the Eternal Hunter",
    "🏆 The Chalice of Immortality",
    "⚔️ Armor of the God Slayer",
    "🪓 The Axe of the Mountain King",
    "🔱 Scepter of the Fallen Empire"
]
def gen_treasure(board):
    """Generates a random major treasure at a random location on the board."""
    treasure={"row":0,"col":0, "name":""}
    ran_row = random.randint(0,len(board)-1)
    ran_col = random.randint(0,len(board[0])-1)
    ran_name = random.choice(major_treasure_names)
    treasure["row"]=ran_row
    treasure["col"]=ran_col
    treasure["name"]=ran_name
    return treasure

def gen_minor_treasure(player):
    """Randomly selects a minor treasure and boosts a random stat for player."""
    ran_name = random.choice(minor_treasure_names)
    player_stats = ["health", "defense", "attack"]
    pick_stat = random.choice(player_stats)
    if pick_stat == "health":
        total = roll_dice(2,4)
        player["health"]+= total
        input(f"Minor Treasure: You found {ran_name}: +{total} to your character's {pick_stat.upper()}!")
    else:
        total = roll_dice(1,4)
        if pick_stat == "defense":
            player["defense"]+= total
        if pick_stat == "attack":
            player["attack"] += total
        input(f"Minor Treasure: You found {ran_name}: +{total} to your character's {pick_stat.upper()}!")





def check_treasure(player,treasure):
    """Checks if the player is on the major treasure location and adds it to player['treasure_found']."""
    player_row = player["row"]
    player_col = player["column"]
    treasure_row =treasure["row"]
    treasure_col = treasure["col"]
    treasure_name = treasure["name"]
    if (player_row == treasure_row) and (player_col == treasure_col):
        player["treasure_found"].append(treasure_name)
        return True
    else:
        return False



