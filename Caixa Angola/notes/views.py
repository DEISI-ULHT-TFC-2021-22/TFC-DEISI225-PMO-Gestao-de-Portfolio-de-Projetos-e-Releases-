from django.shortcuts import render, redirect
from .models import MyNote
from .forms import CreateNote
from django.http import HttpResponse
from main.decorators import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def notelist(request):
    notes = MyNote.objects.filter(user=request.user).order_by('-Data')
    return render(request, 'notes/notelist.html', {'notes':notes})

@login_required
def addnote(request):
    upload = CreateNote()
    if request.method == 'POST':
        upload = CreateNote(request.POST, request.FILES)
        if upload.is_valid():
            note = upload.save(commit=False)
            note.user = request.user
            note.save()
            upload.save()
            return redirect('notelist')
        else:
            return HttpResponse("""Erro = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'notes/addnote.html', {'addnote': upload})

@login_required
def edit_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = MyNote.objects.get(id=note_id)
    except MyNote.DoesNotExist:
        return redirect('notelist')
    
    note_form = CreateNote(request.POST or None, instance=note_sel)
    if note_form.is_valid():
        note_form.save()
        return redirect('notelist')
    return render(request, 'notes/addnote.html', {'addnote': note_form})

@login_required
def delete_note(request, note_id):
    note_id = int(note_id)
    try:
        note_sel = MyNote.objects.get(id=note_id)
    except MyNote.DoesNotExist:
        return redirect('notelist')
    note_sel.delete()
    return redirect('notelist')