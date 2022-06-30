from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, IsApprovedForm
from .decorators import *
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, Http404, HttpResponse, HttpResponseRedirect
import os
from .forms import *
from .models import Event, Document, Oportunidade
from django.views.generic import DetailView
from braces.views import GroupRequiredMixin
 
def show_pdf(request):
    filepath = os.path.join('static', 'sample.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# propostas/oportunidades
def novasoportunidades(request):
	submitted = False
	if request.method == "POST":
		form = OportunidadeForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			submission.user = request.user
			submission.save()
			form.save()
			messages.success(request, ("A sua oportunidade foi submetida com sucesso."))
			return 	HttpResponseRedirect('/?submitted=True')
	else:
		form = OportunidadeForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'novasOportunidades.html', {'form':form, 'submitted':submitted})

def submission_status_search(request):
	if request.method == 'POST':
		searched = request.POST['searched']
		submissions = Oportunidade.objects.filter(user=request.user, nome__contains=searched).order_by('-date') or Oportunidade.objects.filter(user=request.user, id_number__contains=searched).order_by('-date')
		return render(request, 'submissionstatus-search.html', {'searched':searched, 
		'submissions': submissions})
	else:
		return render(request, 'submissionstatus-search.html', {})

@groupcheck('Gestor de Portfólios', 'superuser')
def status_search(request):
	if request.method == 'POST':
		searchedss = request.POST['searchedss']
		submissions = Oportunidade.objects.filter(nome__contains=searchedss).order_by('-date') or Oportunidade.objects.filter(id_number__contains=searchedss).order_by('-date')
		return render(request, 'status-search.html', {'searchedss':searchedss, 
		'submissions': submissions})
	else:
		return render(request, 'status-search.html', {})
		
@groupcheck('Gestor de Portfólios', 'superuser')
def propostas_search(request):
	if request.method == 'POST':
		searcheds = request.POST['searcheds']
		submissions = Oportunidade.objects.filter(nome__contains=searcheds).order_by('-date') or Oportunidade.objects.filter(id_number__contains=searcheds).order_by('-date')
		return render(request, 'propostas-search.html', {'searcheds':searcheds, 
		'submissions': submissions})
	else:
		return render(request, 'propostas-search.html', {})

@groupcheck('Gestor de Portfólios', 'superuser')
def propostas(request):
	oportunidade_list = Oportunidade.objects.all().order_by('-date')
	return render(request, 'propostas.html', {
		'oportunidade_list': oportunidade_list
	})

