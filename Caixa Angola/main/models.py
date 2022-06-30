from cProfile import label
from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	img1 = models.ImageField(upload_to='img', blank=True, null=True)
	img2 = models.ImageField(upload_to='img', blank=True, null=True)
	img3 = models.ImageField(upload_to='img', blank=True, null=True)
	img4 = models.ImageField(upload_to='img', blank=True, null=True)
	img5 = models.ImageField(upload_to='img', blank=True, null=True)
	img6 = models.ImageField(upload_to='img', blank=True, null=True)
	img7 = models.ImageField(upload_to='img', blank=True, null=True)
	img8 = models.ImageField(upload_to='img', blank=True, null=True)
	type = models.CharField('Tipo do evento', max_length=120)
	name = models.CharField('Nome do evento', max_length=120)
	# event_date = models.DateTimeField('Event Date')
	description = models.TextField(blank=True)
	# gallery = models.CharField('Nome do evento', max_length=120, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Document(models.Model):
	documents = models.FileField(upload_to='documents', blank=True, null=True)
	name = models.CharField('Nome do evento', max_length=120)
	# event_date = models.DateTimeField('Event Date')
	# gallery = models.CharField('Nome do evento', max_length=120, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Oportunidade(models.Model):
	state_choices = (
		("Em espera","Em espera"),
		("Em progresso", "Em progresso"),
		("Finalizado", "Finalizado")
	)
	is_approved_choices = (
		("Sim","Sim"),
		("Não", "Não"),
	)
	recursos_choices = (
		("Sim","Sim"),
		("Não", "Não"),
	)

	nome = models.CharField('Nome', max_length=120)
	id_number = models.IntegerField('ID')
	departamento = models.CharField('Departamento', max_length=120)
	email = models.EmailField(max_length=120)
	desc = models.TextField('Descrição da oportunidade', max_length=240)
	recursos = models.CharField(choices=recursos_choices, max_length=120)
	date = models.DateTimeField(auto_now_add=True)
	state = models.CharField(choices=state_choices, max_length=120, default='Em espera')
	is_approved = models.CharField(choices=is_approved_choices, max_length=120)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.nome