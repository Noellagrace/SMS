from django.db import models

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

    def __str__(self):
        return self.code
    

class PersonnelAD(models.Model):
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
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=25)

    def __str__(self):
        return self.nom