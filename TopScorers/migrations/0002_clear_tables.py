from django.db import migrations

def clear_tables(apps, schema_editor):
    Player = apps.get_model('TopScorers', 'Player')  # Model Player
    Club = apps.get_model('TopScorers', 'Club')  # Model Club
    Stats = apps.get_model('TopScorers', 'Stats')  # Model Stats

    Player.objects.all().delete()
    Club.objects.all().delete()
    Stats.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('TopScorers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(clear_tables),
    ]
