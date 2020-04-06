from player import Player, players

def menu():
    menu_choice = input (f"Options: \n[1] Would you like to add a new player \n[2] Would you like to print a list of players \nEnter here: ")
    if menu_choice == "1":
        add_player()
    elif menu_choice == "2":
        print(players)
    else:
        print (f"error")
        SystemExit

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
    print(players)
    return new_player


if __name__ == "__main__":
    while True:
        menu()