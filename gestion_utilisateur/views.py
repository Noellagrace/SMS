from django.shortcuts import redirect, render
from django.contrib import messages
from gestion_utilisateur.forms import AnneScolaireForm, ClasseForm, EleveForm, EnseignantForm, ParentForm, PersonnelADForm
from gestion_utilisateur.models import Annee_scolaire, Classe, Eleve, Enseignant, Parent, PersonnelAD

# Create your views here.

def create_anneescolaire(request):
    form = AnneScolaireForm()

    if request.method == "POST":
        form = AnneScolaireForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/')
            except:
                message = "something is wromg!"
                form = AnneScolaireForm()
            return render(request, 'anneescolaire.html',{'message':message,'form':form})
    else:
        form = AnneScolaireForm()
    return render(request, 'anneescolaire.html',{'form':form})
        
def show_anneescolaire(request):
    anneescolaires = Annee_scolaire.objects.order_by('-id');
    return render(request, 'index_annee.html', {'anneescolaires':anneescolaires})



def create_classe(request):
    form = ClasseForm()

    if request.method == "POST":
        form = ClasseForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_classe')
            except:
                message = "something is wromg!"
                form = ClasseForm()
            return render(request, 'classe.html',{'message':message,'form':form})
    else:
        form = ClasseForm()
    return render(request, 'classe.html',{'form':form})

def show_classe(request):
    classes = Classe.objects.order_by('-id');
    return render(request, 'index_classe.html', {'classes':classes})



def create_personnelAD(request):

    if request.method == "POST":
        form = PersonnelADForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_personnelAD')
            except:
                message = "something is wromg!"
                form = PersonnelADForm()
            return render(request, 'personnel.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:
        form = PersonnelADForm()
    return render(request, 'personnel.html',{'form':form})

def show_personnelAD(request):
    personnelADS = PersonnelAD.objects.order_by('-id');
    return render(request, 'index_personnel.html', {'personnelADS':personnelADS})



def create_Enseignant(request):

    if request.method == "POST":
        form = EnseignantForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_enseignant')
            except:
                message = "something is wromg!"
                form = EnseignantForm()
            return render(request, 'enseignant.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:
        form = EnseignantForm()
    return render(request, 'enseignant.html',{'form':form})

def show_enseignant(request):
    enseignants = Enseignant.objects.order_by('-id');
    return render(request, 'index_enseignant.html', {'enseignants':enseignants})



def create_Eleve(request):

    if request.method == "POST":
        form = EleveForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_eleve')
            except:
                message = "something is wromg!"
                form = EleveForm()
            return render(request, 'eleve.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:
        form = EleveForm()
    return render(request, 'eleve.html',{'form':form})

def show_eleve(request):
    eleves = Eleve.objects.order_by('-id');
    return render(request, 'index_eleve.html', {'eleves':eleves})


def create_parent(request):

    if request.method == "POST":
        form = ParentForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_parent')
            except:
                message = "something is wromg!"
                form = ParentForm()
            return render(request, 'parent.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:
        form = ParentForm()
    return render(request, 'parent.html',{'form':form})

def show_parent(request):
    parents = Parent.objects.order_by('-id');
    return render(request, 'index_parent.html', {'parents':parents})