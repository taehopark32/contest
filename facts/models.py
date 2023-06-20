from django.db import models

# Create your models here.
class AnimalFact(models.Model):
    info = models.CharField(max_length=200)
    def __str__(self):
        return self.info
 
class CapitalFact(models.Model):
    info = models.CharField(max_length=200)
    def __str__(self):
        return self.info