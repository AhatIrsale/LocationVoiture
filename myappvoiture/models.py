from django.db import models
class Modele(models.Model):
    age_minimum= models.IntegerField()
    airbag =  models.CharField(max_length=50)
    capacitie = models.FloatField()
    attach_cat = models.CharField(max_length=40)
    clim = models.BooleanField()
    denomination = models.IntegerField()
    marque = models.CharField()
    nb_passag = models.IntegerField()
    nb_perms = models.IntegerField()
    type = models.CharField(max_length=50)
    version= models.IntegerField()
    cat = models.CharField(max_length=60)
    def __str__(self):
        return f"{self.version}"

class Agence(models.Model):
    description =  models.CharField(max_length=50)
    prove = models.CharField(max_length=500)
    slug = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.description}"

class Voiture(models.Model):
    matricule = models.CharField(max_length=50)
    modele = models.ForeignKey(Modele,on_delete=models.CASCADE())
    Agence = models.ForeignKey(Agence,on_delete=models.CASCADE())
    def __str__(self):
        return f"{self.matricule}"
class Client(models.Model):
    nom = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    car = models.ManyToManyField(Voiture,through='Reservation')
class Reservation(models.Model):
    voiture = models.ForeignKey(Voiture, on_delete=models.CASCADE())
    client = models.ForeignKey(Client, on_delete=models.CASCADE())
    dateStart = models.DateField()
    dateEnd = models.DateField()
    tarif = models.CharField(max_length=50)
    statusPayment = models.BooleanField(default=False)
# Create your models here.
