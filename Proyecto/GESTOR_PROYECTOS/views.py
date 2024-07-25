from django.shortcuts import render
from .forms import CustomAuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from .forms import ProyectoForm,TareaForm

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Proyecto, Tarea
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

# Create your views here.

# Permite registrar usuarios

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'

@login_required
def lista_proyectos(request):
    query = request.GET.get("q")  # Paso 1: Captura el término de búsqueda
    proyectos = Proyecto.objects.all()
    if query:
        proyectos = proyectos.filter(nombre__icontains=query)  # Paso 2: Filtra los proyectos
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})  # Paso 3: Pasa los proyectos filtrados

@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    tareas = proyecto.tareas.all()
    query = request.GET.get("q")  # Captura el término de búsqueda
    if query:
        tareas = tareas.filter(nombre__icontains=query)  # Filtra las tareas
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto, 'tareas': tareas})  # Pasa las tareas filtradas

@login_required
def tareas_trabajador(request):
    usuario = request.user
    grupo_trabajador = Group.objects.get(name='Trabajador')
    
    if grupo_trabajador in usuario.groups.all():
        tareas = Tarea.objects.filter(personas=usuario)
    else:
        tareas = Tarea.objects.none()

    return render(request, 'tareas_trabajador.html', {'tareas': tareas})

@login_required
@require_POST
def update_task_status(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    nuevo_estado = request.POST.get('estado')
    if nuevo_estado in [choice[0] for choice in Tarea.ESTADO_CHOICES]:  # Asegúrate de que el nuevo estado sea uno de los estados válidos
        tarea.estado = nuevo_estado
        tarea.save()
    return redirect('tareas_trabajador')

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')  # Redirige a la lista de proyectos después de crear uno nuevo
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})


@login_required
def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.proyecto = proyecto
            tarea.save()
            form.save_m2m()  # Para guardar las relaciones ManyToMany
            return redirect('detalle_proyecto', proyecto_id=proyecto.id)
    else:
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form, 'proyecto': proyecto})