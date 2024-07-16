from django.db import models

# Create your models here.

class Personas(models.Model):
    nombre=models.CharField(max_length=50)
    rol=models.CharField(max_length=50)
    
class Tareas(models.Model):
    ESTADO_CHOICES = [
        ('no_iniciado', 'No Iniciado'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ]
    nombre=models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='no_iniciado')    
    descripcion=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    personas=models.ForeignKey(Personas, on_delete=models.CASCADE)
    
class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    finalizado=models.BooleanField(default=False)
    personas=models.ForeignKey(Personas, on_delete=models.CASCADE)
    tareas=models.ForeignKey(Tareas, on_delete=models.CASCADE)
    

    
    