from django.db import migrations
import csv

def load_initial_data(apps, schema_editor):
    Player = apps.get_model('TopScorers', 'Player')  # Model Player
    Club = apps.get_model('TopScorers', 'Club')  # Model Club
    Stats = apps.get_model('TopScorers', 'Stats')  # Model Stats

    with open('Data.csv', 'r', encoding='utf-8') as file:
        data = csv.DictReader(file)
        for row in data:
            # Wczytaj dane dla modelu Player
            player = Player.objects.create(
                player_name=row['Player Names']
            )

            # Wczytaj dane dla modelu Club
            club = Club.objects.create(
                country=row['Country'],
                league=row['League'],
                club=row['Club']
            )

            # Wczytaj dane dla modelu Stats
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

class Migration(migrations.Migration):

    dependencies = [
        ('TopScorers', '0002_clear_tables'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
