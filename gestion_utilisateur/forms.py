from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User


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
            'montant' : forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = '__all__'
        widgets = {
            'nom_pere' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_pere' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_mere' : forms.TextInput(attrs={'class': 'form-control'}),
            'prenom_mere' : forms.TextInput(attrs={'class': 'form-control'}),
            'email_pere' : forms.TextInput(attrs={'class': 'form-control'}),
            'email_mere' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_pere' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone_mere' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control'}),
            'eleve': forms.Select(attrs={'class': 'form-control'}),
        }


class PosteForm(forms.ModelForm):
    class Meta:
        model = Poste
        fields = '__all__'
        widgets = {
            'code' : forms.TextInput(attrs={'class': 'form-control'}),
            'libelle' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class Personnel_adForm(forms.ModelForm):

    username = forms.CharField(
        max_length=150,  # Assuming the max_length for username is 150
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Personnel_ad
        exclude = ['is_staff','date_joined','is_active','groups','user_permissions','is_superuser','last_login']
        fields = '__all__'
        widgets = {
            'password' : forms.TextInput(attrs={'class': 'form-control'}),
            'matricule' : forms.TextInput(attrs={'class': 'form-control'}),
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            'telephone' : forms.TextInput(attrs={'class': 'form-control'}),
            'adresse' : forms.TextInput(attrs={'class': 'form-control'}),
            'poste' : forms.Select(attrs={'class': 'form-control'}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="ancien mot de pass:", max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="nouveau mot de pass:", max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                     help_text="<samall><ul class='form-text text text-muted'><li>your password can\'t be to")
    new_password2 = forms.CharField(label="confirmation de mot de pass:", max_length=32, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User 