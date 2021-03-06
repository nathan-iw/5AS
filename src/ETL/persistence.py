import pymysql
from src.player import Player
from src.TeamClass import Team
from os import environ
from src.ETL.customer import Customer

class Database():
    def get_connection(self): # function to get the connection string using: pymysql.connect(host, username, password, database) 
        db_connection = pymysql.connect(
            environ.get("DB_HOST"), #host
            environ.get("DB_USER"), #username
            environ.get("DB_PW"), #password
            environ.get("DB_NAME") #database
            )
        return db_connection

    def load_players(self): # function to run a select query like `SELECT * FROM players`
        connection = self.get_connection()
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

    def load_customers(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer")
        customers = []

        while True:
            row = cursor.fetchone()
            if row == None:
                break
            customer = Customer(row[1],row[2],row[3],row[4],row[5],row[0])
            customers.append(customer)

        cursor.close()
        connection.close()
        return customers

                
    # title, first_name, last_name, age, ccn, id=None

    # function to save the name and titles of people to data base.
    def save_to_db(self, customers):
        connection = self.get_connection()
        cursor = connection.cursor()
        for customer in customers:
            cursor.execute(
            """INSERT INTO customer (title, first_name, last_name, age, ccn) 
                    VALUES (%s, %s, %s,%s, %s)""", customer)
        connection.commit()
        cursor.close()
        connection.close()

    def save_players(self, players):
        connection = self.get_connection()
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
