from django.shortcuts import render
from .forms import RegisterModelForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

# Create your views here.

#Permite registrar usuarios
def register(request):
    if request.method == 'POST':
        form = RegisterModelForm(request.POST)  
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterModelForm() 
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'