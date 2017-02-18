from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from microlives.choices import *

class Team(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SiteUser(models.Model):
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES)
    birthday = models.DateField()

    def __str__(self):
        return self.user.username


class MicroLife(models.Model):
    risk_factor = models.CharField(max_length=255)
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES)
    valence = models.DecimalField(max_digits=5, decimal_places=2)
    source = models.CharField(max_length=255)

    def __str__(self):
        return "{factor} - {gender} - {valence}".format(
                                                    factor=risk_factor,
                                                    gender=gender,
                                                    valence=valence)


class Exposure(models.Model):
    microlife = models.ForeignKey(MicroLife)
    siteuser = models.ForeignKey(SiteUser)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return "{factor} - {user} - {date}".format(
                                                factor=microlife.risk_factor,
                                                user=siteuser.user.username,
                                                date=date
        )
