from django.db import models


class Resource(models.Model):
    #  Auto-incrementing 'id' field is automatically set by Django
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
