from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from stock.models import Destino,Materias,Categoria
from stock import models




class MateriasForm(forms.ModelForm):
    name = forms.CharField(label='Nome')
    description = forms.CharField(label='Descrição')
    
    class Meta:
        model = models.Materias
        fields = (
            'name','description','marca','modelo','preco','fornecedor',
            'garantia','quantidade','categoria',
        )

