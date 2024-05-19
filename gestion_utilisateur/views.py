from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from SMS import settings
from gestion_utilisateur.forms import *
from gestion_utilisateur.models import *
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.


def create_anneescolaire(request):
    form = AnneScolaireForm()

    if request.method == "POST":
        form = AnneScolaireForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_anneescolaire')
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

def dashboard(request):
    return render(request, 'index.html')



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
        form = Personnel_adForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_personnelAD')
            except:
                message = "something is wromg!"
                form = Personnel_adForm()
            return render(request, 'personnel.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:
        form = Personnel_adForm()
    return render(request, 'personnel.html',{'form':form})

def show_personnelAD(request):
    personnelADS = Personnel_ad.objects.order_by('-id');
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
    form= EleveForm()
    return render(request, 'index_eleve.html', {'eleves':eleves,'form':form,})


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
    return render(request, 'detail.html', {'parents':parents})


def login_user(request):
    return render(request, 'login_form.html')


def register_user(request):
    return render(request, 'register.html')


def create_Poste(request):

    if request.method == "POST":
        form = PosteForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "created successfuly!")
                return redirect('/show_poste')
            except:
                message = "something is wromg!"
                form = PosteForm()
            return render(request, 'poste.html',{'message':message,'form':form})
        else:
            messages.success(request, "formulaire invalid")
    else:

        form = PosteForm()
    return render(request, 'poste.html',{'form':form})

def show_poste(request):
    postes = Poste.objects.order_by('-id');
    # Ajout d'un message pour informer l'utilisateur en cas d'absence de postes
    if not postes:
        messages.info(request, "Aucun poste trouvé.")
    return render(request, 'index_poste.html', {'postes':postes})




def login_view(request):
   if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       print(username,password)

       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request, user)
           messages.success(request, 'vous avez ete connecte avec succes')
           return redirect('/dashboard')
       else:
           messages.warning(request, "username ou password est incorect")
           return redirect('/account/login/')
   else:
       return render(request, 'login_form.html')


def log_out(request):
   log_out(request)
   messages.success(request, "logged out succesfully")
   return redirect('/account/login/')


def pwd_oublier(request):
    return render(request, 'pwd_forgot.html')


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "le mode a ete change avec succes")
            return redirect('/')
   
    else:
        form = ChangePasswordForm(user=request.user)
        messages.success(request, "errreuur")

        print(form)
    context ={
        'form' : form,
    } 
    return render(request, 'pwd_forgot.html', context)        


"""class Update_poste(UpdateView):
    models = Poste
    form_class= PosteForm
    template = 'update_poste.html'
"""


def modifier(request, id):
    obj = Poste.objects.get(id=id)
    print(obj)
    form = PosteForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid:
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_poste')
    return render(request, 'index_poste.html', {'form':form, 'messages':messages})    


def update_poste(request, id):
    poste = get_object_or_404(Poste, id=id)
    form = PosteForm(instance=poste)
    form_data = model_to_dict(form.instance)
    return JsonResponse(form_data)


def modifierpersonnel(request, id):
    obj = Personnel_ad.objects.get(id=id)
    print(obj)
    form = Personnel_adForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid():  # Ajoutez les parenthèses ici
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_personnelAD')
    return render(request, 'index_personnel.html', {'form':form, 'messages':messages})  


def update_personnel(request, id):
    personnel_ad = get_object_or_404(Personnel_ad, id=id)
    form = Personnel_adForm(instance=personnel_ad)
    form_data = model_to_dict(form.instance)
    return JsonResponse(form_data)


def modifierclasse(request, id):
    obj = Classe.objects.get(id=id)
    print(obj)
    form = ClasseForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid:
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_classe')
    return render(request, 'index_classe.html', {'form':form, 'messages':messages})    


def update_classe(request, id):
    classe = get_object_or_404(Classe, id=id)
    form = ClasseForm(instance=classe)
    form_data = model_to_dict(form.instance)
    return JsonResponse(form_data)


def modifierannee(request, id):
    obj = Annee_scolaire.objects.get(id=id)
    print(obj)
    form = AnneScolaireForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid:
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_anneescolaire')
    return render(request, 'index_annee.html', {'form':form, 'messages':messages})    


