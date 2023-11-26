from django.db import models

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=255)
    club = models.OneToOneField('Club', on_delete=models.CASCADE, null=True, blank=True)
    stats = models.OneToOneField('Stats', on_delete=models.CASCADE, null=True, blank=True)

class Club(models.Model):
    club_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=255)
    league = models.CharField(max_length=255)
    club_name = models.CharField(max_length=255)

class Stats(models.Model):
    stats_id = models.AutoField(primary_key=True)
    matches_played = models.IntegerField()
    substitution = models.IntegerField()
    mins = models.IntegerField()
    goals = models.IntegerField()
    xG = models.FloatField()
    xG_per_avg_match = models.FloatField()
    shots = models.IntegerField()
    on_target = models.IntegerField()
    shots_per_avg_match = models.FloatField()
    on_target_per_avg_match = models.FloatField()
    year = models.IntegerField()
