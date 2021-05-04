from django.db import models


class Kategorie(models.Model):
    nazev = models.CharField(max_length=100)

class Kurz(models.Model):
    nazev = models.CharField(max_length=100)
    zacatek = models.DateTimeField()
    konec = models.DateTimeField()
    popis = models.CharField(max_length=1000)
    cena = models.IntegerField()
    kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.nazev)


class Prihlaska(models.Model):
    email = models.CharField(max_length=100)
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    motivace = models.TextField()
    kurz = models.ForeignKey(Kurz, on_delete=models.SET_NULL, null=True)
