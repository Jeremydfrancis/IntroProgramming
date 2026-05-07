"""
Jeremy Francis
2026_03_18
Main File
"""

import player
import board
import treasure
from my_utilities import *
import math
import art
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console = Console()
def get_valid_choice(message, valid_options):
    """Loops until the user enters a valid option from the given set."""
    while True:
        user_input = input(message).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid option. Please choose from: {', '.join(valid_options)}")

def command_player(board, player):
    """Gets player movement input and returns the direction or command."""
    direction = get_valid_choice(
        "Move: ",
        {"w", "s", "a", "d", "exit", "t", "c","h"}
    )
    if direction == "exit":
        return "exit", player
    if direction == "t":
        return "treasure", player
    if direction == "c":
        return "character", player
    if direction == "h":
        return "help", player
    return move_player(board, player, direction)

def check_movement(board, player):
    """Checks if the player's position is within the board boundaries."""
    row_length = len(board)
    column_length = len(board[0])
    if 0 <= player["row"] < row_length and 0 <= player["column"] < column_length:
        return True
    return False

def move_player(board, player, direction):
    """Moves the player on the board in the given direction with wraparound."""
    board[player["row"]][player["column"]] = "🔳"
    if direction == "w":
        player["row"] -= 1
    elif direction == "s":
        player["row"] += 1
    elif direction == "a":
        player["column"] -= 1
    elif direction == "d":
        player["column"] += 1
    player["row"] = player["row"] % len(board)
    player["column"] = player["column"] % len(board[0])
    board[player["row"]][player["column"]] = "🧙"
    return board, player
def print_combat_stats(my_player,enemy,player_misses,enemy_misses,player_dmg_tot,enemy_dmg_tot,player_health,enemy_health):
    """Displays a 'rich' table showing final combat stats for player and enemy."""
    stats_table = Table(title="  FINAL COMBAT STATS  ")
    stats_table.add_column("Player", style="cyan", justify="center")
    stats_table.add_column("Enemy", style="red", justify="center")
    stats_table.add_row(my_player['name'], enemy['name'])
    stats_table.add_row(f"Misses: {player_misses}", f"Misses: {enemy_misses}")
    stats_table.add_row(f"Damage: {player_dmg_tot}", f"Damage: {enemy_dmg_tot}")
    stats_table.add_row(f"Health: {player_health}", f"Health: {enemy_health}")
    console.print(stats_table, justify="center")

def combat(my_player, enemy):
    """Runs the combat loop between player and enemy, returns True if player wins, False if player dies."""
    player_health = my_player['health']
    player_attack = my_player['attack']
    player_defense = my_player['defense']
    enemy_health = enemy['health']
    enemy_attack = enemy['attack']
    enemy_defense = enemy['defense']
    player_misses = 0
    player_dmg_tot = 0
    enemy_misses = 0
    enemy_dmg_tot = 0

    while player_health > 0 and enemy_health > 0:
        clear_terminal()
        player_attack_roll = random.randint(1, 20)
        enemy_attack_roll = random.randint(1, 20)
        player_attack_bonus = math.trunc(player_attack / 5)
        enemy_attack_bonus = math.trunc(enemy_attack / 5)
        player_defense_bonus = math.trunc(player_defense / 5)
        enemy_defense_bonus = math.trunc(enemy_defense / 5)

        table = Table(title="  COMBAT  ", title_style="blue")
        table.add_column("Player", style="cyan", justify="center")
        table.add_column("Enemy", style="red", justify="center")
        table.add_row(my_player['name'], enemy['name'])
        table.add_row(f"[red]HP[/red]: {player_health}", f"[red]HP[/red]: {enemy_health}")
        table.add_row(f"[orange1]ATK[/orange1]: {player_attack}", f"[orange1]ATK[/orange1] {enemy_attack}")
        table.add_row(f"[green]DEF[/green]: {player_defense}", f"[green]DEF[/green] {enemy_defense}")
        console.print(table, justify="center")
        choose_attack = get_valid_choice(
            "\n\nChoose your attack:\n(P)ower Attack\n(Q)uick Attack\n(C)ounterattack\n(N)ormal Attack\n",
            {"p", "q", "c", "n"}
        )
        if choose_attack == 'p':
            player_attack_bonus *= 2
            enemy_attack_bonus *= 1.5
        elif choose_attack == 'q':
            player_attack_bonus *= 2
            enemy_defense_bonus *= 1.5
        elif choose_attack == 'c':
            player_defense_bonus *= 2.5
            player_attack_bonus = 0
        elif choose_attack == 'n':
            pass

        player_damage = math.trunc(player_attack_roll + player_attack_bonus - enemy_defense_bonus - 10)
        if player_damage <= 0:
            console.print("[yellow]>> Your attack missed![/yellow]")
            player_misses += 1
        else:
            enemy_health -= player_damage
            enemy["health"] = enemy_health
            player_dmg_tot += player_damage
            console.print(f"[green]>> You dealt {player_damage} damage![/green]")

        enemy_damage = math.trunc(enemy_attack_roll + enemy_attack_bonus - player_defense_bonus - 10)
        if enemy_damage <= 0:
            console.print("[green]>> You dodged the enemy's attack![/green]")
            enemy_misses += 1
        else:
            player_health -= enemy_damage
            my_player["health"] = player_health
            enemy_dmg_tot += enemy_damage
            console.print(f"[red]>> Enemy dealt {enemy_damage} damage![/red]")

        input("\nPress Enter to continue...")

    if player_health <= 0:
        clear_terminal()
        console.print(f"[bold red]{art.game_over}[/bold red]", justify="center")
        console.print(f"[bold red]You found {len(my_player['treasure_found'])} major treasures.[/bold red]", justify="center")
        print_combat_stats(my_player,enemy,player_misses,enemy_misses,player_dmg_tot,enemy_dmg_tot,player_health,enemy_health)
        input("\nPress Enter to continue...")
        return False
    if enemy_health <= 0:
        clear_terminal()
        console.print(f"[bold green]{enemy['name']} has been defeated![/bold green]\n\n",justify="center")
        print_combat_stats(my_player,enemy,player_misses,enemy_misses,player_dmg_tot,enemy_dmg_tot,player_health,enemy_health)
        input("\nPress Enter to continue...")
        return True
    return None

