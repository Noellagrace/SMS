from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from gestion_utilisateur.forms import *


class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = '__all__'
        widgets = {
            'code' : forms.TextInput(attrs={'class': 'form-control'}),
            'libelle' : forms.TextInput(attrs={'class': 'form-control'}),
        } 


class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['nom']  # Inclure uniquement les champs que l'utilisateur doit pouvoir modifier
        widgets = {
            'nom': forms.Select(attrs={'class': 'form-control'}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'eleve' : forms.Select(attrs={'class': 'form-control'}),
            'note' : forms.NumberInput(attrs={'class': 'form-control'}),
            'note_coeficiee' : forms.NumberInput(attrs={'class': 'form-control'}),
            'classe' : forms.TextInput(attrs={'class': 'form-control'}),
            'sequence' : forms.TextInput(attrs={'class': 'form-control'}),
            'matiere' : forms.Select(attrs={'class': 'form-control'}),
            'evaluation' : forms.Select(attrs={'class': 'form-control'}),
            'enseignant' : forms.Select(attrs={'class': 'form-control'}),
            'date' : forms.DateInput(attrs={'class': 'form-control'}),
        }                               