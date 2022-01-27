from django.db import models

# Create your models here.

class T1Score(models.Model):
    Level = models.CharField(max_length=100, null=False, blank=False)
    point = models.IntegerField()

    def __str__(self):
        return f'{self.Level} - {self.point}'

class T2Score(models.Model):
    Level = models.CharField(max_length=100, null=False, blank=False)
    point = models.IntegerField()

    def __str__(self):
        return f'{self.Level} - {self.point}'