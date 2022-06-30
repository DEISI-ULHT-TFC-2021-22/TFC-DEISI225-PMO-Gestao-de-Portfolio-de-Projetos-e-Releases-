from django import forms
from .models import MyNote

class CreateNote(forms.ModelForm):
    class Meta:
        model = MyNote
        fields = ('Título', 'Descrição',)
        widgets = {
			'Título': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
			'Descrição': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição'})
        }
    