from django.db import models

# Create your models here.
class Molecule(models.Model):
    name = models.CharField(max_length=200)
    mass = models.FloatField(default=0)
    reference = models.CharField(max_length=200)
    ccs = models.FloatField(default=0)
    sdf_file = models.CharField(max_length=50000, default='none')

