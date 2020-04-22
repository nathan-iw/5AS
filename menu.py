from src.player import Player
import src.load as load
from src.ETL.persistence import Database
from unittest.mock import Mock, patch
from src.TeamClass import Team
import src.ETL.transform as transform
import src.ETL.extract as extract
# import src.TeamClass.Team
import time 

players = []
class App():
    def __init__(self, db):
        self.db = db

    def menu(self):
        while True:
            menu_choice = input(
                f"Options: \n[1] Would you like to add a new player \n[2] Would you like to print a list of players \n[3] Create Gang \nEnter here: ")
            if menu_choice == "1":
                self.add_player(players)
            elif menu_choice == "2":
                self.print_players()
            elif menu_choice == "3":
                self.create_team()
            else:
                db.save_players(players)
                exit()


    def save_csv_customers(self, db, csv_file):
        dirty_customers = extract.csv_load(csv_file)
        clean_customers = transform.process_customers(dirty_customers)
        db.save_to_db(clean_customers)

    def add_player(self, players):
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


    def print_players(self):
        number = 0
        for player in players:
            print(f"select {number} for {player.get_player_info()}")
            number += 1


    def create_team(self):
        self.print_players()
        team_captain_index = int(input("Which hustler would you to be the lead pimp? "))
        team_name = input("What would you like to call this posse? ")
        new_team = Team(team_name, players[team_captain_index])
        while True:
            player_index = int(input("Who would you like to join your crew? "))
            if player_index == "":
                self.menu()
            team_full = new_team.add_player_to_team(players[player_index])
            if team_full:
                self.menu()
        print()


if __name__ == "__main__": # the file you run in command line becomes main by default so this 'if' function only applies if you run `python3 menu.py` 
# so this if block is used, otherwise you'd be importing menu as a module, therefore __name__ == menu and this 'if' block would be ignored
    # players = persistence.load_players()
    # menu()
    # print("menu is main")
    # dirty_customers = extract.csv_load("short_customers.csv")
    # clean_customers = transform.process_customers(dirty_customers)
    db = Database()
    app = App(db)
    # app.menu()
    start = time.time()

    app.save_csv_customers(db, "short_customers.csv")
    customers = db.load_customers()
    for customer in customers:
        customer.print_summary()

if "test_menu.py" == "__main__":
    db = Mock(Database)
