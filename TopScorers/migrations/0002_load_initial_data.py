import csv

from django.db import migrations

from ..models import Player, Club, Stats


def load_initial_data(apps, schema_editor):
    with open('Data.csv', 'r', encoding='utf-8') as file:
        data = csv.DictReader(file)
        for row in data:
            # Wczytaj dane dla modelu Club
            player_club = Club.objects.create(
                country=row['Country'],
                league=row['League'],
                club_name=row['Club']
            )

            # Wczytaj dane dla modelu Stats
            player_stats = Stats.objects.create(
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

            # Wczytaj dane dla modelu Player i połącz z klubem oraz statystykami
            Player.objects.create(
                player_name=row['Player Names'],
                club=player_club,
                stats=player_stats
            )


class Migration(migrations.Migration):
    dependencies = [
        ('TopScorers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
