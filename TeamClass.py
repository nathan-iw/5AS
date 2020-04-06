class Team:
    def __init__ (self, team_name, team_captain):
        self.team_name = team_name
        self.team_captain = team_captain
        self.team_members = [team_captain]

    def add_player_to_team(self, player):
        if len(self.team_members) < 7:
            self.team_members.append(player)
            print(f"gangsta has been added, for real")
            print(f"you're rollin' with these playa's {self.print_team_members()}")
        else:
            print(f"you're already rollin' with these playa's {self.print_team_members()}\nTeam is on and poppin'")

    def print_team_members(self):
        for gangsta in self.team_members:
            print(gangsta.name)