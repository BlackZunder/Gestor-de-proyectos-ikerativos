from django.contrib import admin
from .models import CustomUser, Tarea, Proyecto

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Tarea)
admin.site.register(Proyecto)

