from django.contrib import admin
from .models import CustomUser, Tareas, Proyectos

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Tareas)
admin.site.register(Proyectos)

