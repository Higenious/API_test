from django.db import models
#from  django import views


class Stock(models.Model):
       ticker = models.CharField(max_length=10)
       open = models.FloatField()
       close = models.FloatField()
       volume = models.IntegerField()


       def __str__(self):
            return self.ticker
