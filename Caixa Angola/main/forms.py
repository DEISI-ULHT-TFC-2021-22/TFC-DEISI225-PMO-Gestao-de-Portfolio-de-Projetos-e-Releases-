from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect
from .models import Event, Document, Oportunidade
from django.forms import ModelForm

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, label = 'Primeiro nome', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, label = 'Último nome', required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    # departamento = forms.ChoiceField (choices = CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = (
			'img1', 'img2', 'img3', 'img4', 'img5', 'img6', 'img7', 'img8', 'type', 'name', 'description'
			)# , 'gallery')
		labels = {	
			'type': '',
            'name': '',
			# 'event_date': 'YYYY-MM-DD HH:MM:SS',
			'description': '',
			'gallery': '',
		}
		widgets = {
			'type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo do evento'}),
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do evento'}),
			# 'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição'}),
			'gallery': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Galeria do evento'}),
		}

class DocumentForm(ModelForm):
	class Meta:
		model = Document
		fields = ('documents', 'name')
		labels = {	
            'name': '',
			# 'file_date': 'YYYY-MM-DD HH:MM:SS',
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do ficheiro'}),
			# 'file_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
		}

class OportunidadeForm(ModelForm):
	class Meta:
		model = Oportunidade
		fields = ('nome', 'id_number', 'departamento', 'email', 'desc', 'recursos')
		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}),
			'id_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID'}),
			'departamento': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Departamento'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'desc': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição'}),
		}

class IsApprovedForm(ModelForm):
	is_approved_choices = (
		('', '----'),
		("Sim","Sim"),
		("Não", "Não"),
	)
	
	is_approved = forms.ChoiceField(choices=is_approved_choices, required=False, label='Aprovado')

	class Meta:
		model = Oportunidade
		fields = ('is_approved',)
		widgets = {
				'is_approved': forms.Select(attrs={'class': 'custom-select md-form'}),
			}

class StateForm(ModelForm):
	state_choices = (
		("Em espera","Em espera"),
		("Em progresso", "Em progresso"),
		("Finalizado", "Finalizado")
	)
	
	state = forms.ChoiceField(choices=state_choices, required=False, label='Estado')

	class Meta:
		model = Oportunidade
		fields = ('state',)
		widgets = {
				'state': forms.Select(attrs={'class': 'custom-select md-form'}),
			}