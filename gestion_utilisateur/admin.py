from django.contrib import admin

from gestion_utilisateur.models import Annee_scolaire, Classe, Eleve, Enseignant, Parent, Personnel_ad, Poste

# Register your models here.
admin.site.register(Annee_scolaire)
admin.site.register(Classe)
admin.site.register(Personnel_ad)
admin.site.register(Enseignant)
admin.site.register(Eleve)
admin.site.register(Parent)
admin.site.register(Poste)