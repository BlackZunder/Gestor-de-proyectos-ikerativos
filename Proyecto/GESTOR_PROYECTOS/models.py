from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('no_iniciado', 'No Iniciado'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ]
    PRIORIDAD_CHOICES=[
        ('baja','Baja'),
        ('media','Media'),
        ('alta','Alta'),
    ]
    nombre=models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='no_iniciado')
    prioridad=models.CharField(max_length=50,choices=PRIORIDAD_CHOICES)
    descripcion=models.TextField()
    fecha=models.DateField(auto_now_add=True)
    fecha_final = models.DateField()  
    personas = models.ManyToManyField(User)
    proyecto = models.ForeignKey('Proyecto', related_name='tareas', on_delete=models.CASCADE)  



class Proyecto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    finalizado=models.BooleanField(default=False)
    personas = models.ManyToManyField(User)
    def __str__(self):
        return self.nombre
