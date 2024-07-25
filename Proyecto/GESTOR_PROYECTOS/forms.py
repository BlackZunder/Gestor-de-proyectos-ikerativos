from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import password_validation 
from .models import Proyecto, Tarea


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
)
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
    )
    
class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'personas']
        
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'estado', 'prioridad', 'descripcion', 'fecha_final', 'personas']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la tarea'}),
            'estado': forms.Select(),
            'prioridad': forms.Select(),
            'descripcion': forms.Textarea(attrs={'placeholder': 'Descripción de la tarea'}),
            'fecha_final': forms.DateInput(attrs={'type': 'date'}),
            'personas': forms.SelectMultiple(),
        }