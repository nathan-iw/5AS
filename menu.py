from player import Player
import load
from TeamClass import Team

players = []


def menu():
    while True:
        menu_choice = input(
            f"Options: \n[1] Would you like to add a new player \n[2] Would you like to print a list of players \n[3] Create Gang \nEnter here: ")
        if menu_choice == "1":
            add_player(players)
        elif menu_choice == "2":
            print_players()
        elif menu_choice == "3":
            create_team()
        else:
            load.save_player(players, "player_list.csv")
            exit()


def add_player(players):
    player_name = input("Whom would one like to add? ")
    player_age = input("How aged is the player ")
    player_foot = input("Upon which foot does he ball? ")
    player_gender = input("Are they male, female or prefer not to say? ")
    player_status = input("Can the player ball? [Y/N] ")
    if player_status == "Y":
        player_status = True
    else:
        player_status = False
    new_player = Player(player_name, int(player_age), player_foot, player_gender, player_status)
    players.append(new_player)
    return new_player


def print_players():
    number = 0
    for player in players:
        print(f"select {number} for {player.get_player_info()}")
        number += 1


def create_team():
    print_players()
    team_captain_index = int(input("Which hustler would you to be the lead pimp? "))
    team_name = input("What would you like to call this posse? ")
    new_team = Team(team_name, players[team_captain_index])
    while True:
        player_index = int(input("Who would you like to join your crew? "))
        if player_index == "":
            menu()
        team_full = new_team.add_player_to_team(players[player_index])
        if team_full:
            menu()
    print()


if __name__ == "__main__":
    players = load.load_players("player_list.csv")
    menu()
