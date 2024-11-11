from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.prompt import Prompt
from rich.table import Table

def main():
    print("NHL statistics by nationality")
    while True:
        season = Prompt.ask("Select season [bright_magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/bright_magenta]")
        if season in ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]:
            break

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask("Select nationality [bright_magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/][/bright_magenta]")
        if nationality == "exit":
            break
        if nationality in ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", "BLR", "SLO", "USA", "FIN", "GBR"]:
            players = stats.top_scorers_by_nationality(nationality)
            table = Table(title=f"Top scorers of {nationality} season {season}")
            table.add_column("name", style="bright_cyan")
            table.add_column("team", style="purple3")
            table.add_column("goals", style="green3")
            table.add_column("assists", style="green3")
            table.add_column("points", style="green3")

            for player in players:
                table.add_row(player.name, player.team, str(player.goals), str(player.assists), str((player.goals + player.assists)))

            print(table)

if __name__ == "__main__":
    main()
