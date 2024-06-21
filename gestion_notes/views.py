from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from gestion_notes.models import Note

from gestion_utilisateur.models import *
from .forms import NoteForm

@login_required
def add_notes_view(request):
    user = request.user
    professeur = get_object_or_404(Professeur, user=user)
    
    enseignements = Enseignement.objects.filter(enseignant=professeur)
    
    if hasattr(user, 'enseignant'):
        enseignant = user.enseignant
        enseignements = Enseignement.objects.filter(enseignant=enseignant)
        classes = [enseignement.classe for enseignement in enseignements]
        print(classes)

    if request.method == 'POST':
        classe_id = request.POST.get('classe_id')
        matiere_id = request.POST.get('matiere_id')
        sequence = request.POST.get('sequence')
        evaluation = request.POST.get('evaluation')
        date = request.POST.get('date')
        
        notes_data = request.POST.getlist('note')
        eleves_ids = request.POST.getlist('eleve_id')
        print(classe_id)
        print(matiere_id)
        print(sequence)
        print(evaluation)
        print(date)
        print(notes_data)
        print(eleves_ids) 
        
        for note_value, eleve_id in zip(notes_data, eleves_ids):
            eleve = get_object_or_404(Eleve, id=eleve_id)
            matiere = get_object_or_404(Matiere, id=matiere_id)
            Note.objects.create(
                eleve=eleve,
                note=note_value,
                sequence=sequence,
                evaluation=evaluation,
                classe=eleve.classe,
                enseignant=professeur,
                matiere=matiere,
                date=date
            )
            
           
        
        return redirect('/notes/add_notes_view/')  # Rediriger vers une page de succès après l'enregistrement des notes
    
    context = {
        'enseignements': enseignements,
        'classes': classes,  # Vous pouvez filtrer selon vos besoins
    }
    return render(request, 'ajouter_note.html', context)



@login_required
def filter_notes(request):
    user = request.user
  
    notes = []
    
    if hasattr(user, 'enseignant'):
        enseignant = user.enseignant
        enseignements = Enseignement.objects.filter(enseignant=enseignant)
        classes = [enseignement.classe for enseignement in enseignements]
        print(classes)

    if request.method == 'POST':
        classe_id = request.POST.get('classe_id')
        matiere_id = request.POST.get('matiere_id')
        sequence = request.POST.get('sequence')
        evaluation = request.POST.get('evaluation')

        if classe_id and sequence and evaluation:
            notes = Note.objects.filter(
                classe_id=classe_id,
                matiere_id=matiere_id,
                sequence=sequence,
                evaluation=evaluation
            )

    return render(request, 'index_notes.html', {
       'classes': classes,
        'notes': notes
    })
