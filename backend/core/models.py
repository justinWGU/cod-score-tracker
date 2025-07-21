from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Match(models.Model):
    scheduled_time = models.DateTimeField(null=True, blank=True)
    right_team = models.CharField(blank=True)
    leftTeamScore = models.IntegerField(null=True, blank=True)
    rightTeamScore = models.IntegerField(null=True, blank=True)
    map_set = models

    # TODO: Create a new dev branch from main. Figure out how to properly create models
class Map(models.Model):
    map = models.CharField(blank=True)
    mode = models
