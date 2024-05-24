from django.db import models
from gestion_notes.models import *

# Create your models here.
class Classe(models.Model):
    code = models.CharField(max_length=25)
    libelle = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.code
    


class Matiere (models.Model):
    classe = models.ForeignKey('gestion_utilisateur.classe', on_delete = models.CASCADE)
    code = models.CharField(max_length=5)
    libelle = models.CharField(max_length=255)
    coeficient = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))
    enseignant = models.ForeignKey('gestion_utilisateur.Enseignant', on_delete = models.CASCADE)

    def __str__(self):
        return self.libelle
    

class Semestre(models.Model):
    id_semestre = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Evaluation(models.Model):
    type = models.CharField(max_length = 100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE)

    def __str__(self):
        return self.type


class Note(models.Model):
    notes = models.IntegerField()
    eleve = models.ForeignKey('gestion_utilisateur.Eleve', on_delete = models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete = models.CASCADE)
    evalution = models.ForeignKey(Evaluation, on_delete = models.CASCADE)