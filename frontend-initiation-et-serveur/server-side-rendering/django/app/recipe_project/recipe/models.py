from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title