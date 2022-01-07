from os import makedev
from django.db import models


class Cars(models.Model):
    make = models.CharField(max_length = 100)
    model = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.name}'