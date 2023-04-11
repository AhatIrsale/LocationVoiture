from django.db import models
class Modele(models.Model):
    age_minimum= models.IntegerField()
    airbag =  models.CharField(max_length=50)
    capacitie = models.FloatField()
    attach_cat = models.CharField(max_length=40)
    clim = models.BooleanField()
    denomination = models.IntegerField
    marque = models.CharField()
    nb_passag = models.IntegerField()
    nb_perms = models.IntegerField()
    type = models.CharField(max_length=50)
    version= models.IntegerField()
    cat = models.CharField(max_length=60)

class Agence(models.Model):
    description =  models.CharField(max_length=50)
    prove = models.CharField(max_length=500)
    slug = models.CharField(max_length=30)

class Voiture(models.Model):
    matricule = models.CharField(max_length=50)
    modele = models.ForeignKey(Modele,on_delete=models.CASCADE())
    Agence = models.ForeignKey(Agence,on_delete=models.CASCADE())
# Create your models here.
