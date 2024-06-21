#from . import views
from gestion_utilisateur import views
from django.urls import path
from .views import *
urlpatterns = [
    path('show_matiere', views.show_matiere),
    path('create_notes', views.create_notes),
    path('show_notes', views.show_notes),
    path('add_notes', views.add_notes),
    path('filtrer/', views.filtrer_eleves, name='nom_de_la_vue_pour_filtrer'),
    path('affecter/<int:id>', views.affecter),
    path('add_notes_view/', add_notes_view, name='add_notes_view'),
    path('filter_notes/', filter_notes, name='filter_notes'),

]