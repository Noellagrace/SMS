from django.contrib import admin


from gestion_utilisateur.models import Annee_scolaire, Classe, CustomUser, Eleve, Enseignement, Parent, Personnel, Poste, Professeur

# Register your models here.
admin.site.register(Annee_scolaire)
admin.site.register(Classe)
admin.site.register(Personnel)
admin.site.register(Professeur)
admin.site.register(Eleve)
admin.site.register(Parent)
admin.site.register(Poste)
#admin.site.register(Enseignement)
admin.site.register(CustomUser)
