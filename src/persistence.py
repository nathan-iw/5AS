import pymysql
from src.player import Player
from src.TeamClass import Team


def get_connection(): # function to get the connection string using: pymysql.connect(host, username, password, database) 
    db_connection = pymysql.connect(
        supersecret.db_host, #host
        supersecret.user_name, #username
        supersecret.password, #password
        supersecret.database #database
        )
    return db_connection

def load_players(): # function to run a select query like `SELECT * FROM players`
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM player")
    players = []
      
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        player = Player(row[1],row[2],row[3],row[4],row[5],row[0]) # row 0 last because it's a default 
        players.append(player)
       
    cursor.close()
    connection.close()
    return players

def save_players(players):
    connection = get_connection()
    cursor = connection.cursor()
    for player in players:
        if player.id == None:
            args = (player.name, player.age, player.foot, player.gender, player.player_status)
            cursor.execute("INSERT INTO player (name, age, foot, gender, status) VALUES (%s, %s, %s, %s, %s)", args) # %s prevents SQL injection!
    connection.commit()
    cursor.close()
    connection.close()

# function to run an update query like `INSERT INTO players ...`

# function to use the above to load players from DB

# Function to use the above to save players to DB  