def update_annee(request, id):
    annee = get_object_or_404(Annee_scolaire, id=id)
    form = AnneScolaireForm(instance=annee)
    form_data = model_to_dict(form.instance)
    return JsonResponse(form_data)


def modifierenseignant(request, id):
    obj = Enseignant.objects.get(id=id)
    print(obj)
    form = EnseignantForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid:
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_enseignant')
    return render(request, 'index_enseignant.html', {'form':form, 'messages':messages})    


def update_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    form = EnseignantForm(instance=enseignant)
    form_data = model_to_dict(form.instance)
    return JsonResponse(form_data)


def modifiereleve(request, id):
    obj = Eleve.objects.get(id=id)
    print(obj)
    form = EleveForm(request.POST or None, instance=obj)
    print(form)
    messages = ''
    if form.is_valid:
        form.save()
        messages = "Modifications effectuees avec succes!"
        return redirect('/show_eleve')
    return render(request, 'index_eleve.html', {'form':form, 'messages':messages})    


def update_eleve(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    form = EleveForm(instance=eleve)
    form_data = model_to_dict(form.instance)
    
    # Convertir les objets Annee_scolaire en une liste d'ids
    form_data['annee_scolaire'] = list(eleve.annee_scolaire.values_list('id', flat=True))
    
    return JsonResponse(form_data)

def delete_annee(request,id):
    annee = get_object_or_404(Annee_scolaire, id=id)
    annee.delete()
    messages.success(request, 'annee supprimer avec succes')
    return redirect('/show_anneescolaire')


def delete_classe(request,id):
    classe = get_object_or_404(Classe, id=id)
    classe.delete()
    messages.success(request, 'classe supprimer avec succes')
    return redirect('/show_classe')


def delete_enseignant(request,id):
    enseignant = get_object_or_404(Enseignant, id=id)
    enseignant.delete()
    messages.success(request, 'enseignant supprimer avec succes')
    return redirect('/show_enseignant')


def delete_eleve(request,id):
    eleve = get_object_or_404(Eleve, id=id)
    eleve.delete()
    messages.success(request, 'eleve supprimer avec succes')
    return redirect('/show_eleve')


def search_enseignant(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        enseignants = Enseignant.objects.filter(nom__icontains=query)
    
    #conversion des resultats de la requette en un dictionnaire de reponse en json
        results = []
        for enseignant in enseignants:
            results.append({
                'matricule': Enseignant.matricule,
                'nom': Enseignant.nom,
                'prenom': Enseignant.prenom,
                'email': Enseignant.email,
                'telephone': Enseignant.telephone,
                'adresse': Enseignant.adresse,
            })
            print(enseignant)
        return render(request, 'index_enseignant.html', {'enseignants': enseignants})    
    
    return JsonResponse({'results': []})


def search_annee(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        annees = Annee_scolaire.objects.filter(anneescolaire__icontains=query)
    
    #conversion des resultats de la requette en un dictionnaire de reponse en json
        results = []
        for annee in annees:
            results.append({
                'date_debut': Annee_scolaire.date_debut,
                'date_fin': Annee_scolaire.date_fin,
                'anneescolaire': Annee_scolaire.anneescolaire,
            })
            print(annee)
        return render(request, 'index_annee.html', {'annnes': annees})    
    
    return JsonResponse({'results': []})


def search_eleve(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        eleves = Eleve.objects.filter(nom__icontains=query)
    
    #conversion des resultats de la requette en un dictionnaire de reponse en json
        results = []
        for eleve in eleves:
            results.append({
                'matricule': Eleve.matricule,
                'nom': Eleve.nom,
                'prenom': Eleve.prenom,
                'date_naiss': Eleve.date_naiss,
                'adresse': Eleve.adresse,
                'classe': Eleve.classe,
                'annee_scolaire': Eleve.annee_scolaire,
            })
            print(eleve)
        return render(request, 'index_eleve.html', {'eleves': eleves})    
    
    return JsonResponse({'results': []})


def detail(request, id):
    eleve = get_object_or_404(Eleve, id=id)
    form= ParentForm()
    # parent = get_object_or_404(Parent, id=id)
    return render(request, 'detail.html', {'eleve': eleve,'form':form})

