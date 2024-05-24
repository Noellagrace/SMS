#from . import views
from gestion_utilisateur import views
from django.urls import path

urlpatterns = [
    path('show_matiere', views.show_matiere),

]