from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.name
