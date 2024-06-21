from django.db import models
from django.contrib.auth.models import User
from SMS import settings
from gestion_notes.models import *

# Create your models here.
class Classe(models.Model):
    code = models.CharField(max_length=25)
    libelle = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.code
    


class Matiere (models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=255)
    #coeficient = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))
    def __str__(self):
        return self.libelle
    

class Semestre(models.Model):
    id_semestre = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom


class Note(models.Model):

    eleve = models.ForeignKey('gestion_utilisateur.Eleve', on_delete=models.CASCADE, related_name='notes')
    evaluation = models.CharField(max_length=15)
    note = models.FloatField()
    note_coeficiee = models.FloatField()
    classe = models.ForeignKey('gestion_utilisateur.Classe', on_delete=models.CASCADE, related_name='notes')
    sequence = models.CharField(max_length=50)
    enseignant = models.ForeignKey('gestion_utilisateur.Professeur', on_delete=models.CASCADE, related_name='notes')
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name='notes')
    
    date = models.DateField()

    @property
    def note_coeficiee(self):
        return self.note * self.evaluation.coefficient

    def __str__(self):
        return f"{self.classe} - {self.matiere} - {self.eleve.nom}- {self.note}  - {self.evaluation} - - {self.sequence} "



# Optionally, to track changes for traceability
class NoteHistory(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='history')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    previous_value = models.FloatField()
    new_value = models.FloatField()    