from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import password_validation 
from .models import CustomUser

class RegisterModelForm(UserCreationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'autocomplete': 'new-password'}),
    )
    class Meta:
        model = CustomUser 
        fields = ("username", "password1", "password2")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
)
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña'}),
    )