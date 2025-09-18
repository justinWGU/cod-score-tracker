from django.db import models
from django.contrib.auth.models import User


class Match(models.Model):
    scheduled_time = models.DateTimeField(null=True, blank=True)
    right_team = models.CharField(blank=True)
    left_team = models.CharField(blank=True)
    leftTeamScore = models.IntegerField(null=True, blank=True)
    rightTeamScore = models.IntegerField(null=True, blank=True)

class Map(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)
    map = models.CharField(blank=True)
    mode = models.CharField(blank=True)