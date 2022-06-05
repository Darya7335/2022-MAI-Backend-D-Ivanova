from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50, null=False)


class Director(models.Model):
    name = models.CharField(max_length=50, null=False)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