@groupcheck('Gestor de Portfólios', 'superuser')
def status_oportunidade(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	form = StateForm(request.POST or None, instance=oportunidade)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = StateForm(request.POST, instance=oportunidade)
	if form.is_valid():
		form.save()
		return redirect('Status')

	return render(request, 'proposta-status.html', 
		{'oportunidade': oportunidade,
		'form':form})

@groupcheck('Gestor de Portfólios', 'superuser')
def status(request):
	oportunidade_list = Oportunidade.objects.filter(is_approved='Sim').order_by('-date')
	return render(request, 'status.html', {
		'oportunidade_list': oportunidade_list
		})

def submissionstatus(request):
	oportunidade_list = Oportunidade.objects.filter(user=request.user).order_by('-date')
	return render(request, 'submissionStatus.html', {
		'oportunidade_list': oportunidade_list
		})

@groupcheck('Gestor de Portfólios', 'superuser')
def status_oportunidade(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	form = StateForm(request.POST or None, instance=oportunidade)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = StateForm(request.POST, instance=oportunidade)
	if form.is_valid():
		form.save()
		return redirect('Status')

	return render(request, 'proposta-status.html', 
		{'oportunidade': oportunidade,
		'form':form})

@groupcheck('Gestor de Portfólios', 'superuser')
def approve_oportunidade(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	oportunidade.is_approved = 'Sim'
	oportunidade.save()
	return redirect('Propostas')

@groupcheck('Gestor de Portfólios', 'superuser')
def edit_oportunidade(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	form = OportunidadeForm(request.POST or None, instance=oportunidade)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = OportunidadeForm(request.POST, instance=oportunidade)
	if form.is_valid():
		form.save()
		return redirect('Propostas')

	return render(request, 'edit-proposta.html', 
		{'oportunidade': oportunidade,
		'form':form})

@groupcheck('Gestor de Portfólios', 'superuser')
def delete_oportunidade(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	oportunidade.delete()
	return redirect('indexPMO')

@groupcheck('Gestor de Portfólios', 'superuser')
def oportunidade_details(request, oportunidade_id):
	oportunidade = Oportunidade.objects.get(pk=oportunidade_id)
	return render(request, 'oportunidade_details.html', 
		{'oportunidade': oportunidade})

# documents
@groupcheck('Gestor de Portfólios', 'superuser')
def edit_document(request, document_id):
	document = Document.objects.get(pk=document_id)
	form = DocumentForm(request.POST or None, instance=document)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = DocumentForm(request.POST, request.FILES, instance=document)
	if form.is_valid():
		form.save()
		return redirect('documentlist')

	return render(request, 'edit_document.html', 
		{'document': document,
		'form':form})

@groupcheck('Gestor de Portfólios', 'superuser')
def delete_document(request, document_id):
	document = Document.objects.get(pk=document_id)
	document.delete()
	return redirect('documentlist')

# def manual(request):
	return render(request, 'manual.html', {})

# baixar manual
# def manual(request):
	with open('static/MDU.pdf', 'r') as pdf:
		response = HttpResponse(pdf.read(),content_type='static/MDU.pdf')
		response['Content-Disposition'] = 'filename=MDU.pdf'
		return response

@groupcheck('Gestor de Portfólios', 'superuser')
def indexpmo(request):
	return render(request, 'indexPMO.html')

@groupcheck('Gestor de Projetos', 'superuser')
def indexgestor(request):
	return render(request, 'indexGestor.html')

# documents
@groupcheck('Gestor de Portfólios', 'superuser')
def documentlist(request):
	document_list = Document.objects.all().order_by('-date')
	return render(request, 'documentos.html', {
		'document_list': document_list
	})

@groupcheck('Gestor de Projetos', 'Gestor de Portfólios', 'superuser')
def adddocument(request):
	submitted = False
	if request.method == "POST":
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return 	HttpResponseRedirect('/indexGestor?submitted=True')
	else:
		form = DocumentForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'sendFiles.html', {'form':form, 'submitted':submitted})

@groupcheck('Gestor de Projetos', 'superuser')
def edit_document(request, document_id):
	document = Document.objects.get(pk=document_id)
	form = DocumentForm(request.POST or None, instance=document)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = DocumentForm(request.POST, request.FILES, instance=document)
	if form.is_valid():
		form.save()
		return redirect('documentlist')

	return render(request, 'edit_document.html', 
		{'document': document,
		'form':form})

@groupcheck('Gestor de Projetos', 'superuser')
def delete_document(request, document_id):
	document = Document.objects.get(pk=document_id)
	document.delete()
	return redirect('documentlist')


# eventos caixa social
def caixasocial(request):
	event_list = Event.objects.all().order_by('-date')
	return render(request, 'caixaSocial.html', {
		'event_list': event_list
	})

@groupcheck('Gestor de Portfólios', 'superuser')
def eventlist(request):
	event_list = Event.objects.all().order_by('-date')
	return render(request, 'event-list.html', {
		'event_list': event_list
	})

@groupcheck('Gestor de Portfólios', 'superuser')
def addevent(request):
	submitted = False
	if request.method == "POST":
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return 	HttpResponseRedirect('/EventList?submitted=True')
	else:
		form = EventForm
		if 'submitted' in request.GET:
			submitted = True
	return render(request, 'add-event.html', {'form':form, 'submitted':submitted})

@groupcheck('Gestor de Portfólios', 'superuser')
def edit_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	form = EventForm(request.POST or None, instance=event)
	if form.is_valid():
		form.save()
	if request.method == "POST":
		form = EventForm(request.POST, request.FILES, instance=event)
	if form.is_valid():
		form.save()
		return redirect('eventlist')

	return render(request, 'edit_event.html', 
		{'event': event,
		'form':form})

@groupcheck('Gestor de Portfólios', 'superuser')
def delete_event(request, event_id):
	event = Event.objects.get(pk=event_id)
	event.delete()
	return redirect('eventlist')

# authentication
@user_passes_test(lambda user: not user.username, login_url='/', redirect_field_name=None)
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.success(request, ("Houve um erro ao logar em sua conta, tente novamente."))	
			return redirect('login')	
	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ("Utilizador desconectado com sucesso."))
	return redirect('/')

@user_passes_test(lambda user: not user.username, login_url='/', redirect_field_name=None)
def register_user(request):
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username= form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registro efetuado com sucesso, aguarde até o administrador autorizar a sua conta."))
			return redirect('/')
	else:
		form = RegisterUserForm()
	return render(request, 'register_user.html', {
		'form':form,
	})
