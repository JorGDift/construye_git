from django.db import models
from .managers import IronmongeryManager


# Create your models here.
class IronmongeryLocation(models.Model):
    # campos de la tabla
    city = models.CharField('Ciudad', max_length=64)
    cologne = models.CharField('Colonia', max_length=64)
    street = models.CharField('Calle', max_length=64)
    postal_code = models.CharField('Código postal', max_length=64)
    outdoor_number = models.CharField('Número exterior', max_length=64)
    latitude = models.DecimalField('Latitud', max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField('Longitud', max_digits=9, decimal_places=6, null=True, blank=True)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # manger asignado
    objects = IronmongeryManager()

    # meta datos
    class Meta:
        verbose_name = "Localización de la ferreteria"
        verbose_name_plural = "Localización de las ferreteria"
        ordering = ['-created']

    def __str__(self):
        return str(self.cologne)


class Ironmongery(models.Model):
    # campos de la tabla
    name = models.CharField('Nombre', max_length=64)
    logo = models.ImageField('Logo', upload_to='IronmongeryLogo', null=True, blank=True)
    banner = models.ImageField('Banner', upload_to='IronmongeryBanner', null=True, blank=True)
    fk_location = models.ForeignKey(IronmongeryLocation, on_delete=models.CASCADE)
    phone = models.CharField(max_length=12)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # manger asignado
    objects = IronmongeryManager()

    # meta datos
    class Meta:
        verbose_name = "Ferreteria"
        verbose_name_plural = "Ferreteria"
        ordering = ['-created']

    def __str__(self):
        return str(self.name)
