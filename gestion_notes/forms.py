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
            'classe' : forms.Select(attrs={'class': 'form-control'}),
            'code' : forms.TextInput(attrs={'class': 'form-control'}),
            'libelle' : forms.TextInput(attrs={'class': 'form-control'}),
            'coeficient' : forms.Select(attrs={'class': 'form-control'}),
        } 


class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['nom']  # Inclure uniquement les champs que l'utilisateur doit pouvoir modifier
        widgets = {
            'nom': forms.Select(attrs={'class': 'form-control'}),
        }


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'
        widgets = {
            'type' : forms.Select(attrs={'class': 'form-control'}),
            'date_debut' : forms.TextInput(attrs={'class': 'form-control'}),
            'date_fin' : forms.TextInput(attrs={'class': 'form-control'}),
            'matiere' : forms.Select(attrs={'class': 'form-control'}),
        } 


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'notes' : forms.Select(attrs={'class': 'form-control'}),
            'eleve' : forms.TextInput(attrs={'class': 'form-control'}),
            'matiere' : forms.TextInput(attrs={'class': 'form-control'}),
            'evaluation' : forms.TextInput(attrs={'class': 'form-control'}),
        }                               