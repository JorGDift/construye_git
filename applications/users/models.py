# models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from applications.ironmongery.models import Ironmongery

# managers
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    # campos de la tabla
    email = models.EmailField('Correo', max_length=50, blank=True, null=True, unique=True)
    firs_name = models.CharField('Nombre', max_length=50, blank=True, null=True)
    last_name = models.CharField('Apellido', max_length=50, blank=True, null=True)
    avatar = models.ImageField('Foto', upload_to='users', blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=15, blank=True, null=True)
    fk_ironmongery = models.ForeignKey(Ironmongery, on_delete=models.CASCADE, null=True)
    is_staff = models.BooleanField('Es staff', default=False)
    is_active = models.BooleanField('Es activo', default=False)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # campo para inicio de sesión
    USERNAME_FIELD = 'email'

    # campos requeridos
    REQUIRED_FIELDS = [

    ]
    
    # manger asignado
    objects = UserManager()

    # meta datos
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['-created']

    def __str__(self):
        return str(self.email)