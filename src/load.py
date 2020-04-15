import csv
from player import Player

def save_player(players, player_file):
    try:
        with open(player_file,"w") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for player in players:
                
                csv_writer.writerow([player.name.title(),player.age, player.foot.capitalize(),player.gender.capitalize(),player.player_status])
    except Exception as error:
        print(f"Seriously, again??? {error}")

def load_players(player_file):
    players = []
    try:
        with open(player_file,"r") as csv_file:
           rows = csv.reader(csv_file, quoting=csv.QUOTE_ALL, skipinitialspace=True)
           for row in rows:
                if row[4] == "True":
                   row[4] = True
                else:
                   row[4] = False
                players.append(Player(row[0],int(row[1]),row[2],row[3],row[4]))
        return players
    except Exception as error:
        print(error)