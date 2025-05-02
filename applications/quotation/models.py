from django.db import models
from applications.users.models import User
from applications.ironmongery.models import Ironmongery
from applications.warehouse.models import Product
from .managers import QuotationDetailManager


# Create your models here.
class Quotation(models.Model):
    total = models.DecimalField('Total', decimal_places=2, max_digits=6)
    status = models.BooleanField('Status')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    fk_ironmongery = models.ForeignKey(Ironmongery, on_delete=models.CASCADE)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # meta datos
    class Meta:
        verbose_name = "Cotización"
        verbose_name_plural = "Cotizaciones"
        ordering = ['-created']

    def __str__(self):
        return str(self.fk_user)


class QuotationDetail(models.Model):
    product_amount = models.IntegerField('Cantidad de productos')
    unit_price = models.DecimalField('Precio Unitario', decimal_places=2, max_digits=6)
    fk_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fk_quotation = models.ForeignKey(Quotation, on_delete=models.CASCADE)
    created = models.DateTimeField('Creación', auto_now_add=True)
    upgrade = models.DateTimeField('Actualización', auto_now=True)

    # manger asignado
    objects = QuotationDetailManager()

    # meta datos
    class Meta:
        verbose_name = "Detalle de cotización"
        verbose_name_plural = "Detalles de cotización"
        ordering = ['-created']

    def __str__(self):
        return str(self.fk_quotation)

