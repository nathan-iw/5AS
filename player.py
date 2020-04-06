## 5 A Side ###
# What attributes do we need to know about a player?
# Create a function to return a string giving the player's info

# Name
# Age
# L/R
# Gender
# Status (Playing/ Not)

# Gary McTest is male, age 7, both-footed and currently able to play."

players = []

class Player:
    def __init__(self, name, age, foot, gender, player):
        self.name = name
        self.age = age
        self.foot = foot
        self.gender = gender 
        self.player = player 

    def get_player_info(self):
        if self.player == False:
            aval = "unable"
        else:
            aval = "able"
        return f"{self.name} is {self.gender.lower()}, age {self.age}, {self.foot.lower()}-footed and currently {aval} to play."

    
    

# print(player("Gaz",65,"Right","Female",True))