"""
URL configuration for Proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from GESTOR_PROYECTOS.views import CustomLoginView,lista_proyectos, detalle_proyecto, tareas_trabajador, update_task_status,crear_proyecto,crear_tarea

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'), 
    path("admin/", admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    path('proyectos/<int:proyecto_id>/', detalle_proyecto, name='detalle_proyecto'),
    path('tareas_trabajador/', tareas_trabajador, name='tareas_trabajador'),  # Nueva ruta
    path('tareas/update_status/<int:tarea_id>/', update_task_status, name='update_task_status'),  # Ruta para actualizar el estado de la tarea
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('crear_proyecto/', crear_proyecto, name='crear_proyecto'), # Nueva ruta para crear un proyecto
    path('crear_tarea/<int:proyecto_id>/', crear_tarea, name='crear_tarea')  # Ajuste para aceptar proyecto_id
]