def help_screen():
    """Displays the help screen information."""
    clear_terminal()
    console.print("[bold yellow]--- HOW TO PLAY ---[/bold yellow]\n", justify="center")
    console.print("[cyan]GOAL:[/cyan] Find 8 major treasures to win the game.\n", justify="center")
    console.print("[cyan]CONTROLS:[/cyan]", justify="center")
    console.print("  'W' - Move Up", justify="center")
    console.print("  'S' - Move Down", justify="center")
    console.print("  'A' - Move Left", justify="center")
    console.print("  'D' - Move Right", justify="center")
    console.print("  't' - View collected treasures", justify="center")
    console.print("  'c' - View your character", justify="center")
    console.print("  'exit' - Save and quit\n", justify="center")
    console.print("[cyan]GAMEPLAY:[/cyan]", justify="center")
    console.print("  Every move rolls a 1d6.", justify="center")
    console.print("  Roll a 6: Find a minor treasure that boosts your stats.", justify="center")
    console.print("  Roll a 1: Enemy encounter - fight or die!", justify="center")
    console.print("  Major treasure is placed randomly - find it to add to your collection.", justify="center")
    console.print("  Once found, a new major treasure spawns somewhere on the map.\n", justify="center")
    console.print("[cyan]COMBAT:[/cyan]", justify="center")
    console.print("  Choose Power, Quick, Counterattack, or Normal attack each round.", justify="center")
    console.print("  Outlast the enemy's HP to survive. Reach 0 HP and it's game over.\n", justify="center")
    input("Press Enter to continue...")

def show_game_details(my_player, created_board):
    """Displays the board, player stats, and controls stacked vertically."""
    board_str = board.show_board(created_board)
    board_panel = Panel(board_str, title="[bold yellow]Map[/bold yellow]", border_style="red")
    stats_table = Table(title="[bold cyan]Player Stats[/bold cyan]", border_style="cyan", show_header=False)
    stats_table.add_column("", justify="left", style="white")
    stats_table.add_column("", justify="left", style="white")
    stats_table.add_row("[cyan]Position[/cyan]", f"Row: {my_player['row']}  Col: {my_player['column']}")
    stats_table.add_row("[yellow]Treasures Found[/yellow]", f"{len(my_player['treasure_found'])}/8")
    stats_table.add_row("[red]HP[/red]", str(my_player['health']))
    stats_table.add_row("[orange1]ATK[/orange1]", str(my_player['attack']))
    stats_table.add_row("[green]DEF[/green]", str(my_player['defense']))
    controls_table = Table(title="[bold yellow]Controls[/bold yellow]", border_style="yellow", show_header=False)
    controls_table.add_column("", justify="center", style="white")
    controls_table.add_column("", justify="center", style="white")
    controls_table.add_column("", justify="center", style="white")
    controls_table.add_column("", justify="center", style="white")
    controls_table.add_row("w - Up", "s - Down", "a - Left", "d - Right")
    controls_table.add_row("t - Treasures", "c - Character", "h - Help", "exit - Quit")
    console.print(board_panel, justify="center")
    console.print(stats_table, justify="center")
    console.print(controls_table, justify="center")
