# import csv
# from TopScorers.models import Player, Club, Stats
#
# with open('Data.csv', 'r', encoding='utf-8') as file:
#     data = csv.DictReader(file)
#     for row in data:
#         # Tworzenie klubu
#         club, created = Club.objects.get_or_create(
#             country=row['Country'],
#             league=row['League'],
#             club=row['Club']
#         )
#
#         # Tworzenie gracza
#         player = Player.objects.create(
#             player_name=row['Player Names']
#         )
#
#         # Tworzenie statystyk
#         stats = Stats.objects.create(
#             matches_played=row['Matches_Played'],
#             substitution=row['Substitution'],
#             mins=row['Mins'],
#             goals=row['Goals'],
#             xG=row['xG'],
#             xG_per_avg_match=row['xG Per Avg Match'],
#             shots=row['Shots'],
#             on_target=row['OnTarget'],
#             shots_per_avg_match=row['Shots Per Avg Match'],
#             on_target_per_avg_match=row['On Target Per Avg Match'],
#             year=row['Year']
#         )
#
#         # Powiązanie klubu, gracza i statystyk
#         player.club = club
#         player.stats = stats
#         player.save()


# Skrypt importujący dane z pliku CSV
import csv
from TopScorers.models import Player, Club, Stats

with open('Data.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file)
    for row in data:
        # Tworzenie klubu
        club, created = Club.objects.get_or_create(
            country=row['Country'],
            league=row['League'],
            club_name=row['Club']
        )

        # Tworzenie gracza
        player = Player.objects.create(
            player_name=row['Player Names'],
            club=club  # Przypisanie klubu do gracza
        )

        # Tworzenie statystyk
        stats = Stats.objects.create(
            matches_played=row['Matches_Played'],
            substitution=row['Substitution'],
            mins=row['Mins'],
            goals=row['Goals'],
            xG=row['xG'],
            xG_per_avg_match=row['xG Per Avg Match'],
            shots=row['Shots'],
            on_target=row['OnTarget'],
            shots_per_avg_match=row['Shots Per Avg Match'],
            on_target_per_avg_match=row['On Target Per Avg Match'],
            year=row['Year']
        )

        # Przypisanie klubu i statystyk do gracza
        player.club = club
        player.stats = stats
        player.save()
