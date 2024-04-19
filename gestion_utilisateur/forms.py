from django import forms
from .models import *


class AnneScolaireForm(forms.ModelForm):
    class Meta:
        model = Annee_scolaire
        fields = ['date_debut', 'date_fin', 'anneescolaire']
        widgets = {
            'date_debut': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'anneescolaire': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = '__all__'
        widgets = {
            'code' : forms.TextInput(attrs={'class': 'form-control'}),
            'libelle' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class PersonnelADForm(forms.ModelForm):
    class Meta:
        model = PersonnelAD
        fields = ['matricule', 'nom', 'prenom', 'email', 'telephone', 'adresse']
        widgets = {
            'matricule' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['matricule', 'nom', 'prenom', 'email', 'telephone', 'adresse']
        widgets = {
            'matricule' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control'}),
        }


class EleveForm(forms.ModelForm):
    class Meta:
        model = Eleve
        fields = '__all__'
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'date_naiss': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'classe': forms.Select(attrs={'class': 'form-control'}),
            'annee_scolaire': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse']
        widgets = {
            'nom' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control'}),
        }
