from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title