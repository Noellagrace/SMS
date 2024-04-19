from random import choice

from django.db import models 


def generer_matricule(model: models.Model):
    """
    Fonction qui permet de generer un matricule.

    :param model: un model de base de donnees
    :return: un matricule
    """

    # Matricule final qui sera renvoye
    matricule_final = ""
    # Les lettres et chiffres qui sont utilises pour generer le matricule
    lettres = "qwertyuiopasdfghjklzxcvbnm0123456789"
    # On fait une boucle qui va s'executer 6 fois
    for i in range(6):
        # A chaque iteration, on choisit une lettre au hasard et on l'ajoute a matricule
        matricule_final = matricule_final + choice(lettres)
    
    matricule_existant = model.objects.filter(matricule=matricule_final.upper())
    if matricule_existant:
        return generer_matricule(model)
    
    return matricule_final.upper()