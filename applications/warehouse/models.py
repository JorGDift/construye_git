from django.db import models
from applications.ironmongery.models import Ironmongery
from .managers import ProductManager, ProductCategoryManager, ProductBrandManager


# Create your models here.
class Brand(models.Model):
    # campos de la tabla
    name = models.CharField("Nombre", max_length=64)
    fk_ironmongery = models.ForeignKey(Ironmongery, on_delete=models.CASCADE)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    objects = ProductBrandManager()

    # meta datos
    class Meta:
        verbose_name = "Marca del producto"
        verbose_name_plural = "Marca de los productos"
        ordering = ['-created']

    def __str__(self):
        return str(self.name)

class ProductCategory(models.Model):
    # campos de la tabla
    name = models.CharField('Categoria', max_length=64)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    #manager asignado
    objects = ProductCategoryManager()

    # meta datos
    class Meta:
        verbose_name = "Categoria del producto"
        verbose_name_plural = "Categoria los productos"
        ordering = ['-created']

    def __str__(self):
        return str(self.name)


class ProductSubCategory(models.Model):
    name = models.CharField('Nombre', max_length=64)
    fk_product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # meta datos
    class Meta:
        verbose_name = "Sub categoria del producto"
        verbose_name_plural = "Sub categoria los productos"
        ordering = ['-created']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    STATUS_CHOICES = [
        ("0", "Alta"),
        ("1", "Baja"),
    ]

    # campos de la tabla
    name = models.CharField('Nombre', max_length=64, blank=True)
    description = models.TextField('Descripción')
    image = models.ImageField('Imagen', upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True)
    sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE, blank=True)
    price = models.FloatField('Precio')
    status = models.CharField('Estatus', max_length=1, choices=STATUS_CHOICES, default=0)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    fk_ironmongery = models.ForeignKey(Ironmongery, on_delete=models.CASCADE)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)
    

    #manager asignado
    objects = ProductManager()

    # meta datos
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created']

    def __str__(self):
        return str(self.name)
