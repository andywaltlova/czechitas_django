from django.db import models


class Organizace(models.Model):
    jmeno = models.CharField(max_length=100)
    ico = models.IntegerField()
    ulice = models.CharField(max_length=100)
    mesto = models.CharField(max_length=100)
    psc = models.IntegerField()


class Kontakt(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    datum_posledniho_kontaktu = models.DateTimeField()
    organizace = models.ForeignKey(
        Organizace, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.jmeno.__str__() + ' ' + self.prijmeni.__str__()