def game_loop(my_player,created_board,treasure_location):
    """Main game loop handling movement, combat, treasure, and win or loss conditions."""
    player_name = my_player['name']
    while True:
        last_board = created_board
        created_board, my_player = command_player(created_board, my_player)
        if created_board == "exit":
            print(f"Thanks for playing: {player_name}")
            if my_player["treasure_found"]:
                print("Treasures collected:")
                for item in my_player["treasure_found"]:
                    print(f"\t>\t{item}")
            else:
                print("You found no treasures.")
            save_name = input("Please enter a name for you save: ")
            save_game(my_player, last_board, treasure_location,save_name)
            break
        if created_board == "treasure":
            created_board = last_board
            if my_player["treasure_found"]:
                print("Treasures found so far:")
                for item in my_player["treasure_found"]:
                    print(f"\t>\t{item}")
            else:
                print("You have not found any treasures yet.")
            continue
        if created_board == "character":
            created_board = last_board
            if my_player:
                print(f"{my_player['name']}\n{my_player['history']}")
            else:
                print("No character data found")
            continue
        if created_board == "help":
            created_board = last_board
            help_screen()
            continue
        treasure_name = treasure_location["name"]
        check_minor = roll_target(1, 6,6)
        check_combat = roll_target(1, 6,1)
        if check_minor:
            clear_terminal()
            treasure.gen_minor_treasure(my_player)
        check_major = treasure.check_treasure(my_player, treasure_location)
        if check_major:
            clear_terminal()
            input(f"{treasure_name} found!")
            treasure_location = treasure.gen_treasure(created_board)
            if len(my_player["treasure_found"]) >= 8:
                console.print(art.win_screen, justify="center")
                console.print("[cyan]You have found all 8 major treasures![/cyan]", justify="center")
                break
        if check_combat:
            enemy = player.gen_enemy(1)
            battle = combat(my_player,enemy)
            if not battle:
                break
        clear_terminal()
        show_game_details(my_player,created_board)

def main():
    """Entry point of the program - shows title screen, handles new/load game, and starts the game loop."""
    console.print(f"[bold red1]{art.title_screen}[/bold red1]\n\n{art.author}", justify="center")
    console.print("\n\n[bold yellow]Find 8 major treasures to win![/bold yellow]", justify="center")
    console.print("\n\n[cyan]Press H for Help or Enter to continue...[/cyan]", justify="center")
    choice = input().strip().lower()
    if choice == "h":
        help_screen()
    try:
        load_option = input("Do you want to create a (n)ew game or (l)oad a past game? : ")
        while True:
            if load_option != "n" and load_option != "l":
                print(f"{load_option} is not a valid option")
                continue
            else:
                break
        if load_option == "l":
            print("--Saved Games--")
            show_saves()
            selected_game = input("Please enter the name of the game you would like to load: ")
            game_data = load_game(selected_game)
            if game_data is None:
                print("No save file found, starting new game...")
                load_option = "n"
            else:
                my_player = game_data['player']
                created_board = game_data['board']
                treasure_location = game_data['treasure']
                clear_terminal()
                show_game_details(my_player,created_board)
                game_loop(my_player, created_board, treasure_location)
        if load_option == "n":
            clear_terminal()
            my_player = player.generate_char_info(player)
            rows_message = "Please enter the number of rows you would like to generate: "
            columns_message = "Please enter the number of columns you would like to generate: "
            rows = board.get_positive_integer(rows_message)
            columns = board.get_positive_integer(columns_message)
            created_board = board.create_board(rows, columns)
            created_board, my_player = board.place_player_random(created_board, my_player)
            clear_terminal()
            treasure_location = treasure.gen_treasure(created_board)
            show_game_details(my_player,created_board)
            game_loop(my_player, created_board, treasure_location)
    except ValueError as error:
        print(f"{error} is not a valid option")





if __name__ == "__main__":
    main()