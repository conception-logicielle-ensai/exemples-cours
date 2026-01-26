from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    """Modèle de base de données - représentation interne"""
    email = models.EmailField(unique=True, db_index=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
