from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

from gestion_utilisateur.utiles import generer_matricule

class Annee_scolaire(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    anneescolaire = models.CharField(max_length=25)

    def __str__(self):
        return self.anneescolaire 


class Classe(models.Model):
    code = models.CharField(max_length=25)
    libelle = models.CharField(max_length=50)
    montant = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.code
    


class Poste(models.Model):
    code = models.CharField(max_length=10)
    libelle = models.CharField(max_length=25) 

    def __str__(self):
        return self.libelle  



class Enseignant(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=25)
    def save(self, *args, **kwargs) -> None:
        if not self.matricule:
            self.matricule = generer_matricule(Enseignant)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom


class Eleve(models.Model):
    matricule = models.CharField(max_length=10)
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    date_naiss = models.DateField()
    adresse = models.CharField(max_length=25)
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)
    annee_scolaire = models.ManyToManyField(Annee_scolaire)
    def save(self, *args, **kwargs) -> None:
        if not self.matricule:
            self.matricule = generer_matricule(Eleve)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom


class Parent(models.Model):
    nom_pere = models.CharField(max_length=25)
    prenom_pere = models.CharField(max_length=25)
    nom_mere = models.CharField(max_length=25)
    prenom_mere = models.CharField(max_length=25)
    email_pere = models.EmailField()
    email_mere = models.EmailField()
    telephone_pere = models.CharField(max_length=15)
    telephone_mere = models.CharField(max_length=15)
    adresse = models.CharField(max_length=25)
    eleve = models.ForeignKey(Eleve, on_delete = models.CASCADE)
    def __str__(self):
        return self.nom_pere
 

class Personnel_ad(AbstractUser):
    matricule = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=25)
    poste = models.ForeignKey(Poste, on_delete = models.CASCADE, related_name='users', null=True, blank=True)

    def __str__(self):
        return self.username
    