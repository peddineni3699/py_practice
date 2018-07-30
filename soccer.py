
import csv


if __name__ == "__main__":


    # Clear the teams output each time the script is run
    with open ("output/teams.txt", "w") as file:
        file.write("")

    teams = {"sharks": {"team_name": "Sharks", "roster": []},
            "dragons": {"team_name": "Dragons", "roster": []},
            "raptors": {"team_name": "Raptors", "roster": []}}


    def write_team_to_file(teams,group_name):
        with open("output/teams.txt", "a") as file:
            file.write("--- {} ---\n".format(teams[group_name]["team_name"]))
            for player in teams[group_name]["roster"]:
                file.write("{}, {}, {}\n".format(
                    player["name"],
                    player["experience"],
                    player["guardian(s)"]
                ))
            file.write("\n")


    def add_player_to_team(player, team):
        team["roster"].append(player)


    def experienced_players_on_team(team_name):
        experienced_players_on_team = 0
        for player in teams[team_name]["roster"]:
            if player["experience"] == "YES":
                experienced_players_on_team += 1
        return experienced_players_on_team

    # below function used to return list of dictionaries for experienced and inexperienced players
    def sorter_based_on_experience(kwargs, flag):
        player_pool = kwargs
        sort_flag = flag
        if sort_flag:
            return [item for item in player_pool if item.get('Soccer Experience') == 'YES']
        else:
            return [item for item in player_pool if item.get('Soccer Experience') == 'NO']

    # below logic used to group teams based on the rule that all the teams contain equal number of experienced and inexperienced players

    def get_experienced_players_count(players):
        number_of_experienced_players = 0
        for player in players:
            if player["Soccer Experience"] == "YES":
                number_of_experienced_players += 1
        return number_of_experienced_players


    with open("test.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        a = list(reader)

        players_per_team = len(a) // len(teams)
        experienced_player_per_team = get_experienced_players_count(a) // len(teams)


        for soccer_player in a:
            player_info = { "name": soccer_player["Name"],
                            "experience": soccer_player["Soccer Experience"],
                            "guardian(s)": soccer_player["Guardian Name(s)"]}
            if player_info["experience"] == "YES":
                if experienced_players_on_team("sharks") < experienced_player_per_team:
                    add_player_to_team(player_info, teams["sharks"])
                elif experienced_players_on_team("dragons") < experienced_player_per_team:
                    add_player_to_team(player_info, teams["dragons"])
                else:
                    add_player_to_team(player_info, teams["raptors"])

            else:
                if len(teams["sharks"]["roster"]) - experienced_players_on_team(
                        "sharks") < players_per_team - experienced_player_per_team:
                    add_player_to_team(player_info, teams["sharks"])
                elif len(teams["dragons"]["roster"]) - experienced_players_on_team(
                        "dragons") < players_per_team - experienced_player_per_team:
                    add_player_to_team(player_info, teams["dragons"])
                else:
                    add_player_to_team(player_info, teams["raptors"])

    #writing into text file
    write_team_to_file(teams, "sharks")
    write_team_to_file(teams, "dragons")
    write_team_to_file(teams, "raptors")