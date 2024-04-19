from gestion_utilisateur import views
from django.urls import path

urlpatterns = [
    path('create_anneescolaire', views.create_anneescolaire),
    path('show_anneescolaire', views.show_anneescolaire),
    path('create_classe', views.create_classe),
    path('show_classe', views.show_classe),
    path('create_personnelAD', views.create_personnelAD),
    path('show_personnelAD', views.show_personnelAD),
    path('create_Enseignant', views.create_Enseignant),
    path('show_enseignant', views.show_enseignant),
    path('create_Eleve', views.create_Eleve),
    path('show_eleve', views.show_eleve),
    
] 