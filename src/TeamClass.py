class Team:
    def __init__ (self, team_name, team_captain):
        self.team_name = team_name
        self.team_captain = team_captain
        self.team_members = [team_captain]

    def add_player_to_team(self, player):
        if len(self.team_members) < 7:
            self.team_members.append(player)
            print("gangsta has been added, for real")
            self.whos_rollin()
            return False
        else:
            self.whos_rollin()
            print("This team is whack! But's it's full now fam!")
            return True

    def whos_rollin(self):
        print("you're already rollin' with these playa's:")
        self.print_team_members()

    def print_team_members(self):
        for gangsta in self.team_members:
            print(gangsta.name)
