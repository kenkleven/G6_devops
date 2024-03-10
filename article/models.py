from django.db import models

# Create your models here.
class Categorie(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Non active', 'Non active'),
    )
    nom = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.nom

class Article(models.Model):
    STATUS_CHOICES = (
        ('Actif', 'Actif'),
        ('Non actif', 'Non actif'),
    )
    nom = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS_CHOICES)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    date_update = models.DateTimeField(auto_now=True, null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nom
