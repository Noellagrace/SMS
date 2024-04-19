from django.contrib import admin

from gestion_utilisateur.models import Annee_scolaire, Classe, Eleve, Enseignant, Parent, PersonnelAD

# Register your models here.
admin.site.register(Annee_scolaire)
admin.site.register(Classe)
admin.site.register(PersonnelAD)
admin.site.register(Enseignant)
admin.site.register(Eleve)
admin.site.register(Parent)