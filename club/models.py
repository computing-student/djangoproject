from django.db import models
import datetime
from django.utils import timezone
    


class Usuaris(models.Model):
    nom = models.CharField(max_length=200)
    cognoms = models.CharField(max_length=200)
    edat = models.IntegerField(max_length=3)
    estudis = models.CharField(max_length=200)


class Reserves(models.Model):
    usuari = models.ForeignKey(Usuaris, on_delete=models.CASCADE)
    date = models.DateField(_("Date"), default=datetime.date.today)


class Material(models.Model):
    producte = models.CharField(max_length=200)
    ubicacio = models.IntegerField(max_length=3)
    aula = models.CharField(max_length=200)


class Reserves_Material(models.Model):
    reserva = models.ForeignKey(Reserves, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)


class Aules(models.Model):
    planta = models.IntegerField(max_length=3)
    mida = models.IntegerField(max_length=3)
    disponibilitat = models.BooleanField(initial=True)