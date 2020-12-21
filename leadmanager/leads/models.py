from django.db import models


class PersonManager(models.Manager):
    def get_fun_people(self):
        print(self)


class Lead(models.Model):
    name = models.CharField(max_length=100)
    objects = PersonManager.get_fun_people('r')
