from django.db import models
from . gen import Gen

# Create your models here.

class Scores(models.Model):
    team1 = models.IntegerField()
    team2 = models.IntegerField()

    def __str__(self):
        return f'{self.team1, self.team2}'

