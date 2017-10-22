from sys import argv
# Read the WYSS section for how to run this
script_name, home_team_score, away_team_score, quarter, time_left, home_team, away_team = argv

print(f"*** {away_team} vs {home_team} ***")
print(f"*** {home_team} \t {home_team_score} ***")
print(f"*** {away_team} \t {away_team_score} ***")
print(f"*** Quarter: {quarter} \t {time_left} ***")
