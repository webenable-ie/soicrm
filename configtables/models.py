from django.db import models

# Create your models here.


class Sport(models.Model):
    sport = models.CharField(max_length=100)


class Region(models.Model):
    region = models.CharField(max_length=250)


class ClubType(models.Model):
    club_type = models.CharField(max_length=100)