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

class Tareas(models.Model):
    ESTADO_CHOICES = [
        ('no_iniciado', 'No Iniciado'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado'),
    ]
    
    nombre=models.CharField(max_length=50)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='no_iniciado')    
    descripcion=models.CharField(max_length=50)
    personas=models.ForeignKey(CustomUser, on_delete=models.CASCADE)



class Proyectos(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    finalizado=models.BooleanField(default=False)
    personas=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tareas=models.ManyToManyField(Tareas)
    

    
    