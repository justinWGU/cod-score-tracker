from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Match(models.Model):
    leftTeamScore = models.IntegerField(null=True, blank=True)
    rightTeamScore = models.IntegerField(null=True, blank=True)
