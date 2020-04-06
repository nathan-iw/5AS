### 5 A Side ###
# What attributes do we need to know about a player?
# Create a function to return a string giving the player's info

# Name
# Age
# L/R
# Gender
# Status (Playing/ Not)

#Gary McTest is male, age 7, both-footed and currently able to play."

def player(name, age, foot, gender, player):
    if player == False:
        aval = "unable"
    else:
        aval = "able"
    return f"{name} is {gender.lower()}, age {age}, {foot.lower()}-footed and currently {aval} to play."
    

# print(player("Gaz",65,"Right","Female",True))