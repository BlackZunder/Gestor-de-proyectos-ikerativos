from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    ROLES = [
        ('jefe', 'Jefe'),
        ('empleado', 'Empleado'),
    ]
    rol = models.CharField(max_length=50, choices=ROLES, default='empleado')
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

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
    personas=models.ManyToManyField(CustomUser)
    proyecto = models.ForeignKey('Proyecto', related_name='tareas', on_delete=models.CASCADE)  



class Proyecto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    finalizado=models.BooleanField(default=False)
    personas=models.ManyToManyField(CustomUser)
    
