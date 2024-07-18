from django.shortcuts import render
from .forms import RegisterModelForm, CustomAuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Proyecto
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    
@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})

@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    tareas = proyecto.tareas.all()
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})