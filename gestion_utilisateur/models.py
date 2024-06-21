from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from gestion_notes.models import Matiere 
from gestion_utilisateur.utiles import generer_matricule
from django.contrib.auth.hashers import make_password

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



class Eleve(models.Model):
    matricule = models.CharField(max_length=6, editable=False, default="")
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    date_naiss = models.DateField()
    adresse = models.CharField(max_length=25)
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)
    annee_scolaire = models.ManyToManyField(Annee_scolaire)
    classe = models.ForeignKey(Classe, on_delete = models.CASCADE)


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
 

"""class Personnel_ad(AbstractUser):
    matricule = models.CharField(max_length=10)
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=25)
    poste = models.ForeignKey(Poste, on_delete = models.CASCADE, related_name='users', null=True, blank=True)

    def __str__(self):
        return self.username
"""    



class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser (email=email, **extra_fields)
        user.password = make_password (password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is _staff", False)
        extra_fields.setdefault("is _superuser", False)
        return self._create_user (email, password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault ("is_staff", True)
        extra_fields.setdefault ("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields ["is_superuser"]
        return self._create_user (email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    USER_TYPE = ((1, "Personnel"), (2, "Professeur"), (3, "Parent_eleve"))
    SEXE = [("M", "Masculin"), ("F", "Feminin")]

    matricule =  models.TextField(max_length=5, editable=False, default="")
    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    telephone = models.CharField(max_length=256, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    username = None # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, null=True)
    sexe = models.CharField(max_length=1, choices=SEXE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager ()

    def save(self, *args, **kwargs) -> None:
        if not self.matricule:
            self.matricule = generer_matricule(CustomUser)  # Générer un matricule pour l'utilisateur
        super().save(*args, **kwargs) 

    def _str_(self):
       return f"{self.nom.upper()} {self.prenom.capitalize()}"
    

class Personnel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    poste = models.ForeignKey(Poste, on_delete = models.CASCADE, related_name='users', null=True, blank=True)


class Professeur(models.Model):
   user = models.OneToOneField(CustomUser, related_name='enseignant',on_delete=models.CASCADE)
   
   def __str__(self):
       return f"{self.user.nom.upper()} {self.user.prenom.capitalize()} "

class Enseignement(models.Model):
    enseignant = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    matiere = models.ForeignKey('gestion_notes.Matiere', on_delete=models.CASCADE)
    coeficient = models.IntegerField(choices=((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)))

    def __str__(self):
        return f"{self.enseignant.nom} enseigne {self.matiere.code} à la classe {self.classe.code}"


class Parent_eleve(models.Model):
   
   nom_pere = models.CharField (max_length=256)
   telephone_pere = models.CharField(max_length=256, blank=True, null=True)
   email_pere = models.EmailField(blank=True, null=True)
   nom_mere = models.CharField(max_length=256)
   telephone_mere = models.CharField(max_length=256, blank=True, null=True)
   email_mere = models.EmailField (blank=True, null=True)
   adresse = models. TextField(blank=True, null=True)

   def _str_(self):
    return f"Parents de {self.nom_pere.upper()} et {self.nom_mere.capitalize()}"

 