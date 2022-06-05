from django.db import models
from django.urls import reverse


class Country(models.Model):
    CountryName = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('Country', kwargs={'Country': self.CountryID})

class Director(models.Model):
    DirectorName = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.DirectorName


    def get_url(self):
        return reverse('Director', kwargs={'Director': self.DirectorID})

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    CountryID = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    DirectorID = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
