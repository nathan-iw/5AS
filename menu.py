from player import Player
import load

def menu():
    while True:
        menu_choice = input (f"Options: \n[1] Would you like to add a new player \n[2] Would you like to print a list of players \nEnter here: ")
        if menu_choice == "1":
            add_player()
        elif menu_choice == "2":
            print_players()
        else:
            load.save_player(players, "player_list.csv")
            exit()
    

def add_player():
    player_name = input ("Whom would one like to add? ")
    player_age = input ("How aged is the player ")
    player_foot = input ("Upon which foot does he ball? ")
    player_gender = input ("Are they male, female or prefer not to say? ")
    player_status = input ("Can the player ball? [Y/N] ")
    if player_status == "Y":
        player_status = True
    else:
        player_status = False
    new_player = Player(player_name, int(player_age), player_foot, player_gender, player_status)
    players.append(new_player)
    return new_player

def print_players():
    for player in players:
        print(player.get_player_info())


if __name__ == "__main__":
    players = load.load_players("player_list.csv")
    menu()