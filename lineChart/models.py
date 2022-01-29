from django.db import models

# Create your models here.

class Score(models.Model):

    T1A = models.IntegerField()
    T1AS = models.IntegerField()
    T1D = models.IntegerField()
    T1DS = models.IntegerField()
    T1ADS = models.IntegerField()
    T1ASQ = models.IntegerField()
    T1DSQ = models.IntegerField()
    T1ADSQ = models.IntegerField()

    T2A = models.IntegerField()
    T2AS = models.IntegerField()
    T2D = models.IntegerField()
    T2DS = models.IntegerField()
    T2ADS = models.IntegerField()
    T2ASQ = models.IntegerField()
    T2DSQ = models.IntegerField()
    T2ADSQ = models.IntegerField()


    def __str__(self):
        return f'{self.T1A+self.T1AS+self.T1D+self.T1DS+self.T1ADS, self.T2A+self.T2AS+self.T2D+self.T2DS+self.T2ADS}'

